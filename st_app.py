import streamlit as st
from contextlib import contextmanager
import os

import json
import uuid

st.set_page_config(layout="wide",initial_sidebar_state="collapsed")
page_styling = """
<style>
[data-testid="stAppViewContainer"] {
background-color: #000000;
background-size: cover;
background-position: center;
background-blend-mode: screen;
}

[data-testid="stHeader"] {
background-color: rgba(0,0,0,0);
}

.stChatMessage {
background-color:#000000;
}

.stChatInput {
    position: fixed; /* Ensure it's fixed at the bottom */
    bottom: 20px;
    z-index: 1000;
    background-color: rgb(14,17,23);
}

[data-testid="stBottomBlockContainer"] {
background-color:#000000;
}

div[data-testid="stTextInput"] div[data-baseweb="input"] {
        border-radius: 20px;
        background-color: #000000;
        border: #061a52;
        transition: all 0.3s ease-in-out;
    }
div[data-testid="stTextInput"] label {
        font-weight: bold;
        color:rgb(137, 137, 141);
        margin-left: 10px
    }

div[data-testid="stChatInput"] div[data-baseweb="textarea"] {
        border-radius: 30px;
    }

.stButton {
text-align:center;
}

* { font-family: 'Arial', sans-serif; /* Change this to your desired font */ }

</style>"""
st.markdown(page_styling, unsafe_allow_html= True)



@contextmanager
def custom_loader(gif_path: str):
    """
    A custom Streamlit loader context manager that displays a GIF.
    
    Args:
        gif_path (str): Path to the GIF file.
        message (str): Loading message to display.
    """
    placeholder = st.empty()
    try:
        # Display the GIF with a loading message
        placeholder.markdown(
            f"""
            <div style="text-align:center;">
                <img src="{gif_path}" alt="loading" style="width:200px;height:auto;">
            </div>
            """,
            unsafe_allow_html=True,
        )
        yield
    finally:
        # Clear the placeholder once done
        placeholder.empty()


st.header("_Shoppin Assistant_")
st.divider()
    

# initialising empty name and message in session state
if 'name' not in st.session_state:
    st.session_state.name = ''

if 'openai_api_key' not in st.session_state:
    st.session_state.openai_api_key = ''

if 'messages' not in st.session_state:
    st.session_state.messages = []


if st.session_state.name == '':
    name_input_placeholder = st.empty()  # Create a placeholder for the name input
    api_key_placeholder = st.empty()
    button_placeholder = st.empty()      # Create a placeholder for the button

    with name_input_placeholder:
        name_input = st.text_input('Enter your name')
    
    with api_key_placeholder:
        openai_api_key = st.text_input("Enter OpenAI key")

    with button_placeholder:
        submit_button = st.button('Submit')

    if submit_button and name_input and openai_api_key:
        st.session_state.name = name_input
        st.session_state.openai_api_key = openai_api_key
        os.environ['OPENAI_API_KEY'] = openai_api_key
        name_input_placeholder.empty()   # Clear the name input box
        api_key_placeholder.empty()
        button_placeholder.empty()
    elif submit_button and name_input:
        st.error("Enter OpenAI key")

# sidebar for tool calling and agent response in realtime
with st.sidebar:
    st.header("Real-time Tool Calls & Responses")
    tool_calls_container = st.empty()  # Placeholder for tool calls
    response_container = st.empty() 


def add_message(role, message_id,content):
    "Function to add message in the session state for display"
    st.session_state.messages.append({
        "id": message_id,
        "role": role, 
        "content": content
    })
    return message_id


def display_chat_history():
    "This function will display previous chat history in session state"
    # Add custom CSS for message bubbles and feedback
    st.markdown("""
        <style>
        .chat-container {
            display: flex;
            flex-direction: column;
            gap: 10px;
            padding: 10px;
        }
        .message {
            display: inline-block;
            padding: 8px 16px;
            border-radius: 20px;
            margin-bottom: 0px;
            word-wrap: break-word;
        }
        .user-message-container {
            display: flex;
            justify-content: flex-end;
            margin-right: 0px;
            margin-bottom: 20px;
        }
        .assistant-message-container {
            display: flex;
            justify-content: flex-start;
            margin-left: 0px;
        }
        .user-message {
            background-color: #3b4147;
            color: white;
            border-radius: 15px;
        }
        .assistant-message {
            background-color: #000000;
            color: white;
        }
        </style>
        """, unsafe_allow_html=True)

    for message in st.session_state.messages:
        message_id = message["id"]
        
        # Create columns for message and feedback
    
        if message["role"] == "user":
            st.markdown(f"""
                <div class="user-message-container">
                    <div class="message user-message">
                        {message["content"]}
                    </div>
                </div>
            """, unsafe_allow_html=True)
        else:
            with st.chat_message("ai", avatar="https://i.gifer.com/LCPT.gif"):
                st.markdown(f"""
                    <div class="assistant-message-container">
                        <div class="message assistant-message">
                            {message["content"]}
                        </div>
                    </div>
                """, unsafe_allow_html=True)


if st.session_state.name and st.session_state.openai_api_key:
    from src.agent import app
    
    display_chat_history()

    chat_input = st.chat_input("enter message here")
    if chat_input:
        st.markdown(f"""
                    <div class="user-message-container">
                        <div class="message user-message">
                            {chat_input}
                        </div>
                    </div>
                """, unsafe_allow_html=True)
        add_message("user",uuid.uuid4() ,chat_input)
        config = {"configurable": {"thread_id": st.session_state.name}}
        inputs = {"messages": [{"role": "user", "content": chat_input}]}

        tool_calls = []
        with custom_loader("https://i.gifer.com/LCPT.gif"):
            for output in app.stream(inputs, config):  # Adjust input accordingly
                for key, value in output.items():
                    heading = f"Output from node '{key}':"
                    
                    # Display tool calls
                    if key == "agent" and "tool_calls" in value["messages"][0].additional_kwargs:
                        func_detected = (
                            value["messages"][0]
                            .additional_kwargs.get("tool_calls")[0]
                            .get("function")
                        )
                        tool_calls.append(
                            str({
                                func_detected.get("name"): json.loads(func_detected.get("arguments"))
                            })
                        )
                        # tool_calls.append("\n\n")
                        # Update the tool call sidebar
                        tool_calls_container.write(f"**:green[Tool Calls]:**\n\n{'\n\n'.join(tool_calls)}")

                    # Update the response container
                    response_text = value["messages"][0].content
                    response_container.write(f"**:green[Response]:** \n\n{response_text}")

        
        with st.chat_message("ai", avatar="https://i.gifer.com/LCPT.gif"):
            st.markdown(value["messages"][0].content)
            add_message("ai",uuid.uuid4(),value["messages"][0].content)
# Dummy Data
PRODUCTS = [
    {"product_id": "P12345", "name": "Leather Jacket", "category": "Jackets", "color": "Black", "price": 150.00, "size": ["S", "M", "L", "XL"], "store": "FashionMart", "availability": True},
    {"product_id": "P67890", "name": "Running Shoes", "category": "Shoes", "color": "White", "price": 120.00, "size": ["8", "9", "10", "11"], "store": "ShoeWorld", "availability": True},
    {"product_id": "P11111", "name": "Denim Jeans", "category": "Jeans", "color": "Blue", "price": 80.00, "size": ["30", "32", "34", "36"], "store": "TrendyWear", "availability": False},
    {"product_id": "P22222", "name": "Floral Skirt", "category": "Skirts", "color": "Multicolor", "price": 35.00, "size": ["S", "M", "L"], "store": "StyleHub", "availability": True}
]

SHIPPING_DATA = {
    "FashionMart": {"standard": {"days": 5, "cost": 10.00}, "express": {"days": 2, "cost": 25.00}},
    "ShoeWorld": {"standard": {"days": 6, "cost": 8.00}, "express": {"days": 3, "cost": 20.00}},
    "TrendyWear": {"standard": {"days": 7, "cost": 12.00}, "express": {"days": 3, "cost": 22.00}},
    "StyleHub": {"standard": {"days": 4, "cost": 9.00}, "express": {"days": 1, "cost": 18.00}}
}

DISCOUNTS = {
    "SAVE10": {"discount_percent": 10, "applicable_stores": ["FashionMart", "ShoeWorld", "StyleHub"]},
    "FREESHIP": {"discount_percent": 100, "applicable_stores": ["TrendyWear"], "applies_to": "shipping"}
}

PRICE_COMPARISON = {
    "Leather Jacket": [
        {"store": "FashionMart", "price": 150.00},
        {"store": "StyleHub", "price": 140.00},
        {"store": "TrendyWear", "price": 155.00}
    ],
    "Running Shoes": [
        {"store": "ShoeWorld", "price": 120.00},
        {"store": "RunGear", "price": 115.00},
        {"store": "FitFoot", "price": 125.00}
    ],
    "Casual Denim Jacket": [
        {"store": "SiteA", "price": 80.00},
        {"store": "SiteB", "price": 75.00},
        {"store": "StyleHub", "price": 78.00}
    ]
}

RETURN_POLICIES = {
    "FashionMart": "Returns accepted within 30 days with original packaging.",
    "ShoeWorld": "Returns accepted within 14 days for unworn items only.",
    "TrendyWear": "No returns on sale items. 15-day return window for full-price items.",
    "SiteB": "Hassle-free returns within 30 days. Free return shipping available."
}


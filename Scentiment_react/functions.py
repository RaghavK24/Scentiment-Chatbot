import random
from datetime import datetime, timedelta


def random_date(start, end):
    """Generate a random date between `start` and `end`."""
    return start + timedelta(
        seconds=random.randint(0, int((end - start).total_seconds())),
    )


def generate_random_products():
    """Generates a list of random products."""
    products = []
    product_names = ["Scented Candle", "Essential Oil", "Fragrance Diffuser", "Aromatherapy Kit", "Incense Sticks"]
    for _ in range(random.randint(1, 5)):
        product = {
            "name": random.choice(product_names),
            "quantity": random.randint(1, 5),
            "price": f"${random.uniform(10, 100):.2f}"
        }
        products.append(product)
    return products


def get_order_details(order_id, detail_type="status"):
    if not order_id or order_id == "null":
        return "Order Id is not present ask user order id"
    # Generate random order details
    now = datetime.now()
    random_past_date = random_date(datetime(now.year - 1, 1, 1), now).strftime('%Y-%m-%d')
    random_future_date = random_date(now, datetime(now.year + 1, 1, 1)).strftime('%Y-%m-%d')
    products = generate_random_products()

    details = {
        "order_number": order_id,
        "status": random.choice(["Out for Delivery", "Delivered", "Processing", "Cancelled"]),
        "last_updated": random_past_date,
        "estimated_delivery": random_future_date,
        "shipping_details": {
            "expected_date": random_future_date,
            "carrier": random.choice(["FedEx", "UPS", "DHL", "USPS"]),
            "tracking_number": f"TRACK{random.randint(1000, 9999)}",
            "shipping_address": "1234 Scent Street, Aroma ville, AS 12345"
        },
        "payment_details": {
            "payment_method": random.choice(["Credit Card", "PayPal", "Gift Card"]),
            "payment_status": random.choice(["Completed", "Pending", "Failed"]),
            "total_amount": f"${sum(float(product['price'].strip('$')) * product['quantity'] for product in products):.2f}"
        },
        "customer_review": {
            "rating": random.choice([1, 2, 3, 4, 5]),
            "review_date": random_past_date,
            "comments": random.choice(["Great product!", "Very satisfied", "Could be better", "Not what I expected", "Exceeded expectations"])
        },
        "product_details": products,
        "promotional_offers": {
            "offer_code": f"SCENT{random.randint(100, 999)}",
            "offer_details": "Get 10% off on your next purchase",
            "valid_until": random_future_date
        },
        "customer_loyalty_points": {
            "points_earned": random.randint(10, 100),
            "points_redeemed": random.randint(0, 50),
            "balance_points": random.randint(50, 150)
        },
        "shipping_options": {
            "standard_shipping": "5-7 business days",
            "express_shipping": "2-3 business days",
            "international_shipping": "Varies by location"
        },
        "gift_wrapping_options": {
            "available": random.choice([True, False]),
            "cost": f"${random.uniform(2, 10):.2f}",
            "message": random.choice(["Happy Birthday!", "Best Wishes", "With Love", "Congratulations!"])
        }
    }

    # Return the requested detail
    if detail_type in details:
        return {key: value for key, value in details.items() if key == detail_type or key == "order_number"}
    else:
        return {"error": "Unsupported detail_type"}


def get_product_recommendations(product_type: str):
    inventory = [
        {"name": "OCEAN BREEZE", "category": "Fragrance Oil",
         "image_link": "https://www.scentiment.com/cdn/shop/files/Scentiment_Fragrance-Oil_Hotel_Ocean-Breeze_20ml_294afa0d-b4a3-438d-b0af-fa02b4c2484b.png?v=1703888139",
         "link_to_buy": "https://www.scentiment.com/products/ocean-breeze?variant=43770920534263"},
        {"name": "VEGAS PYRAMID", "category": "Fragrance Oil",
        "image_link": "https://www.scentiment.com/cdn/shop/files/Scentiment_Fragrance-Oil_Hotel_Vegas-Pyramid_20ml.png?v=1705164370&width=713",
        "link_to_buy": "https://www.scentiment.com/products/vegas-pyramid?variant=44259856548087"},
        {"name": "BRILLIANCE", "category": "Fragrance Oil",
        "image_link": "https://www.scentiment.com/cdn/shop/files/Scentiment_Fragrance-Oil_Brilliance_20ml.png?v=1706884279&width=1100",
        "link_to_buy": "https://www.scentiment.com/products/brilliance-1?variant=44312724308215"},
        {"name": "ROYALTY", "category": "Fragrance Oil",
        "image_link": "https://www.scentiment.com/cdn/shop/files/Scentiment_Fragrance-Oil_Royalty_20ml.png?v=1706884396&width=1100",
        "link_to_buy": "https://www.scentiment.com/products/royalty?variant=44312754454775"},
        {"name": "FIVE", "category": "Fragrance Oil",
        "image_link": "https://www.scentiment.com/cdn/shop/files/Scentiment_Fragrance-Oil_Five_20ml.png?v=1706909469&width=493",
        "link_to_buy": "https://www.scentiment.com/products/five?variant=44235743953143"},
        {"name": "SCENT DIFFUSER", "category": "Diffuser",
         "image_link": "https://www.scentiment.com/cdn/shop/files/Scentiment_Scent-Diffuser-Standard_Black.png?v=1705519316&width=713",
         "link_to_buy": "https://www.scentiment.com/products/scent-diffuser?variant=42991437218039"},
        {"name": "SCENT DIFFUSER PRO", "category": "Diffuser",
         "image_link": "https://www.scentiment.com/cdn/shop/files/Scentiment_Scent-Diffuser-Pro_d1f17a8b-1968-4741-b543-5f16a607c772.png?v=1706110241&width=713",
         "link_to_buy": "https://scentiment.com/products/scent-diffuser-pro?variant=43763798081783"},
        {"name": "SCENT DIFFUSER STARTER KIT", "category": "Diffuser",
         "image_link": "https://www.scentiment.com/cdn/shop/files/Scentiment_Standard-Starter-kit_Top-3_Black.png?v=1705519091&width=493",
         "link_to_buy": "https://www.scentiment.com/products/scent-diffuser-starter-kit"},
         {"name": "SCENT DIFFUSER MINI", "category": "Diffuser",
         "image_link": "https://www.scentiment.com/cdn/shop/files/Scentiment_Scent-Diffuser-Mini_Black_tilted-front.png?v=1706035828&width=1100",
         "link_to_buy": "https://www.scentiment.com/products/scent-diffuser-mini?variant=43767647797495"},
        {"name": "THE ONE CANDLE", "category": "Candles",
         "image_link": "https://www.scentiment.com/cdn/shop/files/Scentiment_Hotel_8oz_Candle_The-One_Black2.png?v=1704207538&width=493",
         "link_to_buy": "https://www.scentiment.com/products/the-one-candle"},
        {"name": "ONLY W CANDLE", "category": "Candles",
        "image_link": "https://www.scentiment.com/cdn/shop/files/Scentiment_Hotel_8oz_Candle_Only-W_Black2.png?v=1704208045&width=493",
        "link_to_buy": "https://www.scentiment.com/products/only-w-candle?variant=42991437971703"},
        {"name": "BLACK SWAN", "category": "Candles",
        "image_link": "https://www.scentiment.com/cdn/shop/files/Scentiment_Hotel_8oz_Candle_Black-Swan_Black2.png?v=1704207647&width=493",
        "link_to_buy": "https://www.scentiment.com/products/black-swan-candle?variant=42991438037239"},
        {"name": "SECRET DESIRES", "category": "Candles",
        "image_link": "https://www.scentiment.com/cdn/shop/files/Scentiment_Hotel_8oz_Candle_Secret-Desires_Black2.png?v=1704208109&width=493",
        "link_to_buy": "https://www.scentiment.com/products/secret-desires-candle?variant=43045753356535"},
        {"name": "THE ONE", "category": "room sprays",
        "image_link": "https://www.scentiment.com/cdn/shop/files/Scentiment_RoomSpray_TheOne_100ml.jpg?v=1696947136&width=493",
        "link_to_buy": "https://www.scentiment.com/products/the-one-room-spray?variant=43016104968439"},
        {"name": "OCEAN BREEZE", "category": "room sprays",
        "image_link": "https://www.scentiment.com/cdn/shop/files/Scentiment_RoomSpray_OceanBreeze_100ml.png?v=1696616912&width=493",
        "link_to_buy": "https://www.scentiment.com/products/ocean-breeze-room-spray?variant=43442217976055"},
        {"name": "DAY DREAM", "category": "room sprays",
        "image_link": "https://www.scentiment.com/cdn/shop/files/Scentiment_RoomSpray_DayDream_100ml.png?v=1696544498&width=493",
        "link_to_buy": "https://www.scentiment.com/products/day-dream-room-spray?variant=43442186911991"},
        {"name": "FRESH RAIN", "category": "room sprays",
        "image_link": "https://www.scentiment.com/cdn/shop/files/Scentiment_RoomSpray_FreshRain_100ml.png?v=1696545635&width=493",
        "link_to_buy": "https://www.scentiment.com/products/fresh-rain-room-spray?variant=43442192974071"},
    ]

    # Normalize the product type for case-insensitive comparison
    product_type_lower = product_type.lower()

    # Filter the inventory based on the product type
    filtered_products = [product for product in inventory if product_type_lower in product["category"].lower()]
    recommended_products = random.sample(filtered_products, min(3, len(filtered_products)))

    if len(recommended_products) == 0:
        return {
            "inventory": random.sample(inventory, 3),
            "data": "We were not able to find the product you are currently looking for, here is a list of our popula"
        }

    return {
        "inventory": recommended_products,
        "data": "Here is the list of inventory matching user requirements"
    }


def get_discount_offers():
    return [
        "SCENTS15FLASH : Flash sale for next 12 hours on scents oil fragrance, CLAIM: https://www.scentiment.com/products/vegas-pyramid?variant=44259856548087",
        "DIFFUSER20SALE: 20% off on new diffusers, CLAIM: https://scentiment.com/products/scent-diffuser-pro?variant=43763798081783"
    ]


def final_answer(message: str):
    return message

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
        {"name": "Winter Pines Candle: New England Edition", "category": "Scented Candle",
         "image_link": "https://www.fernweheditions.com/product_images/scented-candle-winter-pines.jpg",
         "link_to_buy": "https://www.fernweheditions.com/products/winter-pines-candle"},
        {"name": "Peridot Candle from Joanna Buchanan", "category": "Scented Candle",
         "image_link": "https://www.joannabuchanan.com/product_images/peridot-candle.jpg",
         "link_to_buy": "https://www.joannabuchanan.com/products/peridot-candle"},
        {"name": "Summer Nights Scented Candle from Perpetual Bliss", "category": "Scented Candle",
         "image_link": "https://www.perpetualblissco.com/product_images/summer-nights-candle.jpg",
         "link_to_buy": "https://www.perpetualblissco.com/products/summer-nights-candle"},
        {"name": "Vinyl Records Candle from Anecdote Candles", "category": "Scented Candle",
         "image_link": "https://www.anecdotecandles.com/product_images/vinyl-records-candle.jpg",
         "link_to_buy": "https://www.anecdotecandles.com/products/vinyl-records-candle"},
        {"name": "Sunday Morning Candle from Brooklyn Candle Studio", "category": "Scented Candle",
         "image_link": "https://www.brooklyncandlestudio.com/product_images/sunday-morning-candle.jpg",
         "link_to_buy": "https://www.brooklyncandlestudio.com/products/sunday-morning-candle"},
        {"name": "doTERRA Lavender Essential Oil", "category": "Essential Oil",
         "image_link": "https://www.doterra.com/medias/2023-doterra-lavender-essential-oil-15ml.jpg",
         "link_to_buy": "https://www.doterra.com/US/en/p/lavender-oil"},
        {"name": "Young Living Peppermint Essential Oil", "category": "Essential Oil",
         "image_link": "https://www.youngliving.com/medias/2023-young-living-peppermint-essential-oil-15ml.jpg",
         "link_to_buy": "https://www.youngliving.com/en_US/products/peppermint-essential-oil"},
        {"name": "Plant Therapy Eucalyptus Essential Oil", "category": "Essential Oil",
         "image_link": "https://www.planttherapy.com/media/catalog/product/cache/207e23213cf636ccdef205098cf3c8a3/e/u/eucalyptus-radiata-essential-oil.jpg",
         "link_to_buy": "https://www.planttherapy.com/shop/pure-essential-oils/eucalyptus"},
        {"name": "Aura Cacia Tea Tree Essential Oil", "category": "Essential Oil",
         "image_link": "https://www.auracacia.com/medias/2023-aura-cacia-tea-tree-essential-oil.jpg",
         "link_to_buy": "https://www.auracacia.com/products/tea-tree-essential-oil"},
        {"name": "Radha Beauty Frankincense Essential Oil", "category": "Essential Oil",
         "image_link": "https://www.radhabeauty.com/medias/2023-radha-beauty-frankincense-essential-oil.jpg",
         "link_to_buy": "https://www.radhabeauty.com/products/frankincense-essential-oil"},
        {"name": "Vitruvi Stone Diffuser", "category": "Fragrance Diffuser",
         "image_link": "https://www.vitruvi.com/media/catalog/product/cache/207e23213cf636ccdef205098cf3c8a3/s/t/stone-diffuser.jpg",
         "link_to_buy": "https://www.vitruvi.com/products/stone-diffuser"},
        {"name": "Muji Ultrasonic Aroma Diffuser", "category": "Fragrance Diffuser",
         "image_link": "https://www.muji.us/media/catalog/product/cache/207e23213cf636ccdef205098cf3c8a3/u/l/ultrasonic-aroma-diffuser.jpg",
         "link_to_buy": "https://www.muji.us/products/ultrasonic-aroma-diffuser"},
        {"name": "URPOWER Essential Oil Diffuser", "category": "Fragrance Diffuser",
         "image_link": "https://www.urpower.net/media/catalog/product/cache/207e23213cf636ccdef205098cf3c8a3/e/s/essential-oil-diffuser.jpg",
         "link_to_buy": "https://www.urpower.net/products/essential-oil-diffuser"},
        {"name": "InnoGear Aromatherapy Diffuser", "category": "Fragrance Diffuser",
         "image_link": "https://www.innogear.com/media/catalog/product/cache/207e23213cf636ccdef205098cf3c8a3/a/r/aromatherapy-diffuser.jpg",
         "link_to_buy": "https://www.innogear.com/products/aromatherapy-diffuser"},
        {"name": "Asakuki Essential Oil Diffuser", "category": "Fragrance Diffuser",
         "image_link": "https://www.asakuki.com/media/catalog/product/cache/207e23213cf636ccdef205098cf3c8a3/e/s/essential-oil-diffuser.jpg",
         "link_to_buy": "https://www.asakuki.com/products/essential-oil-diffuser"},
        {"name": "doTERRA Aromatherapy Kit", "category": "Aromatherapy Kit",
         "image_link": "https://www.doterra.com/media/catalog/product/cache/207e23213cf636ccdef205098cf3c8a3/a/r/aromatherapy-kit.jpg",
         "link_to_buy": "https://www.doterra.com/US/en/p/aromatherapy-kit"},
        {"name": "Young Living Starter Kit", "category": "Aromatherapy Kit",
         "image_link": "https://www.youngliving.com/medias/2023-young-living-starter-kit.jpg",
         "link_to_buy": "https://www.youngliving.com/en_US/products/starter-kit"},
        {"name": "Plant Therapy Essential Oil Set", "category": "Aromatherapy Kit",
         "image_link": "https://www.planttherapy.com/media/catalog/product/cache/207e23213cf636ccdef205098cf3c8a3/e/s/essential-oil-set.jpg",
         "link_to_buy": "https://www.planttherapy.com/shop/aromatherapy-kit"},
        {"name": "Radha Beauty Aromatherapy Kit", "category": "Aromatherapy Kit",
         "image_link": "https://www.radhabeauty.com/medias/2023-radha-beauty-aromatherapy-kit.jpg",
         "link_to_buy": "https://www.radhabeauty.com/products/aromatherapy-kit"},
        {"name": "Edens Garden Essential Oil Kit", "category": "Aromatherapy Kit",
         "image_link": "https://www.edensgarden.com/media/catalog/product/cache/207e23213cf636ccdef205098cf3c8a3/e/s/essential-oil-kit.jpg",
         "link_to_buy": "https://www.edensgarden.com/products/essential-oil-kit"},
        {"name": "Satya Nag Champa Incense Sticks", "category": "Incense Sticks",
         "image_link": "https://www.satya.co.uk/media/catalog/product/cache/207e23213cf636ccdef205098cf3c8a3/n/a/nag-champa-incense-sticks.jpg",
         "link_to_buy": "https://www.satya.co.uk/products/nag-champa-incense-sticks"},
        {"name": "Shoyeido Plum Blossom Incense Sticks", "category": "Incense Sticks",
         "image_link": "https://www.shoyeido.com/media/catalog/product/cache/207e23213cf636ccdef205098cf3c8a3/p/l/plum-blossom-incense-sticks.jpg",
         "link_to_buy": "https://www.shoyeido.com/products/plum-blossom-incense-sticks"},
        {"name": "Gonesh Extra Rich Incense Sticks", "category": "Incense Sticks",
         "image_link": "https://www.gonesh.com/media/catalog/product/cache/207e23213cf636ccdef205098cf3c8a3/e/x/extra-rich-incense-sticks.jpg",
         "link_to_buy": "https://www.gonesh.com/products/extra-rich-incense-sticks"},
        {"name": "Hem White Sage Incense Sticks", "category": "Incense Sticks",
         "image_link": "https://www.hem.com/media/catalog/product/cache/207e23213cf636ccdef205098cf3c8a3/w/h/white-sage-incense-sticks.jpg",
         "link_to_buy": "https://www.hem.com/products/white-sage-incense-sticks"},
        {"name": "Nippon Kodo Kayuragi Incense Sticks", "category": "Incense Sticks",
        "image_link": "https://www.nipponkodostore.com/cdn/shop/products/Kayuragi-Incense.jpg?v=1615581073",
        "link_to_buy": "https://www.nipponkodostore.com/products/kayuragi-incense"}
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
        "SCENTS15FLASH: Flash sale for next 12 hours on scented candles, CLAIM: https://www.fernweheditions.com/products/winter-pines-candle",
        "DIFFUSER20SALE: 20% off on new fragrance diffusers, CLAIM: https://www.vitruvi.com/products/stone-diffuser"
    ]


def final_answer(message: str):
    return message
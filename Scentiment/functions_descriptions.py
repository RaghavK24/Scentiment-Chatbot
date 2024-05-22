get_order_details_description = {
    "name": "get_order_details",
    "description": """Retrieve all information about customer orders, including shipping, cancellations. 
            For these be sure to ask for their order id before calling the fucntion. This function can also offer recommendations of fragrances and difussers as well
            as other items on offer. 
            """,
    "parameters": {
        "type": "object",
        "properties": {
            "order_id": {
                "type": "string",
                "description": "The unique identifier for each fragrance product/order id. ask user this, if user has not provided it"
            },
            "detail_type": {
                "type": "string",
                "enum": ['status', 'refund_status', 'estimated_delivery', 'delivery_details', 'cancellation_status',
                         'escalation_status', 'invoice_details'],
                "description": "specify type of request from user, categorize the query of user"
            }
        },
        "required": ["order_id", "detail_type"],
    }
}

get_product_recommendations_description = {
    "name": "get_product_recommendations",
    "description": """If the user is looking for product recommendations provide them a recommendation based on what type of products that they are looking for""",
    "parameters": {
        "type": "object",
        "properties": {
            "product_type": {
                "type": "string",
                "enum": ['Diffuser', 'Fragrance Oil', 'designer scents collection', 'room sprays', 'candles',],
                "description": "the product categories can be diffusers, fragrance oils, candles, room sprays"
            }
        },
        "required": ["product_type"],
    }
}

final_answer_description = {
    "name": "final_answer",
    "description": "Responds to the user with the result of the task or question",
    "parameters": {
        "type": "object",
        "properties": {
            "message": {
                "type": "string",
                "description": "The response message"
            }
        },
        "required": ["message"]
    }
}

get_discounts_offer_description = {
    "name": "get_discount_offers",
    "description": "In case user wants to know about discount",
    "parameters": {
        "type": "object",
        "properties": {
        },
        "required": []
    }
}
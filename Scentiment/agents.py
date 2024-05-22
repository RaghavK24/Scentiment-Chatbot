from functions import get_order_details, get_product_recommendations, final_answer, get_discount_offers
from functions_descriptions import get_order_details_description, get_product_recommendations_description, final_answer_description, get_discounts_offer_description
import json
from openai import OpenAI
import os
from dotenv import load_dotenv


load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def select_action(messages):
    agent_function = {
        'name': 'select_action',
        'description': """Selects an action
        Note: if you want to ask any details from user then trigger final_answer to ask user for the parameters you are looking for
        """,
        'parameters': {
            'type': 'object',
            'properties': {
                'thought': {
                    'type': 'string',
                    'description': 'The reasoning behind the selection of an action'
                },
                'action': {
                    'type': 'string',
                    'enum': ["final_answer", "get_discount_offers", "get_order_details", 'get_product_recommendations'],
                    # ***ensure these match function names***
                    'description': 'Action name to accomplish a task, if you want to ask any details from user then trigger final_answer to ask user for the parameters you are looking for'
                }
            },
            'required': ['thought', 'action']
        }
    }

    completion = client.chat.completions.create(
        model=os.getenv("MODEL"),
        temperature=0,
        messages=messages,
        functions=[agent_function],
        function_call={'name': 'select_action'}
    )
    print("select_action")
    print(completion)

    return json.loads(completion.choices[0].message.function_call.arguments)


def get_action_arguments(action_name, messages):
    completion = client.chat.completions.create(
        model=os.getenv("MODEL"),
        temperature=0,
        messages=messages,
        functions=[get_order_details_description, get_product_recommendations_description, final_answer_description, get_discounts_offer_description],
        # ***ensure these match functions in agent function***
        function_call={'name': action_name}
    )
    print("get_action_arguments")
    print(completion)

    return json.loads(completion.choices[0].message.function_call.arguments)


def run_action(action_name, arguments):
    if action_name == 'final_answer':
        return final_answer(**arguments)
    elif action_name == 'get_order_details':
        return get_order_details(**arguments)
    elif action_name == 'get_product_recommendations':
        return get_product_recommendations(**arguments)
    elif action_name == 'get_discount_offers':
        return get_discount_offers()
    else:
        raise NotImplementedError
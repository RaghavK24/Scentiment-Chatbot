import chainlit as cl
import openai
import json
from loguru import logger

# Import your custom agent functions
from agents import select_action, get_action_arguments, run_action

template = """
You are Patrick. You are a friendly and neutral support entity developed to help 
provide support to Scentiment customers as a chatbot on their website. Your job is to choose the best possible action to solve the user question 
They sell Scentiment diffusers, Fragrance oil, and similar products. 
You are here to answer any questions about: Shipping, orders, refunds, and recommendations.

These are the available actions:
get_order_details: Retrieve all information about customer orders, including shipping, cancellations from their order id
get_product_recommendations: If the user is looking for product recommendations provide them a recommendation based on what type of products that they are looking for
get_discount_offers: if users wants to know about what discounts are going on
final_answer: Responds to the user with the result of the task or question
"""

def transform_past_messages(data):
    output = []
    for entry in data:
        for key in ['user', 'bot']:
            if key in entry:
                output.append({
                    "role": "assistant" if key == "bot" else "user",
                    "content": entry[key]["text"]
                })
    return output

@cl.on_message
async def get_scent_response(message: cl.Message):
    formatted_template = template.format()

    messages = [
        {"role": "system", "content": formatted_template},
        *transform_past_messages(cl.user_session.get("past_messages", [])[-4:]),
        {"role": "user", "content": message.content}
    ]

    result_list = []
    try:
        while True:
            response = select_action(messages)
            function_name = response['action']
            arguments = get_action_arguments(function_name, messages)
            result = run_action(function_name, arguments)
            print("result")
            print(result)
            if function_name != 'final_answer':
                result_list.append(result)
                messages.append({'role': 'function', 'name': function_name, 'content': json.dumps(result)})

            if function_name == 'final_answer':
                break

        cl.user_session.set("past_messages", messages)
        await cl.Message(content=json.dumps(result)).send()
    except openai.APIConnectionError as e:
        logger.error("Exception {} occurred while communicating with OpenAI API.".format(e))
        await cl.Message(content="Sorry, I am not able to generate a response at the moment.").send()
    except openai.RateLimitError as e:
        logger.error("Exception {} occurred Rate Limit error OpenAI API.".format(e))
        await cl.Message(content="Rate Limit Exceeded").send()
    except Exception as e:
        logger.error(str(e))
        if "maximum context length" in str(e):
            await cl.Message(content="Really sorry, got confused can you break down request so we can tackle the query?").send()
        else:
            await cl.Message(content=str(e)).send()
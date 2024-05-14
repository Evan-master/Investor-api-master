from openai import OpenAI
import configs.config
import handle.api
import logging
from handle.deal_function import *

logging.basicConfig(filename='../logging.log', level=logging.INFO, format='%(asctime)s %(levelname)s:%(message)s')

client = OpenAI(api_key=configs.config.get_openAIapi())
apikey = configs.config.get_stockApi()


def stock_investor(prompt):
    messages = [{"role": "user", "content": prompt}]
    tools = configs.config.get_config()

    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo-16k-0613",
            messages=messages,
            tools=tools,
            tool_choice="auto"
        )

        response_message = response.choices[0].message
        messages.append(response_message)
        logging.info("response_message:{}".format(response_message))

        tool_calls = response_message.tool_calls
        if tool_calls:
            logging.info("tool_calls:{}".format(tool_calls))

            for tool_call in tool_calls:
                function_name = tool_call.function.name
                function_to_call = available_functions.get(function_name)
                function_args = json.loads(tool_call.function.arguments)
                function_args['apikey'] = apikey

                function_response = handle_function_call(function_to_call, function_args)
                tool_response = create_tool_response(tool_call, function_response)
                messages.append(tool_response)

            second_response = client.chat.completions.create(
                model="gpt-3.5-turbo-0125",
                messages=messages,
            )
            return second_response.choices[0].message.content

    except Exception as e:
        logging.error(f"Error in stock_investor function: {e}")
        return "An error occurred."


def handle_function_call(function_to_call, function_args):
    if 'tickers' in function_args:
        return function_to_call(
            tickers=function_args.get('tickers'),
            apikey=function_args.get('apikey'),
            limit=function_args.get('limit')
        )
    elif len(function_args) == 4:
        return function_to_call(
            symbol=function_args.get('symbol'),
            interval=function_args.get('interval'),
            apiKey=function_args.get('apikey')
        )
    else:
        return function_to_call(
            symbol=function_args.get('symbol'),
            apikey=function_args.get('apikey')
        )


def create_tool_response(tool_call, function_response):
    if count_json_tokens(function_response) > 8000:
        function_response = simplify_news_json(function_response)
    return {
        "tool_call_id": tool_call.id,
        "role": "tool",
        "name": tool_call.function.name,
        "content": json.dumps(function_response),
    }


available_functions = {
    "get_intraday_data": handle.api.get_intraday_data,
    "get_quote_data": handle.api.get_quote_data,
    "get_weeklyadjust_data": handle.api.get_weeklyadjust_data,
    "get_monthad_data": handle.api.get_monthad_data,
    "get_news_data": handle.api.get_news_data,
    "get_income_data": handle.api.get_income_data,
    "get_balance_data": handle.api.get_balance_data,
    "get_cash_data": handle.api.get_cash_data
}

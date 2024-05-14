import json


def simplify_news_json(original_json, company_filter="TSLA", max_news=10):
    data = original_json

    simplified_news = []
    for item in data["feed"]:
        if any(ticker["ticker"] == company_filter for ticker in item.get("ticker_sentiment", [])):
            news_item = {key: item.get(key, "N/A") for key in item}
            simplified_news.append(news_item)
            if len(simplified_news) >= max_news:
                break

    return json.dumps(simplified_news, indent=4)


def count_json_tokens(item):
    if isinstance(item, dict):

        return sum(count_json_tokens(key) + count_json_tokens(value) for key, value in item.items()) + len(item) - 1 + 2
    elif isinstance(item, list):

        return sum(count_json_tokens(elem) for elem in item) + len(item) - 1 + 2
    elif isinstance(item, str):

        return 1 + 2
    else:

        return 1

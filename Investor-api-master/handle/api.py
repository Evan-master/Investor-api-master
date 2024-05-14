import requests


def get_intraday_data(symbol, interval, apikey, function="TIME_SERIES_INTRADAY"):
    response = requests.get(
        "https://www.alphavantage.co/query",
        params={
            "function": function,
            "symbol": symbol,
            "interval": interval,
            "apikey": apikey
        }
    )
    return response.json()


def get_weeklyadjust_data(symbol, apikey, function="TIME_SERIES_WEEKLY"):
    response = requests.get(
        "https://www.alphavantage.co/query",
        params={
            "function": function,
            "symbol": symbol,
            "apikey": apikey
        }
    )
    return response.json()


def get_monthad_data(symbol, apikey, function="TIME_SERIES_MONTHAD"):
    response = requests.get(
        "https://www.alphavantage.co/query",
        params={
            "function": function,
            "symbol": symbol,
            "apikey": apikey
        }
    )
    return response.json()


def get_quote_data(symbol, apikey, function="GLOBAL_QUOTE"):
    response = requests.get(
        "https://www.alphavantage.co/query",
        params={
            "function": function,
            "symbol": symbol,
            "apikey": apikey
        }
    )
    return response.json()


def get_news_data(tickers, apikey, topics=None, sort=None, time_from=None, time_to=None, limit=10,
                  function="NEWS_SENTIMENT"):
    params = {
        "function": function,
        "tickers": tickers,
        "apikey": apikey,
        "topics": topics,
        "sort": sort,
        "time_from": time_from,
        "time_to": time_to,
        "limit": limit
    }
    # 移除None值的参数
    params = {k: v for k, v in params.items() if v is not None}

    response = requests.get(
        "https://www.alphavantage.co/query",
        params=params
    )
    return response.json()


def get_income_data(symbol, apikey, function="TIME_SERIES_INCOME"):
    response = requests.get(
        "https://www.alphavantage.co/query",
        params={
            "function": function,
            "symbol": symbol,
            "apikey": apikey
        }
    )
    return response.json()


def get_balance_data(symbol, apikey, function="TIME_SERIES_BALANCE"):
    response = requests.get(
        "https://www.alphavantage.co/query",
        params={
            "function": function,
            "symbol": symbol,
            "apikey": apikey
        }
    )
    return response.json()


def get_cash_data(symbol, apikey, function="TIME_SERIES_CASH"):
    response = requests.get(
        "https://www.alphavantage.co/query",
        params={
            "function": function,
            "symbol": symbol,
            "apikey": apikey
        }
    )
    return response.json()

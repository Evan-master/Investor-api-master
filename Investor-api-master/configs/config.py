def get_config():
    cfg = [
        {
            "type": "function",
            "function": {
                "name": "get_intraday_data",
                "description": "Get intraday stock data",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "function": {"type": "string"},
                        "symbol": {"type": "string"},
                        "interval": {"type": "string"},
                        "apikey": {"type": "string"}
                    },
                    "required": ["function", "symbol", "interval", "apikey"]
                }
            }
        },
        {
            "type": "function",
            "function": {
                "name": "get_weeklyadjust_data",
                "description": "Get weekly adjusted stock data",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "function": {"type": "string"},
                        "symbol": {"type": "string"},
                        "apikey": {"type": "string"}
                    },
                    "required": ["function", "symbol", "apikey"]
                }
            }
        },
        {
            "type": "function",
            "function": {
                "name": "get_monthad_data",
                "description": "Get monthly adjusted stock data",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "function": {"type": "string"},
                        "symbol": {"type": "string"},
                        "apikey": {"type": "string"}
                    },
                    "required": ["function", "symbol", "apikey"]
                }
            }
        },
        {
            "type": "function",
            "function": {
                "name": "get_quote_data",
                "description": "Get stock quote data",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "function": {"type": "string"},
                        "symbol": {"type": "string"},
                        "apikey": {"type": "string"}
                    },
                    "required": ["function", "symbol", "apikey"]
                }
            }
        },
        {
            "type": "function",
            "function": {
                "name": "get_news_data",
                "description": "Retrieve the latest stock market news for specified tickers, with optional filtering by topics and sorting.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "function": {
                            "type": "string",
                            "description": "The API function to call, e.g., NEWS_SENTIMENT."
                        },
                        "tickers": {
                            "type": "string",
                            "description": "Comma-separated list of stock symbols (tickers) to retrieve news for."
                        },
                        "topics": {
                            "type": "string",
                            "default": None,
                            "description": "Optional topics to filter news articles, e.g., technology, ipo."
                        },
                        "sort": {
                            "type": "string",
                            "default": None,
                            "description": "Optional sorting mode for news articles, e.g., latest, earliest, relevance."
                        },
                        "time_range": {
                            "type": "string",
                            "default": None,
                            "description": "Optional time range for news articles, e.g., 20220410T0130-20220411T0130."
                        },
                        "apikey": {
                            "type": "string",
                            "description": "Your API key for authentication."
                        },
                        "limit": {
                            "type": "string",
                            "default": 10,
                            "description": "You only need to return the number of stories within ten"
                        }
                    },
                    "required": ["function", "tickers", "apikey"]
                }
            }
        },
        {
            "type": "function",
            "function": {
                "name": "get_income_data",
                "description": "Get income statement data",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "function": {"type": "string"},
                        "symbol": {"type": "string"},
                        "apikey": {"type": "string"}
                    },
                    "required": ["function", "symbol", "apikey"]
                }
            }
        },
        {
            "type": "function",
            "function": {
                "name": "get_balance_data",
                "description": "Get balance sheet data",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "function": {"type": "string"},
                        "symbol": {"type": "string"},
                        "apikey": {"type": "string"}
                    },
                    "required": ["function", "symbol", "apikey"]
                }
            }
        },
        {
            "type": "function",
            "function": {
                "name": "get_cash_data",
                "description": "Get cash flow data",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "function": {"type": "string"},
                        "symbol": {"type": "string"},
                        "apikey": {"type": "string"}
                    },
                    "required": ["function", "symbol", "apikey"]
                }
            }
        }
    ]

    return cfg


def get_openAIapi():
    apikey = "<apikey>"
    return apikey


def get_stockApi():
    apikey = "<apikey>"
    return apikey


def get_port():
    return 8086

import investor

if __name__ == '__main__':
    prompt = '苹果公司的股票情况怎么样'
    answer = investor.stock_investor(prompt)
    print(answer)
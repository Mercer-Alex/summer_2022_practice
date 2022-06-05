def max_profit(prices):
    curr_max = 0
    min_price = 1000

    for x in prices:
        if x < min_price:
            min_price = x
        if x - min_price > curr_max:
            curr_max = x - min_price
    return curr_max


stock = [7, 1, 5, 3, 6, 4]

print(max_profit(stock))

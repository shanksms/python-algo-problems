def buySellStockOnce(prices):
    min_price_so_far , max_profit = float ('inf') , 0.0
    for price in prices:
        max_profit_sell_today = price - min_price_so_far
        print(max_profit_sell_today)
        max_profit = max(max_profit, max_profit_sell_today)
        min_price_so_far = min(min_price_so_far, price)
    return max_profit

if __name__ == '__main__':
    print(buySellStockOnce([310,315,275,295,260,270,290,230,255,250]))

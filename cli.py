from bot import BasicBot
from utils import (
    validate_order_side,
    validate_order_type,
    validate_symbol,
    parse_float_input
)

def main():
    bot = BasicBot()

    print("Welcome to Binance Futures Testnet Trading Bot")

    while True:
        symbol = input("Enter trading symbol (e.g. BTCUSDT): ").upper()
        if validate_symbol(symbol):
            break
        print("Invalid symbol. Must be alphanumeric and end with 'USDT'.")

    while True:
        side = input("Enter order side (buy/sell): ").lower()
        if validate_order_side(side):
            break
        print("Invalid side. Use 'buy' or 'sell'.")

    while True:
        order_type = input("Enter order type (market/limit): ").lower()
        if validate_order_type(order_type):
            break
        print("Invalid order type. Use 'market' or 'limit'.")

    quantity = parse_float_input("Enter quantity: ")

    if order_type == "market":
        bot.place_market_order(symbol, side, quantity)
    elif order_type == "limit":
        price = parse_float_input("Enter limit price: ")
        bot.place_limit_order(symbol, side, quantity, price)

if __name__ == "__main__":
    main()
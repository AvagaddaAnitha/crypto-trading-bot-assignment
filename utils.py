def validate_order_side(side: str) -> bool:
    return side.lower() in ['buy', 'sell']

def validate_order_type(order_type: str) -> bool:
    return order_type.lower() in ['market', 'limit']

def validate_symbol(symbol: str) -> bool:
    # Very basic validation – production code should check against Binance symbol list
    return symbol.isalnum() and symbol.upper().endswith("USDT")

def parse_float_input(prompt: str) -> float:
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid number. Please enter a valid numeric value.")

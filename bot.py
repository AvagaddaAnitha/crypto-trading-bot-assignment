from binance.client import Client
from binance.enums import *
from config import API_KEY, API_SECRET, BASE_URL
from logger import setup_logger

logger = setup_logger()

class BasicBot:
    def __init__(self):
        self.client = Client(API_KEY, API_SECRET)
        self.client.FUTURES_URL = BASE_URL
        self.client.API_URL = BASE_URL

    def place_market_order(self, symbol, side, quantity):
        try:
            order = self.client.futures_create_order(
                symbol=symbol,
                side=SIDE_BUY if side == 'buy' else SIDE_SELL,
                type=ORDER_TYPE_MARKET,
                quantity=quantity
            )
            logger.info(f"Market Order: {order}")
            return order
        except Exception as e:
            logger.error(f"Market order error: {e}")
            return None

    def place_limit_order(self, symbol, side, quantity, price):
        try:
            order = self.client.futures_create_order(
                symbol=symbol,
                side=SIDE_BUY if side == 'buy' else SIDE_SELL,
                type=ORDER_TYPE_LIMIT,
                quantity=quantity,
                price=price,
                timeInForce=TIME_IN_FORCE_GTC
            )
            logger.info(f"Limit Order: {order}")
            return order
        except Exception as e:
            logger.error(f"Limit order error: {e}")
            return None
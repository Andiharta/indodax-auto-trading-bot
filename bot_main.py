# FILE: bot_main.py

import argparse
import os
import time
from dotenv import load_dotenv

from modules.api_wrapper import IndodaxAPI
from modules.scorer import get_potential_pairs
from modules.storage import TransactionStorage
from modules.utils import format_currency, log, get_timestamp

# Load configuration from .env file
load_dotenv()
API_KEY = os.getenv("API_KEY")
API_SECRET = os.getenv("API_SECRET")
BUY_AMOUNT = int(os.getenv("BUY_AMOUNT", 10000))
SELL_TIMEOUT = int(os.getenv("SELL_TIMEOUT", 900))  # 15 minutes default
CSV_PATH = os.getenv("CSV_PATH", "transaction_history.csv")

def main(mode):
    log(f"Bot started in {mode.upper()} mode.")

    api = IndodaxAPI(api_key=API_KEY, api_secret=API_SECRET, mode=mode)
    storage = TransactionStorage(CSV_PATH)

    while True:
        # Step 1: Select potential pairs using scorer
        potential_pairs = get_potential_pairs(api)
        log(f"Potential pairs: {potential_pairs}")

        for pair in potential_pairs:
            last_price = api.get_ticker(pair)
            qty = BUY_AMOUNT / last_price

            # Step 2: Place buy order
            buy_result = api.order_buy(pair, qty, last_price)
            log(f"Buy result: {buy_result}")

            buy_time = time.time()
            target_price = last_price * 1.01  # Example: sell at +1%
            sold = False

            # Step 3: Monitor price and auto sell
            while time.time() - buy_time < SELL_TIMEOUT:
                current_price = api.get_ticker(pair)
                log(f"Monitoring {pair}: Current price {format_currency(current_price)}")
                if current_price >= target_price:
                    sell_result = api.order_sell(pair, qty, current_price)
                    log(f"Sold {pair} at target price! Sell result: {sell_result}")
                    sold = True
                    storage.save_transaction(get_timestamp(), pair, qty, last_price, current_price, mode)
                    break
                time.sleep(5)
            if not sold:
                # Sell at market price after timeout
                sell_result = api.order_sell(pair, qty, current_price)
                log(f"Timeout reached. Sold {pair} at market price. Sell result: {sell_result}")
                storage.save_transaction(get_timestamp(), pair, qty, last_price, current_price, mode)

        log("Waiting for next loop...\n")
        time.sleep(60)  # Wait 1 minute before next iteration

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Indodax Auto Trading Bot")
    parser.add_argument("--mode", choices=["paper", "live"], default="paper", help="Choose bot mode: paper or live")
    args = parser.parse_args()
    main(args.mode)
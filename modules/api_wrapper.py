# FILE: modules/api_wrapper.py

import time
from modules.utils import log

class IndodaxAPI:
    def __init__(self, api_key=None, api_secret=None, mode="paper"):
        self.api_key = api_key
        self.api_secret = api_secret
        self.mode = mode

    def get_ticker(self, pair):
        """
        Ambil harga terakhir dari pair.
        Untuk demo, return harga random.
        Di live mode, implementasi API Indodax.
        """
        import random
        price = random.uniform(1000, 100000)
        log(f"[{self.mode}] Ticker {pair}: {price}")
        return price

    def order_buy(self, pair, qty, price):
        """
        Order beli pada pair.
        Paper mode: hanya print transaksi.
        Live mode: implementasi API Indodax.
        """
        if self.mode == "paper":
            log(f"[PAPER] Buy {qty} {pair} at Rp{price}")
            return {"status": "success", "pair": pair, "qty": qty, "price": price}
        else:
            # TODO: implement Indodax live buy API
            log(f"[LIVE] Buy {qty} {pair} at Rp{price} (API not implemented)")
            return {"status": "live_mock", "pair": pair, "qty": qty, "price": price}

    def order_sell(self, pair, qty, price):
        """
        Order jual pada pair.
        Paper mode: hanya print transaksi.
        Live mode: implementasi API Indodax.
        """
        if self.mode == "paper":
            log(f"[PAPER] Sell {qty} {pair} at Rp{price}")
            return {"status": "success", "pair": pair, "qty": qty, "price": price}
        else:
            # TODO: implement Indodax live sell API
            log(f"[LIVE] Sell {qty} {pair} at Rp{price} (API not implemented)")
            return {"status": "live_mock", "pair": pair, "qty": qty, "price": price}
# FILE: modules/storage.py

import csv
import os

class TransactionStorage:
    """
    Kelas untuk menyimpan riwayat transaksi ke CSV pada paper mode.
    """
    def __init__(self, csv_path):
        self.csv_path = csv_path
        if not os.path.exists(self.csv_path):
            with open(self.csv_path, mode="w", newline="") as f:
                writer = csv.writer(f)
                writer.writerow(["timestamp", "pair", "qty", "buy_price", "sell_price", "mode"])

    def save_transaction(self, timestamp, pair, qty, buy_price, sell_price, mode):
        with open(self.csv_path, mode="a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([timestamp, pair, qty, buy_price, sell_price, mode])
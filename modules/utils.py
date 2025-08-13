# FILE: modules/utils.py

import time

def format_currency(value):
    """
    Format angka ke Rupiah dengan pemisah ribuan.
    """
    return "Rp{:,.0f}".format(value)

def get_timestamp():
    """
    Ambil timestamp sekarang.
    """
    return int(time.time())

def log(message):
    """
    Logging sederhana dengan timestamp.
    """
    print(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] {message}")

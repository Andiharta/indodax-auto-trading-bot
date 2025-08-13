# FILE: modules/scorer.py

from modules.utils import log

def get_potential_pairs(api):
    """
    Pilih pair potensial untuk dibeli.
    Implementasi dummy: return beberapa pair tetap.
    Bisa diganti scoring berdasarkan tren harga.
    """
    log("Scoring pairs for potential buy...")
    # Contoh fixed list
    return ["btc_idr", "eth_idr", "ada_idr"]

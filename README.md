# indodax-auto-trading-bot

Bot trading otomatis untuk Indodax menggunakan Python.

## ✨ Fitur
- Auto pilih pair potensial (scoring sederhana, bisa upgrade ke AI/ML)
- Auto beli Rp10.000 per pair
- Auto pasang jual dengan target price dan stop-loss
- Pantau order selama 15 menit, jual otomatis jika target tercapai atau timeout
- **Paper trading mode** untuk simulasi aman tanpa risiko
- Struktur modular dan siap untuk koneksi API Indodax resmi

## 📦 Instalasi

### 1. Clone repository
```bash
git clone https://github.com/Andiharta/indodax-auto-trading-bot.git
cd indodax-auto-trading-bot


2. Buat environment & install dependencies

python -m venv venv
source venv/bin/activate   # Linux / Mac
venv\\Scripts\\activate    # Windows

pip install -r requirements.txt

3. Konfigurasi

Copy .env.example menjadi .env

Isi API_KEY dan API_SECRET jika ingin live mode

Ubah MODE=paper untuk simulasi


Contoh:

API_KEY=YOUR_API_KEY
API_SECRET=YOUR_API_SECRET
MODE=paper
BUY_AMOUNT_IDR=10000
CHECK_INTERVAL=30
MAX_CONCURRENT_TRADES=5
PAIRS=btc_idr,eth_idr,doge_idr,trx_idr

🚀 Menjalankan Bot

Paper mode (simulasi)

python bot_main.py --mode paper

Live mode (nyata, hati-hati!)

python bot_main.py --mode live

> Peringatan: Live mode membutuhkan implementasi IndodaxAPI di modules/api_wrapper.py sesuai dokumentasi API resmi Indodax. Pastikan API key hanya memiliki izin read dan trade (tidak ada withdrawal).



📂 Struktur Folder

.
├── bot_main.py
├── modules/
│   ├── __init__.py
│   ├── api_wrapper.py
│   ├── scorer.py
│   ├── storage.py
│   └── utils.py
├── requirements.txt
├── Dockerfile
├── .env.example
└── README.md

⚠️ Disclaimer

Trading cryptocurrency memiliki risiko tinggi. Gunakan bot ini dengan tanggung jawab Anda sendiri. Lakukan uji coba di paper mode terlebih dahulu sebelum live trading.

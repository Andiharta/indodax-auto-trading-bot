# FILE: README.md

# Indodax Auto Trading Bot

Bot trading otomatis untuk Indodax, memilih pair potensial, membeli Rp10.000/pair, dan auto jual dalam 15 menit. Mendukung **paper mode** (simulasi) dan **live mode** via API Indodax.

## Fitur

- Otomatis memilih pair potensial untuk trading.
- Membeli tiap pair dengan nominal tetap (default Rp10.000).
- Otomatis jual dalam 15 menit atau saat profit target tercapai.
- Support mode **paper** (simulasi) dan **live** (real API Indodax).
- Riwayat transaksi (paper mode) disimpan ke CSV.
- Logging sederhana, siap dijalankan di Termux/CLI.

## Instalasi

1. **Clone repo:**

    ```bash
    git clone https://github.com/Andiharta/indodax-auto-trading-bot.git
    cd indodax-auto-trading-bot
    ```

2. **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

3. **Konfigurasi .env:**

    Salin `.env.example` menjadi `.env` dan isi sesuai kebutuhan.

    ```bash
    cp .env.example .env
    ```

    Edit `.env`:

    - `API_KEY` dan `API_SECRET`: isi jika ingin mode live.
    - `BUY_AMOUNT`: nominal beli per pair (Rp), default 10000.
    - `SELL_TIMEOUT`: waktu tunggu auto jual (detik), default 900 (15 menit).
    - `CSV_PATH`: path file riwayat transaksi.

## Menjalankan Bot

### Mode Simulasi (Paper)

```bash
python bot_main.py --mode paper
```

### Mode Live (API Indodax)

```bash
python bot_main.py --mode live
```

> **Catatan:** Mode live hanya template, butuh implementasi API Indodax pada `modules/api_wrapper.py`. Mode paper tidak butuh API Indodax.

### Jalankan di Termux

Pastikan Python dan pip sudah terinstall di Termux.

## Kontribusi

Pull Request dan masukan dipersilakan!

## Lisensi

MIT

# Crypto Trading Bot – Junior Python Developer Assignment

This project is a **Binance Futures Testnet Crypto Trading Bot** built as part of the assignment for the Junior Python Developer role. It allows users to place **market** and **limit** orders interactively via the command line.

---

## 📁 Project Structure

- `bot.py` – Core trading logic using Binance Futures API.
- `cli.py` – CLI interface to interact with the bot.
- `config.py` – Stores API credentials and testnet endpoint.
- `logger.py` – Logger configuration to capture and store logs.
- `utils.py` – Input validation utilities.
- `log output` – Logs are printed to the console via the `logger.py` setup.

---

## ⚙️ Features

- Place **Market Orders**
- Place **Limit Orders**
- Input validation for:
  - Symbols (e.g., BTCUSDT)
  - Order side (buy/sell)
  - Order type (market/limit)
- Logs all API responses and errors in real-time

---

## 📌 Log Files

Logging is handled through Python's `logging` module (see `logger.py`):
- Logs include timestamp, level, and message.
- Sample logs for:
  - Successful market/limit orders
  - Errors during order placement

> 📍 Note: Logs are currently streamed to the console. To save logs to a file, modify `logging.StreamHandler()` in `logger.py` to `logging.FileHandler('logfile.log')`.

---

## 🛠 How to Run

1. Replace `API_KEY` and `API_SECRET` in `config.py` with your Binance **Futures Testnet** credentials.
2. Install `python-binance` if not already:
   ```bash
   pip install python-binance

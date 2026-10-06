from flask import Flask, jsonify
import os, threading, time, requests
from datetime import datetime

app = Flask(__name__)

CAPITAL_INICIAL = 5.64
status_bot = {
    "status": "online",
    "capital": CAPITAL_INICIAL,
    "trades": 0,
    "lucro": 0.0,
    "ultimo_sinal": "Aguardando mercado..."
}

def bot_loop():
    while True:
        try:
            status_bot["ultimo_sinal"] = f"Analisando... {datetime.now().strftime('%H:%M:%S')}"
            time.sleep(30)
        except Exception as e:
            print(e)
            time.sleep(10)

threading.Thread(target=bot_loop, daemon=True).start()

@app.route('/')
def home():
    return f"""
    <h1>🤖 BOT DO GATO - ONLINE</h1>
    <p>Capital: ${status_bot['capital']}</p>
    <p>Trades: {status_bot['trades']}</p>
    <p>Status: {status_bot['ultimo_sinal']}</p>
    <p>Link do Render: bot-do-gato.onrender.com</p>
    """

@app.route('/status')
def status():
    return jsonify(status_bot)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)

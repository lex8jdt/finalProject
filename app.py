import config as cfg
import multiprocessing
import threading
import signal

from flask import Flask
from api import api_bp
from bot.discord_bot import run_bot, close_bot

def create_app():
    app = Flask(__name__)

    app.register_blueprint(api_bp)

    return app

app = create_app()

def run_flask():
    app.run(debug=cfg.DEBUG, use_reloader=False)

if __name__ == '__main__':
    signal.signal(signal.SIGINT, signal.SIG_DFL)
    
    discord_thread = threading.Thread(target=run_bot)
    discord_thread.start()
    flask_thread = threading.Thread(target=run_flask)
    flask_thread.start()
    
    try:
        discord_thread.join()
        flask_thread.join()
    except KeyboardInterrupt:
        close_bot()
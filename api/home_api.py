import threading
from flask import Blueprint, render_template
from bot import discord_bot

home_bp = Blueprint('home', __name__)

@home_bp.route('/')
def home():
    return render_template('index.html')

@home_bp.route('/bot-try')
def bot_try():
    discord_bot.call_async_send_message(
        '''
            __Hello from FLASK__
        ''')
    return '<h1>Hello</h1>'
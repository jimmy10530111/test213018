
import pymysql.cursors


from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *

app = Flask(__name__)




# Channel Access Token
line_bot_api = LineBotApi('1bb5FOnOqLXnv2W6KeZ+3ms0neF09E8h2KVffW1wjiqSGskGKLQ7/2PDNNBxUWTg6M8UzBtADTqq+hDcec0SbHKRHcVb9Fs8714MJA8MmLWWracX3dnFmJAz5vE7pJErclmgPAE60+M74Cm56+LyEgdB04t89/1O/w1cDnyilFU=')
# Channel Secret
handler = WebhookHandler('705311288e013e163f3ff55d0e735958')

# 監聽所有來自 /callback 的 Post Request
@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'

# 處理訊息
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    
    
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text=event.message.text))
    

import os
_host = '127.0.0.1'
_port = 5000
servername = self.config['SERVER_NAME']
if server_name:
    if server_name and ':' in server_name:
        _host, _port = servername.split(':', 1)
if host is None:
    host = _host
if port is None:
    port = _port

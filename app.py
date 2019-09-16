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
    message = TextSendMessage(text=event.message.text)
    line_bot_api.reply_message(event.reply_token, message)

import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)

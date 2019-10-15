from sqlalchemy import create_engine
import mysql.connector


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
userrid = 'U056904eae738c9778826ba74bc9f2d62'

engine=create_engine('mysql+mysqlconnector://cat:cat@163.17.27.180/cat')
re=engine.connect()
re.execute("SELECT * FROM `gato` WHERE `Date` LIKE '2019-10-07'")
result = re.fetchall()


message = TextSendMessage(result)
#line_bot_api.reply_message(event.reply_token, message)
line_bot_api.push_message(userrid, message)

message2 = TextSendMessage("111111")
line_bot_api.push_message(userrid, message2)
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

        message = TextSendMessage(result)
        line_bot_api.reply_message(event.reply_token, message)


    """
    elif event.message.text == "東方果實蠅":
        line_bot_api.reply_message(event.reply_token, ImageSendMessage(
            original_content_url='https://drive.google.com/uc?export=download&id=1PHSDd75mPEHT5u3uOy_z0J8tyixVVRhK',
            preview_image_url='https://drive.google.com/uc?export=download&id=1PHSDd75mPEHT5u3uOy_z0J8tyixVVRhK'))

    
    
    if event.message.txt == "20191007":
        message = TextSendMessage("測試")
        line_bot_api.reply_message(event.reply_token, message)
        
    """


            

import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 50000))
    app.run(host='0.0.0.0', port=port)

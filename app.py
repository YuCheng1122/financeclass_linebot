from flask import Flask, request, abort, jsonify
from flask_cors import CORS

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *

import func

from urllib.parse import parse_qsl

import requests

app = Flask(__name__)
CORS(app)

# 必須放上自己的Channel Access Token
line_bot_api = LineBotApi('你的Channel Access Token')
# 必須放上自己的Channel Secret
handler = WebhookHandler('你的Channel Secret')

# 監聽所有來自 /callback 的 Post Request
@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    print('THE BODY: ' + body)
    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'

# 處理訊息
# event.message 為 TextMessage 實例。所以此為處理 TextMessage 的 handler
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    if event.source.user_id != "Udeadbeefdeadbeefdeadbeefdeadbeef":
        mtext = event.message.text
        if mtext == "今晚來點":
            func.sendQuicklyReply(event)
        elif mtext == "正餐!":
            func.meal(event)
        elif mtext == "下午茶!":
            func.snack(event)
        elif mtext == "飲料!":
            func.drink(event)
        elif mtext == "查詢天氣":
            func.HowIsTheWeather(event)
        elif mtext == "查詢匯率":
            func.exchangeRate(event)
        elif mtext == "傳個圖片":
            func.sendImage(event)
        elif mtext == "傳個影片":
            func.sendVideo(event)
        elif mtext == "不吃了!":
            func.nothing(event)
        elif mtext == "先不要拜託!":
            #當要連續傳送兩個訊息以上(圖片或文字都可以)，可以用陣列的方式傳送
            message1 = ImageSendMessage(original_content_url='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT98muRclysrk74pPVlN-Os77MZz5-j6JbpqQ&usqp=CAU',preview_image_url='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT98muRclysrk74pPVlN-Os77MZz5-j6JbpqQ&usqp=CAU')
            message2 = TextSendMessage(text = '不要就算了')
            line_bot_api.reply_message(event.reply_token, [message1, message2])
        else:
            message = TextSendMessage(text=event.message.text)
            line_bot_api.reply_message(event.reply_token, message)#讓linebot回傳你說的話(echobot)

# event.message 為 LocationMessage 實例。所以此為處理 LocationMessage 的 handler
@handler.add(MessageEvent, message=LocationMessage)
def location_message(event):
    if event.source.user_id != "Udeadbeefdeadbeefdeadbeefdeadbeef":
        func.sendWeather(event)
import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)

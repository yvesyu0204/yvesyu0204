from line_bot_api import *
from events.basic import  *
from events.oil import *

app=Flask(__name__)

line_bot_api= LineBotApi("Cb1zn5Z1dBNV1osEa7otXndEk3Drfx8FgJdhtMzYyy6zEqzZI/Qck6YKb4qhuQThZcwbL6DM7y4hvAhztthuWlsizsVyuKNMBGNOWe7OGsnQGybzol83rn6zIDMwHAlczfM3RnPEyOxLYKIFwyXlQgdB04t89/1O/w1cDnyilFU=")
handler=WebhookHandler("ec9d3c43144b10b5730b7f6309c5d89b")

@app.route("/callback",methods=["POST"])
def callback():
    signature= request.headers['X-Line-Signature']

    body=request.get_data(as_text=True)
    app.logger.info("Request body: "+body)


    try:
        handler.handle(body,signature)
    except InvalidSignatureError:
        abort(400)

    return "OK"

# 處理訊息
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    message = TextMessage(text=event.message.text)
    line_bot_api.reply_message(event.reply_token ,message)
    
if __name__ =="__main__":
    app.run()
import os

from linebot import LineBotApi, WebhookParser
from linebot.models import MessageEvent, TextMessage, TextSendMessage
from linebot.models import *

channel_access_token = os.getenv("LINE_CHANNEL_ACCESS_TOKEN", None)


def send_text_message(reply_token, text):
    line_bot_api = LineBotApi(channel_access_token)
    message = TextSendMessage(text=text)
    line_bot_api.reply_message(reply_token, message)



def send_image_url(reply_token,img_url):
    line_bot_api = LineBotApi(channel_access_token)  

    message = ImageSendMessage(original_content_url=img_url, preview_image_url=img_url)

    line_bot_api.reply_message(reply_token,message)



def confirm_message(id,text,btn):
    line_bot_api = LineBotApi(channel_access_token) 
    
    message = TemplateSendMessage(
    alt_text='Confirm template',
    template=ConfirmTemplate(
        text='Are you sure?',
        actions=[
            PostbackTemplateAction(
                label='postback',
                text='postback text',
                data='action=buy&itemid=1'
            ),
            MessageTemplateAction(
                label='message',
                text='message text') ]   ) )


    line_bot_api.reply_message(reply_token, message)
 

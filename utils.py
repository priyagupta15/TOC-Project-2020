import os

from linebot import LineBotApi, WebhookParser
from linebot.models import MessageEvent, TextMessage, TextSendMessage
from linebot.models import *

channel_access_token = os.getenv("LINE_CHANNEL_ACCESS_TOKEN", None)


def send_text_message(reply_token, text):
    line_bot_api = LineBotApi(channel_access_token)
    message = TextSendMessage(text=text)
    line_bot_api.reply_message(reply_token, message)



def push_message(reply_token, text):
    line_bot_api = LineBotApi(channel_access_token)
    message = TextSendMessage(text=text)
    line_bot_api.push_message("U60b1a8f3b7c86bf15a8422a5d280b43a", message)






def send_image_url(reply_token,img_url):
    line_bot_api = LineBotApi(channel_access_token)  
    message = ImageSendMessage(original_content_url=img_url, preview_image_url=img_url)
    line_bot_api.push_message("U60b1a8f3b7c86bf15a8422a5d280b43a", message)




def location(reply_token,title,address,latitude,longitude):
    line_bot_api = LineBotApi(channel_access_token)  
    message = LocationSendMessage(
        title = title,
        address=address,
        latitude=latitude,
        longitude=longitude
    )
    line_bot_api.push_message("U60b1a8f3b7c86bf15a8422a5d280b43a", message)




def ask_question(reply_token):
    line_bot_api = LineBotApi(channel_access_token) 
    message = TemplateSendMessage(
        alt_text='Confirm template',
        template=ConfirmTemplate(
            text='When do you want to visit India?',
            actions=[
                PostbackTemplateAction(
                    label='WINTER',
                    text='winter',
                    data='action=buy&itemid=1'
                ),
                MessageTemplateAction(
                    label='SUMMER',
                    text='summer'
                )
            ]
        )
    )
    line_bot_api.reply_message(reply_token, message)



def ask_food_question(reply_token):
    line_bot_api = LineBotApi(channel_access_token) 
    message = TemplateSendMessage(
        alt_text='Confirm template',
        template=ConfirmTemplate(
            text='what kind of food do you like?',
            actions=[
                PostbackTemplateAction(
                    label='SWEET',
                    text='i like sweeeet',
                    data='action=buy&itemid=1'
                ),
                MessageTemplateAction(
                    label='SPICY',
                    text='i like spicy'
                )
            ]
        )
    )
    line_bot_api.push_message("U60b1a8f3b7c86bf15a8422a5d280b43a", message)





#taj mahal
def picture_option2(reply_token):
    line_bot_api = LineBotApi(channel_access_token) 
    message = ImagemapSendMessage(
        base_url='https://i.imgur.com/d3Sq7M1.jpg',
        alt_text='this is an imagemap',
        base_size=BaseSize(height=400, width=400),
        actions=[
            URIImagemapAction(
                link_uri='https://i.imgur.com/d3Sq7M1.jpg',
                area=ImagemapArea(
                    x=0, y=0, width=400, height=400
                )
            ),
            MessageImagemapAction(
                text='WOW',
                area=ImagemapArea(
                     x=520, y=0, width=400, height=400
                )
            )
        ]
    )
    line_bot_api.push_message(reply_token, message)





#ladakh
def picture_option1(reply_token):
    line_bot_api = LineBotApi(channel_access_token) 
    message = ImagemapSendMessage(
        base_url='https://i.imgur.com/omgsh8y.jpg',
        alt_text='this is an imagemap',
        base_size=BaseSize(height=400, width=400),
        actions=[
            URIImagemapAction(
                link_uri='https://i.imgur.com/omgsh8y.jpg',
                area=ImagemapArea(
                    x=0, y=0, width=400, height=400
                )
            ),
            MessageImagemapAction(
                text='WOW',
                area=ImagemapArea(
                     x=520, y=0, width=400, height=400
                )
            )
        ]
    )
    line_bot_api.reply_message(reply_token, message)



#many images
def ImageCarousel(reply_token):
    line_bot_api = LineBotApi(channel_access_token) 
    message = TemplateSendMessage(
        alt_text='ImageCarousel template',
        template=ImageCarouselTemplate(
            columns=[
                #ladakh
                ImageCarouselColumn(
                    image_url='https://i.imgur.com/omgsh8y.jpg',
                    action=PostbackTemplateAction(
                        label='Ladakh',
                        text='i like Ladakh',
                        data='action=buy&itemid=1'
                    )
                ),
                #taj mahal
                ImageCarouselColumn(
                    image_url='https://i.imgur.com/d3Sq7M1.jpg',
                    action=PostbackTemplateAction(
                        label='Taj Mahal',
                        text='i like Taj Mahal',
                        data='action=buy&itemid=2'
                    )
                ),  
                #varanasi            
                ImageCarouselColumn(
                    image_url='https://i.imgur.com/GeBbQ17.jpg',
                    action=PostbackTemplateAction(
                        label='Varanasi',
                        text='i like Varanasi',
                        data='action=buy&itemid=2'
                    )
                ),
                #kerela
                ImageCarouselColumn(
                    image_url='https://i.imgur.com/PxtVKPR.jpg',
                    action=PostbackTemplateAction(
                        label='Kerela',
                        text='i like Kerela',
                        data='action=buy&itemid=2'
                    )
                ),
                #udaipur
                ImageCarouselColumn(
                    image_url='https://i.imgur.com/wQ0D62G.jpg',
                    action=PostbackTemplateAction(
                        label='Udaipur',
                        text='i like Udaipur',
                        data='action=buy&itemid=2'
                    )
                )
            ]
        )   
    )
    line_bot_api.push_message(reply_token, message)





#sticker
def send_sticker(reply_token,package_id,sticker_id):
    line_bot_api = LineBotApi(channel_access_token) 
    message = StickerSendMessage(
        package_id=package_id,
        sticker_id=sticker_id
    )
    line_bot_api.push_message(reply_token, message)
    

def send_button(reply_token):
    line_bot_api = LineBotApi(channel_access_token) 
    message = TemplateSendMessage(
        alt_text='Buttons template',
        template=ButtonsTemplate(
            thumbnail_image_url='https://i.imgur.com/1I1HmDP.jpg',
            title='Menu',
            text='Please select',
            actions=[
                PostbackTemplateAction(
                    label='postback',
                    text='postback text',
                    data='action=buy&itemid=1'
                ),
                MessageTemplateAction(
                    label='message',
                    text='message text'
                ),
                URITemplateAction(
                    label='uri',
                    uri='https://i.imgur.com/1I1HmDP.jpg/'
                )
            ]
        )
    )
    line_bot_api.push_message(reply_token, message)


    

    

 

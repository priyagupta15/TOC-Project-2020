from transitions.extensions import GraphMachine
from utils import *


class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(model=self, **machine_configs)

#user = country = food,weather,places

    #introduction
    def is_going_to_intro(self, event):
        text = event.message.text
        return text.lower() == "hi" 

    #COUNTRY*****************************
    def is_going_to_country(self, event):
        text = event.message.text
        return text.lower() == "where can i visit?"


    #FOOD*****************************
    def is_going_to_food(self, event):
        text = event.message.text
        return text.lower() == "best food?"

    def is_going_to_spicy(self, event):
        text = event.message.text
        return text.lower() == "i like spicy"


    def is_going_to_sweet(self, event):
        text = event.message.text
        return text.lower() == "i like sweeeet"




    #WEATHER*****************************
    def is_going_to_weather(self, event):
        text = event.message.text
        return text.lower() == "weather?"

    def is_going_to_summer(self, event):
        text = event.message.text
        return text.lower() == "summer"

    def is_going_to_winter(self, event):
        text = event.message.text
        return text.lower() == "winter"


    #PLACES*****************************
    def is_going_to_places(self, event):
        text = event.message.text
        return text.lower() == "best place?"

    #LOCATION*****************************
    def is_going_to_location(self, event):
        text = event.message.text
        return text.lower() == "where is that?"



   #******INTRO*****************************
    def on_enter_intro(self, event):
        print("I'm entering intro")
        reply_token = event.reply_token
        user_id = event.source.user_id
        push_message(user_id,"Hi There!")
        send_sticker(user_id,'11537','52002738')
        self.go_back()



   #******COUNTRY*****************************
    def on_enter_country(self, event):
        print("I'm entering country")
        reply_token = event.reply_token
        user_id = event.source.user_id
        push_message(user_id,"India, 怎麼樣？")
        send_sticker(user_id,'11537','52002735')
        #send_text_message(reply_token, "India")



    #******FOOD*****************************
    def on_enter_food(self, event):
        reply_token = event.reply_token
        user_id = event.source.user_id
        #quickReply(user_id)
        #ImageCarousel(reply_token)
        ask_food_question(user_id)
        #ImageCarousel(user_id)
        #send_image_url(user_id,"https://i.imgur.com/yQcSle5.jpg")
        #self.go_back()
   

    def on_enter_spicy(self, event):
        reply_token = event.reply_token
        user_id = event.source.user_id
        push_message(user_id,"AWESOME, you will like this!")
        send_image_url(user_id,"https://i.imgur.com/uQq4kGw.jpg")
        self.go_back()

  

    def on_enter_sweet(self, event):
        print("I'm entering FOOD")
        reply_token = event.reply_token
        user_id = event.source.user_id
        push_message(user_id,"AWESOME, you will like this!")
        send_image_url(user_id,"https://i.imgur.com/CnGNY5o.jpg")
        self.go_back()





    #****** WEATHER *****************************
    def on_enter_weather(self, event):
        print("I'm entering weather")
        reply_token = event.reply_token
        user_id = event.source.user_id
        ask_question(reply_token)
        #self.go_back()

    def on_enter_summer(self, event):
        print("I'm entering summer")
        reply_token = event.reply_token
        user_id = event.source.user_id
        push_message(user_id,"AWESOME, Places recommende are : ")
        location(user_id,"Location","LADAKH","34.2996", "78.2932") #ladakh
        location(user_id,"Location","SIKKIM","27.5330","88.5122") #sikkim
        location(user_id,"Location","JAIPUR","26.9124", "75.7873") #jaipur
        push_message(user_id,"Other Attractions: ")
        ImageCarousel(user_id)
        self.go_back()

    def on_enter_winter(self, event):
        print("I'm entering winter")
        reply_token = event.reply_token
        user_id = event.source.user_id
        push_message(user_id,"AWESOME, Places recommende are : ")
        location(user_id,"Location","NEW DELHI", "28.6139", "77.2090") #new delhi
        location(user_id,"Location","SIKKIM","27.5330","88.5122") #sikkim
        location(user_id,"Location","JAIPUR","26.9124", "75.7873") #jaipur
        push_message(user_id,"Other Attractions: ")
        ImageCarousel(user_id)
        self.go_back()







    #****** PLACES *****************************
    def on_enter_places(self, event):
        print("I'm entering places")
        reply_token = event.reply_token
        user_id = event.source.user_id
        ImageCarousel(user_id)
        self.go_back()

    def on_exit_places(self):
        print("Leaving PLACES")

    



    
    #****** LOCATION *****************************
    def on_enter_location(self, event):
        print("I'm entering location")
        reply_token = event.reply_token
        user_id = event.source.user_id 
        #push_message(user_id,"here")
        #send_button(user_id)
        location(user_id,"Location","INDIA","20.5937","78.9629") #,"INDIA","20.5937","78.9629"
        #send_image_url(user_id,"https://i.imgur.com/eU6Z8yY.jpg")
        self.go_back()

    def on_exit_location(self):
        print("Leaving location")
         



        

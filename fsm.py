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
        push_message("U60b1a8f3b7c86bf15a8422a5d280b43a","Hi There!")
        send_sticker("U60b1a8f3b7c86bf15a8422a5d280b43a",'11537','52002738')
        self.go_back()



   #******COUNTRY*****************************
    def on_enter_country(self, event):
        print("I'm entering country")
        reply_token = event.reply_token
        push_message("U60b1a8f3b7c86bf15a8422a5d280b43a","India, 怎麼樣？")
        send_sticker("U60b1a8f3b7c86bf15a8422a5d280b43a",'11537','52002735')
        #send_text_message(reply_token, "India")



    #******FOOD*****************************
    def on_enter_food(self, event):
        reply_token = event.reply_token
        #quickReply("U60b1a8f3b7c86bf15a8422a5d280b43a")
        #ImageCarousel(reply_token)
        ask_food_question("U60b1a8f3b7c86bf15a8422a5d280b43a")
        #ImageCarousel("U60b1a8f3b7c86bf15a8422a5d280b43a")
        #send_image_url("U60b1a8f3b7c86bf15a8422a5d280b43a","https://i.imgur.com/yQcSle5.jpg")
        #self.go_back()
   

    def on_enter_spicy(self, event):
        reply_token = event.reply_token
        push_message("U60b1a8f3b7c86bf15a8422a5d280b43a","AWESOME, you will like this!")
        send_image_url("U60b1a8f3b7c86bf15a8422a5d280b43a","https://i.imgur.com/uQq4kGw.jpg")
        self.go_back()

  

    def on_enter_sweet(self, event):
        print("I'm entering FOOD")
        reply_token = event.reply_token
        push_message("U60b1a8f3b7c86bf15a8422a5d280b43a","AWESOME, you will like this!")
        send_image_url("U60b1a8f3b7c86bf15a8422a5d280b43a","https://i.imgur.com/CnGNY5o.jpg")
        self.go_back()





    #****** WEATHER *****************************
    def on_enter_weather(self, event):
        print("I'm entering weather")
        reply_token = event.reply_token
        ask_question(reply_token)
        #self.go_back()

    def on_enter_summer(self, event):
        print("I'm entering summer")
        reply_token = event.reply_token
        push_message("U60b1a8f3b7c86bf15a8422a5d280b43a","AWESOME, Places recommende are : ")
        location("U60b1a8f3b7c86bf15a8422a5d280b43a","Location","LADAKH","34.2996", "78.2932") #ladakh
        location("U60b1a8f3b7c86bf15a8422a5d280b43a","Location","SIKKIM","27.5330","88.5122") #sikkim
        location("U60b1a8f3b7c86bf15a8422a5d280b43a","Location","JAIPUR","26.9124", "75.7873") #jaipur
        push_message("U60b1a8f3b7c86bf15a8422a5d280b43a","Other Attractions: ")
        ImageCarousel("U60b1a8f3b7c86bf15a8422a5d280b43a")
        self.go_back()

    def on_enter_winter(self, event):
        print("I'm entering winter")
        reply_token = event.reply_token
        push_message("U60b1a8f3b7c86bf15a8422a5d280b43a","AWESOME, Places recommende are : ")
        location("U60b1a8f3b7c86bf15a8422a5d280b43a","Location","NEW DELHI", "28.6139", "77.2090") #new delhi
        location("U60b1a8f3b7c86bf15a8422a5d280b43a","Location","SIKKIM","27.5330","88.5122") #sikkim
        location("U60b1a8f3b7c86bf15a8422a5d280b43a","Location","JAIPUR","26.9124", "75.7873") #jaipur
        push_message("U60b1a8f3b7c86bf15a8422a5d280b43a","Other Attractions: ")
        ImageCarousel("U60b1a8f3b7c86bf15a8422a5d280b43a")
        self.go_back()







    #****** PLACES *****************************
    def on_enter_places(self, event):
        print("I'm entering places")
        reply_token = event.reply_token
        ImageCarousel("U60b1a8f3b7c86bf15a8422a5d280b43a")
        self.go_back()

    def on_exit_places(self):
        print("Leaving PLACES")

    



    
    #****** LOCATION *****************************
    def on_enter_location(self, event):
        print("I'm entering location")
        reply_token = event.reply_token 
        #push_message("U60b1a8f3b7c86bf15a8422a5d280b43a","here")
        #send_button("U60b1a8f3b7c86bf15a8422a5d280b43a")
        location("U60b1a8f3b7c86bf15a8422a5d280b43a","Location","INDIA","20.5937","78.9629") #,"INDIA","20.5937","78.9629"
        #send_image_url("U60b1a8f3b7c86bf15a8422a5d280b43a","https://i.imgur.com/eU6Z8yY.jpg")
        self.go_back()

    def on_exit_location(self):
        print("Leaving location")
         



        

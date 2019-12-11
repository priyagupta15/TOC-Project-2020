import os
import sys

from flask import Flask, jsonify, request, abort, send_file
from dotenv import load_dotenv
from linebot import LineBotApi, WebhookParser
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage
from fsm import TocMachine
from utils import send_text_message
load_dotenv()


machine = TocMachine(
    states=[
            "user",
            "intro",
            "country",
            "food" ,
            "spicy",
            "sweet",
            "weather",
            "places",
            "location",
            "summer",
            "winter"
            ],



    transitions=[

        { "trigger": "advance", "source": "user",       "dest": "country",   "conditions": "is_going_to_country",  },
        { "trigger": "advance", "source": ["user","country"],       "dest": "intro",     "conditions": "is_going_to_intro",  },

        { "trigger": "advance", "source": "country",    "dest": "food",      "conditions": "is_going_to_food",     },
        { "trigger": "advance", "source": "food",       "dest": "spicy",     "conditions": "is_going_to_spicy",    },
        { "trigger": "advance", "source": "food",       "dest": "sweet",     "conditions": "is_going_to_sweet",    },


        { "trigger": "advance", "source": "country",    "dest": "weather",    "conditions": "is_going_to_weather",  },
        { "trigger": "advance", "source": "weather",    "dest": "summer",     "conditions":  "is_going_to_summer",  },
        { "trigger": "advance", "source": "weather",    "dest": "winter",     "conditions":  "is_going_to_winter",  },


        { "trigger": "advance", "source": "country",    "dest": "places",     "conditions": "is_going_to_places",     },

        { "trigger": "advance", "source": "country",    "dest": "location",   "conditions": "is_going_to_location",   },
        
        #okay state
        #{ "trigger": "advance", "source": ["weather","spicy","sweet"],    "dest": "country",    "conditions": "is_going_to_okay",  },






        {
            "trigger":  "go_back", 
            "source":   ["user", "country", "intro"],
            "dest":      "user" 
        },


        {
            "trigger":  "go_back", 
            "source":   ["food", "weather", "places", "location", "spicy", "sweet", "summer","winter"], #, "winter" 
            "dest":      "country" 
        },

        #{"trigger": "go_back", "source": "state2", "dest": "state1"},



    ],
    initial="user",
    auto_transitions=False,
    show_conditions=True,
)

app = Flask(__name__, static_url_path="")


# get channel_secret and channel_access_token from your environment variable
channel_secret = os.getenv("LINE_CHANNEL_SECRET", None)
channel_access_token = os.getenv("LINE_CHANNEL_ACCESS_TOKEN", None)
if channel_secret is None:
    print("Specify LINE_CHANNEL_SECRET as environment variable.")
    sys.exit(1)
if channel_access_token is None:
    print("Specify LINE_CHANNEL_ACCESS_TOKEN as environment variable.")
    sys.exit(1)

line_bot_api = LineBotApi(channel_access_token)
parser = WebhookParser(channel_secret)


@app.route("/callback", methods=["POST"])
def callback():
    signature = request.headers["X-Line-Signature"]
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # parse webhook body
    try:
        events = parser.parse(body, signature)
    except InvalidSignatureError:
        abort(400)

    # if event is MessageEvent and message is TextMessage, then echo text
    for event in events:
        if not isinstance(event, MessageEvent):
            continue
        if not isinstance(event.message, TextMessage):
            continue
        if not isinstance(event.message.text, str):
            continue
        print(f"\nFSM STATE: {machine.state}")
        print(f"REQUEST BODY: \n{body}")
        response = machine.advance(event)
        if response == False:
            send_text_message(event.reply_token, "Okay!")
    return "OK"


@app.route("/webhook", methods=["POST"])
def webhook_handler():
    signature = request.headers["X-Line-Signature"]
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info(f"Request body: {body}")

    # parse webhook body
    try:
        events = parser.parse(body, signature)
    except InvalidSignatureError:
        abort(400)

    # if event is MessageEvent and message is TextMessage, then echo text
    for event in events:
        if not isinstance(event, MessageEvent):
            continue
        if not isinstance(event.message, TextMessage):
            continue
        if not isinstance(event.message.text, str):
            continue
        print(f"\nFSM STATE: {machine.state}")
        print(f"REQUEST BODY: \n{body}")
        response = machine.advance(event)
        if response == False:
            send_text_message(event.reply_token, "Okay!")
    return "OK"


@app.route("/show-fsm", methods=["GET"])
def show_fsm():
    machine.get_graph().draw("fsm.png", prog="dot", format="png")
    return send_file("fsm.png", mimetype="image/png")


if __name__ == "__main__":
    port = os.environ.get("PORT", 8000)
    app.run(host="0.0.0.0", port=port, debug=True)

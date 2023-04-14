from flask import Flask, render_template, request, jsonify
#from flask_cors import CORS
from chat import get_response, get_id

import os, sys


from pymessenger import Bot

PAGE_ACCESS_TOKEN = "EAAKXHQesWLIBACqgp3yEKyeqEsASAZC4t9thiuNgffcVaJ0s3Fdn3MyIvoUPDjZCCcy2QqNDZCKAZACOOTIYlsjvf3AWtUGyDtyz4RnnT5sZCR7FYtZBEJ5H3bibZAuN6l3MHvvdH5b2RNDZC6FZCVuIznOr7VVZA8vLdJHRZACVB8gXyiYsEDjWYZBH8U7JVk0cTDBNouuriWilxwZDZD"

app = Flask(__name__)
#CORS(app)
bot = Bot(PAGE_ACCESS_TOKEN)


@app.route('/', methods=['GET'])
def verify():
    # Webhook verification
    if request.args.get("hub.mode") == "subscribe" and request.args.get("hub.challenge"):
        if not request.args.get("hub.verify_token") == "hello":
            return "Verification token mismatch", 403
        return request.args["hub.challenge"], 200
    return "Hello world", 200


@app.route('/', methods=['POST'])
def webhook():
    data = request.get_json()
    #text = data['entry'][0]['messaging'][0]['message']['text']
    log(data)  # you may not want to log every incoming message in production, but it's good for testing
    #log(text)
    #response = get_response(text)
    #message = response
    #log(message)
    
    
    if data['object'] == 'page':
        for entry in data['entry']:
            for messaging_event in entry['messaging']:
                if messaging_event.get('message'):
                    sender_id = messaging_event['sender']['id']
                    recipient_id = messaging_event['recipient']['id']
                    message_text = messaging_event['message']['text']
                    response = get_response(message_text)
                    testID = get_id(message_text)
                    #send_message(sender_id, message)
                    bot.send_text_message(sender_id, response)
    
    #m_response = jsonify(message)
    #log(m_response['answer'])
    #return jsonify(message)
    return "ok", 200

def log(message):  # simple wrapper for logging to stdout on heroku
    print(message)
    sys.stdout.flush()


if __name__ == "__main__":
    app.run(debug=True, port=8085)
import sys
from flask import Flask, request, jsonify
from datetime import datetime
import time, json
import hashlib, os, base64, glob
from slackeventsapi import SlackEventAdapter
from slack_sdk.web import WebClient
import openai
import requests
app = Flask(__name__)

# Our app's Slack Event Adapter for receiving actions via the Events API
#slack_signing_secret = os.environ["SLACK_SIGNING_SECRET"]
#slack_events_adapter = SlackEventAdapter(slack_signing_secret, "/slack/events", app)

# Create a SlackClient for your bot to use for Web API requests
slack_bot_token = os.environ["SLACK_BOT_TOKEN"]
print(slack_bot_token)
#slack_client = WebClient(slack_bot_token)

openai.api_key = os.environ["OPENAI_KEY"]

def ask_gpt(prompt):
    response = openai.Completion.create(
        engine="text-davinci-003",  # ChatGPT model
        prompt=prompt,
        max_tokens=200,  # Adjust the response length
        n=1,
        stop=None,
        temperature=0.7,  # Adjust creativity (lower value = more focused, higher value = more random)
        top_p=1,
    )

    return response.choices[0].text.strip()

def post_slack(channel_id, message, slack_token):
    data = {
            'Content-Type': 'application/x-www-form-urlencoded',
            'token': slack_token,
            'channel': channel_id,
            'text': message
           }
    URL = "https://slack.com/api/chat.postMessage"
    print(data)
    res = requests.post(URL, data=data)
    print(res.text)


@app.route('/slack/events', methods=['POST'])
def handle_slack_events():
    global slack_bot_token
    print(slack_bot_token)
    # Load the request data as JSON
    request_data = json.loads(request.data)

    print(request_data, file=sys.stderr)

    # Check if the event is a challenge event
    if 'challenge' in request_data:
        return jsonify({'challenge': request_data['challenge']})
    elif 'event' in request_data:
        event_data = request_data['event']
        # Check if the event is a message event
        if 'type' in event_data and event_data['type'] == 'app_mention':
            # Extract the message text
            message_text = event_data['text']
            if message_text.startswith('<'):
                message_text = message_text.split(' ')[1]
            print("Message received:", message_text)

            # Extract the channel ID
            channel_id = event_data['channel']
            print("Channel ID:", channel_id)

            answer = ask_gpt(message_text + '. 짧고 간결히 반말로 답해줘.')
            print(answer)
            post_slack(channel_id, answer, slack_bot_token)
            return '', 200
        else:
            return '', 200
    else:
        return '', 200

app.run(host='0.0.0.0', port=3000)


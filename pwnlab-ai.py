import sys
import openai
import json
import requests
import time

openai_key = sys.argv[1]
slack_key = sys.argv[2]

# Use the openai_secret_manager to get your API key
openai.api_key = openai_key
SLACK_EVENT_ENDPOINT = "https://slack.com/api/events.listen"
#channel_id = 'C050MENA4H4'  # general  member id: U054A375LAD

def ask_gpt(prompt):
    response = openai.Completion.create(
        engine="text-davinci-003",  # ChatGPT model        
        prompt=prompt,
        max_tokens=500,  # Adjust the response length
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
    res = requests.post(URL, data=data)
    print(res.text)

# Define the Slack bot's token
SLACK_BOT_TOKEN = slack_key
# Define the Slack event listener
SLACK_EVENT_ENDPOINT = "https://slack.com/api/events.listen"

def handle_question(event_data):
    # Extract the user's question from the event data
    question = event_data["text"]
    answer = ask_gpt(question + '. 짧고 간결히 반말로 답해줘.')

    # Send the answer back to the user via Slack
    channel = event_data["channel"]
    requests.get(SLACK_BOT_ENDPOINT % (channel, answer))
    post_slack(channel, answer, slack_key)

# Listen for events from Slack
while True:
    response = requests.post(SLACK_EVENT_ENDPOINT, json={"token": slack_key})
    event_data = json.loads(response.text)
    if "event" in event_data:
        event_type = event_data["event"]["type"]
        if event_type == "app_mention":
            handle_question(event_data["event"])

    time.sleep(1)


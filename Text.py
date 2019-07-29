# pip install nexmo

# sign up for a nexmo account
import nexmo
client = nexmo.Client(key='xxxxxx', secret='xxxxxx')

responseData = client.send_message(
    {
        'from': 'xxxxxx',
        'to': 'xxxxxx',
        'text': 'Hello from Nestwatch!',
    }
)

if responseData["messages"][0]["status"] == "0":
    print("Message sent successfully.")
else:
    print(f"Message failed with error: {responseData['messages'][0]['error-text']}")
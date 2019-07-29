# pip install nexmo

# sign up for a nexmo account
import nexmo
client = nexmo.Client(key='xxxxxxx', secret='xxxxxxxx')

client.send_message({
    'from': 'xxxxxxxxxx',
    'to': 'xxxxxxxxxx',
    'text': 'Hello from Nestwatch!',
})

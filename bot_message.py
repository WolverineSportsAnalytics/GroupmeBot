import requests

print "What would you like groupmeBot to say:"
msg = raw_input()

post_params = { 'bot_id' : '237b9e69c4b105b1637e40f28d', 'text': msg }
requests.post('https://api.groupme.com/v3/bots/post', params = post_params)

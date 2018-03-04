import requests
import argparse
import random
import json
 
def main():
    ''' main '''
    parser = argparse.ArgumentParser()
    parser.add_argument('message', nargs='+', help='message to put on meme')
    args = parser.parse_args()
    message = ' '.join(''.join(random.choice([c.upper, c.lower])() for c in word) for word in args.message)[:200]
    memeage = generate_meme(message)
    send_to_discord(memeage)
 
def generate_meme(message):
    url = 'https://api.imgflip.com/caption_image'
    datastr = {
        'template_id': '102156234', # Meme Template ID
        'username': '', # imgflip Username
        'password': '', # imgflip Password
        'boxes[0]': '',
        'boxes[1][text]': message,
        'boxes[2][x]': 10,
        'boxes[3][y]': 1,
        'boxes[4][width]': 100,
        'boxes[5][height]': 30,
    }
    headers = { 'User-Agent' : 'Mozilla/5.0' }
    resp = requests.post(url, data=datastr, headers=headers)
    return json.loads(resp.text)['data']['url']

def send_to_discord(message):
    url = 'https://discordapp.com/api/webhooks/' # Discord Webhook
    datastr = {'content': f'{message}'}
    headers = {'content-type': 'application/json'}
    req = requests.post(url, json.dumps(datastr), headers=headers)

    if req.status_code != 204:
        print(f'\nReceived {req.status_code} from Discord. Whoops\n')
    else: print('Meme sent to discord')


if __name__ == '__main__':
    main()

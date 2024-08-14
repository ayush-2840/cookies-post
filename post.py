import requests
import os
import re
import time
import random
from requests.exceptions import RequestException

def clear_screen():
    os.system('clear')


def set_cookie():
    Cookie = input('\x1b[1;36m[+] ENTER YOUR COOKIE :: \x1b[1;92m ')
    return Cookie


def get_commenter_name():
    return input('\x1b[1;93m[+] ENTER YOUR HATER NAME :: \x1b[1;91m')


def get_password():
    return input('\x1b[92mEnter Password :: ')


def make_request(url, headers, cookies):
    response = requests.get(url, headers = headers, cookies = cookies).text
    return response
    if RequestException:
        e = None
        print('\x1b[91m[!] Error making request:', e)
        e = None
        del e
        return None
    e = None
    del e

clear_screen()
logo = '\n🔥                          \x1b[1;36m𓆰𓃮𓆪                         🔥            \n\x1b[1;36m@@@  @@@   @@@@@@    @@@@@@    @@@@@@    @@@@@@   @@@  @@@  \x1b[1;91m 𝐑\n\x1b[1;36m@@@  @@@  @@@@@@@@  @@@@@@@   @@@@@@@   @@@@@@@@  @@@@ @@@  \n@@!  @@@  @@!  @@@  !@@       !@@       @@!  @@@  @@!@!@@@  \x1b[1;92m A\n\x1b[1;36m!@!  @!@  !@!  @!@  !@!       !@!       !@!  @!@  !@!!@!@!  \n\x1b[1;36m@!@!@!@!  @!@!@!@!  !!@@!!    !!@@!!    @!@!@!@!  @!@ !!@!  \x1b[1;93m 𝐉\n\x1b[1;36m!!!@!!!!  !!!@!!!!   !!@!!!    !!@!!!   !!!@!!!!  !@!  !!!  \n\x1b[1;36m!!:  !!!  !!:  !!!       !:!       !:!  !!:  !!!  !!:  !!!  \x1b[1;94m 𝐏\n\x1b[1;36m:!:  !:!  :!:  !:!      !:!       !:!   :!:  !:!  :!:  !:!  \n\x1b[1;36m::   :::  ::   :::  :::: ::   :::: ::   ::   :::   ::   ::  \x1b[1;95m 𝐔\n\x1b[1;36m :   : :   :   : :  :: : :    :: : :     :   : :  ::    :                                                                 \x1b[1;96m 𝐓\n\x1b[38;5;208m==============================================================\n\x1b[1;37m[*] OWNER      : \x1b[1;36mHASSAN\n\x1b[1;37m[*] GITHUB     : \x1b[1;36mHASSAN-RAJPUT0\n\x1b[1;37m[*] STATUS     : \x1b[1;91mPERMIUM\n\x1b[1;37m[*] TEAM       : ONE MAN ARMY\n\x1b[1;37m[*] TOOL       : POST COOKIE TOOL\n\x1b[38;5;208m==============================================================\n'
print(logo)
print('\x1b[92m╰◈▪➣ Start Time:', time.strftime('%Y-%m-%d %H:%M:%S\n'))
password = 'H4554N_XD'
user_pass = get_password()
if user_pass == password:
    print('\n\x1b[92mLogin Successful!\n')
print('\n\x1b[91mIncorrect Password! Try again.\n')
os.system('clear')
print(logo)
cookies = set_cookie()
response = make_request('https://business.facebook.com/business_locations', headers = {
    'Cookie': cookies,
    'User-Agent': 'Mozilla/5.0 (Linux; Android 11; RMX2144 Build/RKQ1.201217.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/103.0.5060.71 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/375.1.0.28.111;]' }, cookies = {
    'Cookie': cookies })
return None
token_eaag = re.search('(EAAG\\w+)', str(response)).group(1)
print('\x1b[38;5;208m==============================================================')
id_post = int(input('\x1b[1;95m[+] ENTER POST UID :: \x1b[1;94m'))
commenter_name = get_commenter_name()
delay = int(input('\x1b[38;5;208m[+] ENTER DELAY IN SEC :: \x1b[1;32;1m'))
comment_file_path = input('\x1b[34m[+] ENTER COMMENT FILE PATH :: \x1b[1;93m')
print('\x1b[38;5;208m==============================================================')
print('╰◈▪➣ YOUR POST SERVER ACTIVED :-')
file = open(comment_file_path, 'r')
comments = file.readlines()
None(None, None)
if not response:
    pass
(x, y) = (0, 0)
print()
time.sleep(delay)
teks = comments[x].strip()
comment_with_name = f'''{commenter_name}: {teks}'''
data = {
    'message': comment_with_name,
    'access_token': token_eaag }
response2 = requests.post(f'''https://graph.facebook.com/{id_post}/comments/''', data = data, cookies = {
    'Cookie': cookies }).json()
if "'id':" in str(response2):
    print('\x1b[92mYOUR POST ID --➣', id_post)
    print('\x1b[92mDATE & TIME --➣', time.strftime('%Y-%m-%d %H:%M:%S'))
    print('\x1b[92mYOUR COMMENT SUCESSFULLY SENT ➣', comment_with_name)
    print('\n')
    print('\x1b[38;5;208m       ✪✭════════•『 𝐂𝐎𝐍𝐕𝐎 𝐒𝐄𝐑𝐕𝐄𝐑 𝐁𝐘 𝐇𝐀𝐒𝐒𝐀𝐍 』•════════✭✪')
    x = (x + 1) % len(comments)
y += 1
print('\x1b[91m[{}] Status : Failure'.format(y))
print('\x1b[91m[/]Link : https://m.basic.facebook.com//{}'.format(id_post))
print('\x1b[91m[/]Comments : {}\n'.format(comment_with_name))
if RequestException:
    e = None
    print('\x1b[91m[!] Error making request:', e)
    time.sleep(5.5)
    e = None
    del e
    e = None
    del e
if Exception:
    e = None
    print('\x1b[91m[!] An unexpected error occurred:', e)
    e = None
    del e
    return None
e = None
del e
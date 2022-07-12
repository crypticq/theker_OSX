#!/usr/bin/python3
import subprocess
import requests
import time
import random
import os





class Thekar:
    CMD = '''
    on run argv
      display notification (item 2 of argv) with title (item 1 of argv)
    end run
    '''
    
    def holy_quran(self):
        return {'Ayah':requests.get(f'https://api.alquran.cloud/v1/ayah/{random.randint(1,6236)}').json()['data']['text'] , 'Surah':requests.get(f'https://api.alquran.cloud/v1/ayah/{random.randint(1,6236)}').json()['data']['surah']['name']}
        
    
    
    def notify(self):
        subprocess.call(['osascript', '-e', self.CMD, self.holy_quran()['Surah'], self.holy_quran()['Ayah']])
        os.system('say "Allahu Akbar"')
        


test = Thekar()
while True:
    time.sleep(60 * 5)
    test.notify()


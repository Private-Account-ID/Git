import webbrowser
from time import strftime
from pyttsx3 import init
from speech_recognition import Microphone, Recognizer
from wikipedia import set_lang, summary
from pyjokes import get_joke
from os import startfile, system
from googletrans import Translator 
from random import random
from phonenumbers import PhoneNumberMatcher, format_number, PhoneNumberFormat, parse, is_valid_number, geocoder, carrier, timezone
from playsound import playsound
from requests import get
from bs4 import BeautifulSoup
from random import randint

engine, r = init('sapi5'), Recognizer()
engine.setProperty('rate', 170)     # 0 to 200
engine.setProperty('volume',1.0)    # setting up volume level  between 0 and 1
engine.setProperty('voice', engine.getProperty('voices')[1].id)  # 0 for male 1 for female

def wishMe( H = int(strftime("%H")) ):    # Automatic Wishing function
    if H >= 1 and H <= 12: return 'Good Morning Sir'
    elif H > 12 and H < 21: return "Good Evening Sir"
    else: return 'Good Night Sir'


# Function to play audio files

def PlayAudio(txt):                    # Syntax: **** play music *****                    
    List = [] # path of all the songs        
    playsound(List[randint(1, len(List)+1)]) 

# Function to get information of any sim card number
# Note: please say country code also

def Phonenumbers(txt):  # Syntax: Get me the number of +91 XXXXXXXXXX
    for i in PhoneNumberMatcher(txt,None): n = format_number(i.number, PhoneNumberFormat.E164)
    n = parse(n)
    if is_valid_number(n) == False: return f"{n} is an invalid number."
    return f"Sir, phone number {n} is of country {geocoder.description_for_number(n,'en')} using carrier {carrier.name_for_number(n,'en')} in timezone {timezone.time_zones_for_number(n)}"


# Common replace function for whole program
def Replace(f,txt):                          
    for i in f: txt = txt.replace(i,'',1)
    return txt

# Function that needs replace()  should be below


# Function of Universal Translator
# Note You can change source and destiny languare as per you needs

def Trans(txt):  # syntax: ******* meaning of **** in ****
    txt = txt[txt.index('of')+3:]
    if txt.endswith('in hindi'): return f"The meaning of {txt} is {Translator().translate(txt[:txt.index('in hindi')-1], dest='hi').pronunciation}"
    else: return f"The meaning of {txt} is {Translator().translate(txt,src='hi', dest='en').text}"


# Function to shut down, log off or restart

def Os(txt): # Syntax: shut or log off or restart
    if 'shut' in txt: return 's'
    elif 'log of' in txt: return 'l'
    elif 'restart' in txt: return 'r'


# Function to search for google, picture, map, price, stock price, book or search any accound on twitter or instagram or open any website
# Note: Some urls only works with bing search engine

def Web(txt):  # Syntax: show me ****
    x, txt1 = txt, txt[txt.index('of')+3:]
    if "pic" in x: return f'https://www.bing.com/images/search?q={txt1}' # show me pic of *****
    elif 'map' in x: return f'https://www.bing.com/maps?q={txt1}' # show me map ******
    elif 'price' in x: return f'https://www.bing.com/shop?q={txt1}' # show me price # show me ****
    elif 'book' in x: return f'https://www.google.com/search?q={txt1}&tbm=bks' # show me book ******
    elif 'stock' in x: return f'https://www.google.com/finance/quote/{txt1}'   # show me stock *******
    elif 'twitter' in x: return f'https://www.twitter.com/{txt1.replace(" ", "")}' # show me twitter account of ******
    elif 'insta' in x: return f'https://www.instagram.com/{txt1.replace(" ", "")}' # show me insta account of ******
    elif 'website' in x: return f'www.{txt1}' # show me ****


# Function for Telling short news for wanted topic

def News():  # Syntax : tell me some {topic} news
    news = BeautifulSoup(get(f"https://inshorts.com/en/read/{txt.split()[-2].replace('some','')}").content,'html.parser').find_all(itemprop="headline")
    for i in news: Say(f"\n- {i.get_text()}.")


# Function to extracting information from wikipedia with languare option

def Wikipedia(txt,sen = 2): # Syntax: ****** in wikipedia
    if 'in hindi'in txt:set_lang("hi")                               # change 2nd language from here
    if 'in brief' in txt: sen = 8
    txt = txt[:txt.index(' in wikipedia')]
    Say('searching.....',txt)
    return summary(txt.replace(' ', ''), sentences=sen)

def Say(txt):
    print(f'Jarvis:{txt}')
    engine.say(txt)
    engine.runAndWait()
    engine.stop()


# Function to read and write files

def Open(txt):        
    if txt.startswith('read'):  # Syntax : read **** file
        with open(f"C:\\Users\\abc\Documents\\text\\{txt.split()[-1]}.txt") as f:
            Say(f"Reading.....\n{f.read()}")
            f.close()
    else:                       # Syntax : write *** file
        with open(f"C:\\Users\\abc\Documents\\text\\{txt.split()[2]}.txt",'a+') as f:
            f.write(f'{txt[10:]}\n')
            Say('Done Sir')
            f.close()

# Main Function

def takeCommand(): # Syntax: *** Jarvis *****
    Say('Yes sir')
    with Microphone() as source: 
        r.adjust_for_ambient_noise(source,duration=0.2)
        print('Jarvis: listening.....')
        audio = r.listen(source)
        print('Jarvis: Recognizing.....')
        txt = r.recognize_google(audio, language='en-in').lower()
        box = txt.split();print(f'You said{txt}')
        
        try:
            if 'tell me a joke' in txt: Say(get_joke())
            elif txt.startswith('search') : from pyKit import Search; Search(txt.replace("search", '', 1)) # Syntax: search ******
            elif txt.startswith('take') and txt.endswith("screenshot") : from Pyautogui import Shot; startfile(Shot()) # Syntax: take **** screenshot
            elif 'in wikipedia' in txt: Say(Wikipedia(txt))  
            elif txt.startswith('show me'): webbrowser.open(Web(txt))
            elif txt.endswith('news') and 'tell' in txt: News(txt)  # Syntax: tell ********* {topic or some} news
            elif txt.startswith('start') : from pyautogui import Start; Start(txt)
            elif txt.startswith("shut") or txt.startswith('log of') or txt.endswith('restart'): system(f'shutdown /{Os(txt)} /t 0')
            elif txt.startswith('play') and txt.endswith('youtube'): Play(txt[txt.index('play')+5:-10]) # Syntax: play **** on youtube
            elif txt.startswith('what'):
                if 'day' in txt or 'date' in txt: Say(strftime("%A, %d %B %Y"))
                elif 'txt' in txt: Say(strftime("%H:%M:%S"))
            elif txt.startswith('read pdf'): from PyPdf import Read; Read(txt) # Syntax: read pdf
            elif txt.startswith('write') and box[1] != 'file': from PyKit import HandWrite; startfile(HandWrite(txt)) # Syntax: handwrite *******
            elif box[1]=="file": Open(txt)
            elif 'mean' in txt and 'of' in txt: Say(Trans(txt))
            elif txt.startswith("say") or box[0]=="se": Say(Replace(('say', 'se'), txt))                            # try it to get get down only
            elif txt.startswith('get') and txt.endswith('number'): Say(Phonenumbers(txt))
            elif txt.startswith('convert') and txt.endswith('art'): from PyKit import ImgToArt; Open(ImgToArt()) # Syntax: convert **** art

            
# Function to control Arduino modules
# Note: Setup arduino for Ultrasonic sersor module and pyfirmata, Pymata4 lib  (You can search this for on youtube)

            elif txt.endswith('distance') and 'measure' in txt: import UltrasonicSensor
            elif 'turn' in txt and 'led' in txt: Say(Led(txt)); from pyfirmata import Led
            elif 'servo' in txt and txt.endswith('degree'): from pyfirmata import MoveServo; Say(MoveServo(txt.split()))
        except Exception as e: print(e)


# To enter in Main function Say Jarvis
if __name__ == '__main__':
    Say(wishMe())
    while 1:
        with Microphone() as source: 
            print('listening.....')
            audio   = r.listen(source)
            print('Recognizing.....')
            try: 
                if 'Veronica' in r.recognize_google(audio, language='en-in'): takeCommand()
            except Exception: pass
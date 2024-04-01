from selenium_web import infow
import pyttsx3 as p
import speech_recognition as sr
import randfacts
from Jokes import joke
from Weather import temp, des
import datetime
import time
from Youtube import YouTubeSearchAndPlay
from News import NewsFetcher

engine = p.init()
rate=engine.getProperty('rate')
engine.setProperty('rate',180)
voices=engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(text):
    engine.say(text)
    engine.runAndWait()

def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning")
        return "Sir/Maam"
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon")
        return "Sir/Maam"
    else:
        speak("Good Evening")
        return "Sir/Maam"

greeting = wishme()

today_date = datetime.datetime.now()

r = sr.Recognizer()

speak(f"{greeting}, I'm Juno, Your Voice Assistant.")
#speak("Today is " + today_date.strftime("%A") + ", " + today_date.strftime("%d") + " " + today_date.strftime("%B") + " " + today_date.strftime("%Y") + "And it's currently " + today_date.strftime("%I") + ":" + today_date.strftime("%M") + " " + today_date.strftime("%p") + ".")
#speak("The Temperature in Mumbai is " + str(temp()) + " degree celsius with " + des() + " weather")
#speak("How are you feeling today?")
with sr.Microphone() as source:
    r.energy_threshold=10000
    r.adjust_for_ambient_noise(source,1.2)
    print("Listening...")
    audio = r.listen(source)
    text = r.recognize_google(audio)
    print(text)
if "what" and "about" and "you" in text:
    speak("Im having a good day.")

speak("What can i do for you today")

with sr.Microphone() as source:
    r.energy_threshold=10000
    r.adjust_for_ambient_noise(source,1.2)
    print("Listening...")
    audio = r.listen(source)
    text2 = r.recognize_google(audio)
    
if "information" in text2:
    speak("Which topic would you like me to search for you?")
    
    with sr.Microphone() as source:
        r.energy_threshold=10000
        r.adjust_for_ambient_noise(source,1.2)
        print("Listening...")
        audio = r.listen(source)
        infor = r.recognize_google(audio)
    print("searching {} in wikipedia".format(infor))
    speak("searching {} in wikipedia".format(infor))
    
        
    assist = infow()
    assist.get_info(infor)

elif "joke" in text2 or "jokes" in text2:
    speak("Sure sir, Get Ready for Some Chuckles")
    arr=joke()
    print(arr[0])
    speak(arr[0])
    print(arr[1])
    speak(arr[1])

elif "fact" in text2 or "facts" in text2:
    speak("Sure sir,")
    x=randfacts.getFact()
    print(x)
    speak("Did you know that, "+x)

elif "play" and "video" in text2:
    speak("you want me to play which video??")
    with sr.Microphone() as source:
        r.energy_threshold=10000
        r.adjust_for_ambient_noise(source,1.2)
        print("Listening...")
        audio = r.listen(source)
        vid = r.recognize_google(audio)
    print("Playing {} on youtube".format(vid))
    speak("Playing {} on youtube".format(vid))

    assist = YouTubeSearchAndPlay()
    assist.play(vid)
    #time.sleep(60)

elif "news" in text2:
    print("Sure sir, Now i will show news for you.")
    speak("Sure sir, Now i will show news for you.")
    
    news_fetcher = NewsFetcher(api_key="d8b2236966eb4b9f846b51de364d93f4")
    articles = news_fetcher.fetch_news()

    for article in articles:
        news_title = article['title']
        news_description = article['description']
        news_source = article['source']['name']
        news_text = f"{news_title}. {news_description}. From {news_source}."
        print(news_text)
        speak(news_text)
        
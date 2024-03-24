import randfacts

elif "fact" or "facts" in text2:
    speak("Sure sir,")
    x=randfacts.getFact()
    print(x)
    speak("Did you know that, "+x)


from Jokes import everything

elif "joke" or "jokes" in text2:
    speak("Sure sir, Get Ready for Some Chuckles")
    arr=joke()
    print(arr[0])
    speak(arr[0])
    print(arr[1])
    speak(arr[1])

from Weather import everything

speak("Hello Sir," +wishme()+ " I'm Your Voice Assistant.")
speak("Today is " + today_date.strftime("%A") + ", " + today_date.strftime("%d") + " " + today_date.strftime("%B") + " " + today_date.strftime("%Y") + "And it's currently " + today_date.strftime("%I") + ":" + today_date.strftime("%M") + " " + today_date.strftime("%p") + ".")
speak("The Temperature in Mumbai is " + str(temp()) + " degree celsius with " + des() + " weather")
speak("What can I do for you today?")

import datetime

today_date = datetime.datetime.now()


def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon")
    else:
        speak("Good Evening")
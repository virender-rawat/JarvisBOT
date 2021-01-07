import pyttsx3 #import pyttsx3 for voice support
import datetime
import wikipedia
import speech_recognition as sr
import webbrowser
import os
import smtplib
import speedtest



engine= pyttsx3.init()


def speak (audio):
    engine.say(audio)
    engine.runAndWait()

def time():
    Time = datetime.datetime.now().strftime("%I:%M:%S")
    speak(Time)

def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    date = int(datetime.datetime.now().day)
    speak(year)
    speak(month)
    speak(date)

def wishme():
    speak("Welcome Back Sir!")
    speak("the Current Time is")
    time()
    speak("The Current Date is")
    date()
    hour = datetime.datetime.now().hour
    if hour >= 1  and hour<12:
        speak ("Good Morning Sir")
    elif hour >= 12 and hour <18:
        speak( "Good Afternoon Sir")
    elif hour >= 18 and hour <21:
        speak("Good Evening Sir")
    else:
        speak("its mid-Night sir")
    speak("Alexa at your service.. Please tell me how may i help you!!!!")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening......")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizning.....")
        query = r.recognize_google(audio, language= 'en-in')
        print(query)
    except Exception as e:
        print(e)
        speak("Say that again, please...")
        return "None"
    return  query

def send_Email(to, content):
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.login('call.rawat07@gmail.com', '********')
        server.sendmail('call.rawat07@gmail.com',to,content)
        server.close()

st = speedtest.Speedtest()
option  = int (input('''what speed do you want to measure:
1) Download Speed

2) Upload Speed

3) Ping

Your Choice'''))

if option==1:
    print(st.download()/(1024 * 1024),"Mbps")
elif option==2:
    print(st.upload()/(1024 * 1024),"Mbps")
elif option==3:
    servername=[]
    st.get_servers(servername)
    print(st.results.ping)
else:
    print("please enter corrction option")

if __name__ == '__main__':

    date()
    wishme()

    while True:

        query = takeCommand().lower()
        #logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('searching in wikipedia......')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("Youtube.com")
        elif 'open udemy' in query:
            webbrowser.open("Udemy.com")
        elif 'open google' in query :
            webbrowser.open("google.com")

        elif 'play music' in query:
            music_dir = 'D:\\Downloads\\songs'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir,songs[0]))

        elif 'Open code' in query:
            codePath = "C:\\Program Files\\JetBrains\\PyCharm Community Edition 2020.3\\bin\\pycharm64.exe"
            os.startfile(codePath)

        elif 'open excel' in query:
            codePath = "C:\\Program Files (x86)\\Microsoft Office\\Office16\\EXCEL.EXE"
            os.startfile(codePath)

        elif 'open google' in query:
            go = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
            os.startfile(go)

        elif 'email to Virender' in query:
            try:
                speak("what Should I Say?")
                content = takeCommand()
                to = "call.rawat07@gmail.com"
                send_Email(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("sorry sir, i am not able to send this email at this time")
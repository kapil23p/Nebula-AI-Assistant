import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import pywhatkit as kit
import smtplib
import pyautogui
import time

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
rate = 150
engine.setProperty('voice',voices[1].id)
engine.setProperty('rate',rate)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning sir, how can i help you")
    elif hour>=12 and hour<18:
        speak("Good Afternoon sir, how can i help you")
    else:
        speak("Good Evening sir, how can i help you")

def takecommand():
    r= sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio)
        print(f"User said: {query}\n")
    except Exception as e:
        print("Say that again please sir")
        return "None"
    return query

def sendEmail(to,content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('nebula616ai@gmail.com', 'nebula@616G')
    server.sendmail('nebula616ai@gmail.com', to, content)
    server.close()

if __name__ == '__main__':
    wishme()
    start = True
    while start:
        query = takecommand().lower()
        if 'tell about' in query:
            speak("Searching Wikipedia...")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
            start = False
            
        elif 'open youtube' in query:
            webbrowser.open("https://youtu.be/4xnsmyI5KMQ?feature=shared")
            start = False
            
        elif 'open' in query:
            l=list(map(str, query.split()))
            web=l[-1]
            webbrowser.open(f"https://www.{web}.com")
            start = False
            
        elif 'play spotify' in query:
            webbrowser.open("https://open.spotify.com/playlist/4RfCVZ3lLmaHueLCHrisr4?si=fe195bb355ae4d29")
            time.sleep(1)
            pyautogui.press('space')
            start = False
            
        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")
            
        elif 'email to me' in query:
            try:
                speak("What should i mail")
                content = takecommand()
                to = "pavankapil177@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent")
            except Exception as e:
                print(e)
                error=e
                speak(f"Failed to send because {error}")
            start = False
            
        elif 'who are you' in query:
            speak("My name is Nebula an AI personal assistant ,I can send mails ,play music and i can search for websites and information in wikipedia")
            
        elif 'whatsapp' in query:
            #speak("what should i tell")
            #msg = takecommand()
            #kit.sendwhatmsg_instantly("+918790748995", f"{msg}")
            kit.sendwhatmsg_instantly("+918790748995", "hello")
            time.sleep(15)
            pyautogui.press('Enter')
            start = False

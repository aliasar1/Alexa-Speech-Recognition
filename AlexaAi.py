import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import pywhatkit
import pyjokes
import os
import smtplib
from email.message import EmailMessage

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)   
    engine.runAndWait()

def wishMessage():
    hour = int(datetime.datetime.now().hour)
    if hour >=0 and hour <=12:
        speak("Good Morning Ali Asar.")
        print()
    elif hour >12 and hour <18:
        speak("Good afternoon Ali Asar.")
        print()
    else:
        print()
        speak("Good Night Ali Asar.")    

    speak("I am Alexa how may I help you sir?")    


def listening():
    listener = sr.Recognizer()
    try:        
        with sr.Microphone() as source:
            print("Listening...")
            listener.adjust_for_ambient_noise(source,duration=1)
            voice = listener.listen(source)

            print("\nRecongnising...")
            command = listener.recognize_google(voice, language= 'en-in')
            command = command.lower()
            print(f"User said: {command}")

    except Exception as e:
        # print("Error Found: " + str(e)) 
        return "None"
    return command

def sendMail(to, subject, text):
    sender = 'write your email here'
    password = 'write your password here'
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(sender, password)
    # server.sendmail(sender, to, text)
    email = EmailMessage()
    email['From'] = sender
    email['To'] = to
    email['Subject'] = subject
    email.set_content(text)
    server.send_message(email)

if __name__ == '__main__':
    chrome_path = "C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"

    wishMessage()
    while True:
        query = listening()

        if 'wikipedia' in query:
            try:
                speak("Searching wikipedia")
                query = query.replace("wikipedia", "")
                results = wikipedia.summary(query, sentences= 2)
                speak("According to wikipedia")
                speak(results)
            except Exception as e:
                speak("Couldn't find anything related to that.")

        elif 'open youtube' in query:
            url='https://www.youtube.com/'
            webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))
            webbrowser.get('chrome').open_new_tab(url)

        elif 'open google' in query:
            url='https://www.google.com'
            webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))
            webbrowser.get('chrome').open_new_tab(url)

        elif 'play' in query:
            song = query.replace("play","")
            speak("Playing " + song)
            pywhatkit.playonyt(song)
            
        elif 'time' in query:
            myTime = datetime.datetime.now().strftime("%I:%M %p")
            print(myTime)
            speak(f"Sir the time is {myTime}")

        elif 'open code' in query:
            path = "C:\\Users\\aliar\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(path)

        elif 'joke' in query:
            speak(pyjokes.get_joke())

        elif 'email' in query:
            while True:
                try:
                    speak("What is the subject of your email sir?")
                    subject = listening()
                    speak("What should I say")
                    mail = listening()
                    to = 'write email whom you want to send email'
                    sendMail(to, subject, mail)
                    speak("Email has been sent")
                    break
                except Exception as e:
                    speak("I didn't get it.")   

        elif 'exit' in query:
            speak("Shutting down the system. GoodBye Ali asar have a nice day")
            exit()    

        else:
            speak("Please say that again sir")  


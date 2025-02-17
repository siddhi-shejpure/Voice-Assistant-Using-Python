import pyttsx3 
import speech_recognition as sr
import datetime
import webbrowser
import os
import smtplib
import time
import winshell
import requests
import cv2
import ctypes
import subprocess

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id) # 0 for male, 1 for female voice

def go_deaf():
            speak("For how long should I not listen?Specify a number in seconds, for example 10")
            a = int(accept_input())
            time.sleep(a)
            a=str(a)
            speak("I am back after pretending to be deaf for "+a+"seconds")

def initial_greetings():
    hour=int(datetime.datetime.now().hour)

    if (hour>=0 and hour<=12):
        speak("Wake up, it's time to get going!!")
        print("Wake up, it's time to get going!!")
    elif(hour>=12 and hour<18):
        speak("Afternoon, get going!")
        print("Afternoon, get going!")
    else:
        speak("Evening, get going!")
        print("Evening, get going!")

    speak("I am your assistant. What are you looking for?")
    print("I am your assistant. What are you looking for?")

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def accept_input():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening to you...")
        r.pause_threshold=1
        audio=r.listen(source)

    try:
        print("Recognizing your input....")
        query=r.recognize_google(audio,language='en-in')
        print(f"You spoke: {query}\n")

    except Exception as e:
        print("Encountered some problem, say it again please")
        speak("Encountered some problem, say it again please")
        return "None"

    return query

def sendEmail(to, content):
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('siddhishejpure27@gmail.com','xvxw jajg rmhb nngb')
    to = 'siddhishejpure@gmail.com'
    server.sendmail('siddhishejpure27@gmail.com',to,content)
    print('send mail')
    server.close()

url = "https://official-joke-api.appspot.com/random_joke"
json_data = requests.get(url).json()
arr = ["",""]
arr[0]=json_data["setup"]
arr[1]=json_data["punchline"]
def joke():
    return arr 

def browser_access(url):
    webbrowser.open_new_tab(url)

def write_note():
            speak("What should I write, mam")
            note = accept_input()
            file = open('Note.txt', 'w')
            file.write(note)
            speak("Done sir, find your written note in the same working directory!")

if __name__=='__main__':
    initial_greetings()

    while True:
        query=accept_input().lower()

        if query==0:
            continue

        if 'open notepad' in query:
            npath="C:\\Windows\\system32\\notepad.exe"
            os.startfile(npath)

        elif 'write a note' in query:
            write_note()

        elif "show note" in query:
            speak("Showing Notes")
            file = open("Note.txt", "r")
            print(file.read())
            speak("Kindly watch the note contents printed on your terminal")

        elif "don't listen" in query or "stop listening" in query:
            go_deaf()

        elif 'empty recycle bin' in query:
            speak("On it!")
            winshell.recycle_bin().empty(confirm = False, show_progress = True, sound = True)
            speak("Recycle Bin Recycled")
            print("Recycle Bin Recycled")

        elif 'open youtube' in query:
            browser_access("youtube.com")

        elif 'open google' in query:
            browser_access("google.com")

        elif 'open spotify' in query:
            browser_access("spotify.com")

        elif 'time' in query:
            strtime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Current time is {strtime}")
            print(f"Current time is {strtime}")

        elif 'open purohit sir youtube channel' in query:
           browser_access("https://www.youtube.com/channel/UC_4NoVAkQzeSaxCgm-to25A")
        
        elif 'open linkedin' in query:
            browser_access("linkedin.com")

        elif 'wikipedia' in query:
            browser_access('https://www.wikipedia.org/')

        elif 'email to a friend' in query:
            try:
                speak("Speak up your content")
                content=accept_input()
                to="siddhishejpure@gmail.com"
                sendEmail(to,content)
                speak("Email sent successfully")

            except Exception as e:
                print(e)
                speak("Encountered error while sending email, sorry!")

        elif 'bye'  in query or 'tata' in query:
            speak("Your assistant is shutting down, goodbye")
            print("Your assistant is shutting down, goodbye")
            break

        elif "camera" in query or "take a photo" in query:
    # Open the default camera (0 for the primary camera)
            cap = cv2.VideoCapture(0)
    
            if not cap.isOpened():
             speak("Sorry, I could not access the camera.")
            else:
             speak("Taking a photo.")
        # Read a frame from the camera
            ret, frame = cap.read()
        
            if ret:
            # Save the captured image
              cv2.imwrite("C:\\Users\\siddh\\OneDrive\\Desktop\\img.jpg",frame)
              speak("Photo saved as img.jpg on desktop.")
              print("Photo saved as img.jpg on desktop.")
            else:
              speak("Failed to capture the photo.")
        
        # Release the camera resource
              cap.release()
              cv2.destroyAllWindows()

        elif 'open news' in query:
            speak("I've got Hindustan times and Economic times for you")
            browser_access("https://www.hindustantimes.com/")
            browser_access("https://economictimes.indiatimes.com/")
            speak("Enjoy reading")

        elif 'lock window' in query:
                speak("locking the device")
                ctypes.windll.user32.LockWorkStation()

        elif 'shutdown system' in query:
                speak("Hold on a sec! Your system is on its way to shut down.")
                subprocess.call('shutdown /p /f', shell=True)


        elif "hibernate" in query or "sleep" in query:
                 speak("Hibernating")
                 subprocess.call("shutdown /h", shell=True)


        elif 'current weather is' in query:
            browser_access("https://openweathermap.org/city/1259229")

        elif 'open' in query:
            query = query.replace("open", "")
            browser_access(query)
            time.sleep(5)	

        elif 'nothing' in query:
            speak("Should I stop listening then? ")
            hold=accept_input()

            if 'yes' in hold:
                go_deaf()
            else:
                speak("Okay, on standby then! Still listening to you without causing any disturbance!")

        elif "tell me a joke" or "jokes" in query:
             arr=joke()
             print(arr[0])
             speak(arr[0])
             print(arr[1])
             speak(arr[1])

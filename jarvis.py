import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import random
import smtplib
import subprocess as sp
import pyautogui



engine = pyttsx3.init('sapi5')
voices= engine.getProperty('voices')                        #getting details of current voice
                                                            # print(voices[1].id)
engine.setProperty('voice',voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak("Hello  sir.How may i Help you")

def takeCommand():                                            #It takes microphone input from the user and returns string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
        
    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')     #Using google for voice recognition.
        print(f"User said: {query}\n")                          #User query will be printed.

    except Exception as e:
        # print(e)    
        print("Say that again please...")                       #Say that again will be printed in case of improper voice 
        return "None"                                           #None string will be returned
    return query

if __name__ == "__main__":
    wishme()
    # while True:
    if 1:
        query = takeCommand().lower()         #Converting user query into lower case

        # Logic for executing tasks based on query
        if 'wikipedia' in query:  #if wikipedia found in the query then this block will be executed
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=1) 
            speak("According to Wikipedia")
            print(results)
            speak(results)


        elif 'how are you' in query:
            speak("I am fine, Thank you")
            speak("How are you, Sir")
 
        elif 'fine' in query or "good" in query:
            speak("It's good to know that your fine")
 
        elif "change my name to" in query:
            query = query.replace("change my name to", "")
            assname = query
 
        elif "change name" in query:
            speak("What would you like to call me, Sir ")
            assname = takeCommand()
            speak("Thanks for naming me")

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open my college website' in query:
            webbrowser.open("https://www.bitmesra.ac.in/")

        elif 'open hotstar' in query:
            webbrowser.open("hotstar.com")

        elif 'open code' in query:
            codePath = "C:\\Users\\Hii\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'open dev c code' in query:
            codePath = "C:\\Program Files (x86)\\Dev-Cpp\\devcpp.exe"
            os.startfile(codePath)

        elif 'play music' in query:
            music_dir = 'D:\\songs'
            songs = os.listdir(music_dir)
            print(songs)
            random = os.startfile(os.path.join(music_dir, songs[0]))                 

        elif 'open website' in query:
            speak("Please type the name of the website that you want to open (specify the full url) \n")
            website_name = input()
            print(website_name)
            webbrowser.get('"C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe" %s').open(website_name)
            speak(f"{website_name} opened.")        

        elif 'search' in query:
            speak("What do you want me to search for (please type) ? ")
            search_term = input()
            search_url = f"https://www.google.com/search?q={search_term}"
            webbrowser.get('"C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe" %s').open(search_url)
            speak(f"here are the results for the search term: {search_term}")

        elif 'take a screenshot' in query:
            image = pyautogui.screenshot()
            image.save('screenshot.png')
            speak('Screenshot taken.')

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            print(strTime)
            speak(f"Sir, the time is {strTime}")        
 
        elif 'exit' in query:
            speak("Thanks for giving me your time")
            exit()



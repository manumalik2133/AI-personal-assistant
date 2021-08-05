

import os
import time
import subprocess 
import json
from wikipedia.wikipedia import page, search
import wolframalpha
import requests
import webbrowser
import wikipedia
import datetime
import instaloader
import speech_recognition as sr
import pyttsx3

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

def speak(text):
    engine.say(text)
    engine.runAndWait()

def wishMe():
    hour = datetime.datetime.now().hour
    if hour >= 0 and hour < 12:
        speak("hello, good morning Mr. Manu. It's a beautiful day, and I can't stop myself from smiling!")
        print('hello, good morning Mr. Manu')
    elif hour >= 12 and hour <=18:
        speak('hello, good afternoon Mr. Manu. Sunny days are my favorite days')
        print('hello, good afternoon Mr. Manu')
    else:
        speak("hello, good evening Mr. Manu. It's late go to bed and sleep")
        print("hello, good evening Mr. Manu")
    
def news():
    api_id = "https://newsapi.org/v2/top-headlines?country=us&apiKey=828a1e8c2414499b808b36371ac5af90"
    json_data = requests.get(api_id).json()
    ar = []
    for i in range(3):
        ar.append(json_data["articles"][i]["title"]+".")
        return ar   

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.energy_threshold = 10000
        r.adjust_for_ambient_noise(source,1.2)
        print('I AM LISTENING')
        audio = r.listen(source)
        
        try:
            statement = r.recognize_google(audio,language='en-in')
            print(f"user said:{statement}\n")
                
        except Exception as e:
            speak("pardon me, please say that again")
            return "None"
        return statement
        
print('LOADING YOUR A.I PERSONAL ASSISTANT MAVRICK')
speak("LOADING YOUR PERSONAL AI ASSISTANT MAVRICK")
wishMe()

if __name__ == '__main__':
    while True:
        speak("Tell me how can i help you?")
        statement = takeCommand().lower()
        if statement == 0:
            continue
        
        if "goodbye" in statement or "ok bye" in statement or "stop" in statement:
            speak("Your personal AI assistant MAVRICK is shutting down,Good Bye")
            print("Your personal AI assistant MAVRICK is shutting down,Good Bye")
            break
        
        elif 'wikipedia' in statement:
            speak("searching wikipedia.......")
            statement = statement.replace("wikipedia"," ")
            results = wikipedia.summary(statement , sentences = 3)
            speak("According to wikipeadia.....")
            print(results)
            speak(results)
        
        elif "open youtube" in statement:
            webbrowser.open_new_tab("https://www.youtube.com")
            speak("Youtube is open for you")
            time.sleep(5)
        
        elif "open google" in statement:
            webbrowser.open_new_tab("https://www.google.com")
            speak("Google search is open for you")
            time.sleep(5)
            
        elif "open gmail" in statement:
            webbrowser.open_new_tab("https://mail.google.com/mail/u/1/#inbox")
            speak("Your gmail is open for you")
            time.sleep(5)
        
        elif "headline" in statement:
            print("Sure sir, now i will tell today's headline")
            speak("Sure sir, now i will tell today's headline")
            arr = news()
            for i in range(len(arr)):
                print(arr[i])
                speak(arr[i])
                

        
        elif "time" in statement:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"the time is {strTime}")
        
        elif "who are you" in statement or "what can you do" in statement:
            speak("I am  MAVRICK 1 point 0 your personal assistant. I am programed to do minor tasks like opening YouTube, Gmail, Google chrome and stack overflow. Predict current time, search Wikipedia to abstract required data, play music , videos, get top headline news from Times of India and can answer computational and geographical questions too.")
            
        elif "who made you" in statement or "who created you" in statement or "who discovered you" in statement:
            speak("I WAS BUILD BY MANU")
            print("I WAS BUILD BY MANU")
        
        elif "open stackoverflow" in statement:
            webbrowser.open_new_tab("httPs://stackoverflow.com/login")
            time.sleep(5)
         
        elif "news" in statement:
            news = webbrowser.open_new_tab("https://timesofindia.indiatimes.com/home/headlines")
            speak("Here sre some headlines for you from Times Of India - happy reading")
            time.sleep(7)
         
        elif "search" in statement:
            speak("what do you want me to search")
            search = takeCommand()
            url = f"https://www.google.com/search?q={search}" 
            # statement = statement.replace("search","")
            webbrowser.open_new_tab(url)
            time.sleep(5)  
        
        elif "download" in statement:
            speak("enter the profile name")
            mod = instaloader.Instaloader()
            a = input("Enter The Profile Name -->  ")
            mod.download_profile(a,profile_pic_only=True)
        
        elif "ask" in statement:
            speak("I can answer to computational and geographical questions too just try me!! what do you want to ask")
            question = takeCommand()
            app_id = "R2K75H-7ELALHR35X"
            client = wolframalpha.Client('R2K75H-7ELALHR35X')
            res = client.query(question)
            answer = next(res.results).text
            speak(answer)
            print(answer)
        
        elif "age" in statement or "old" in statement:
            speak("I am sweet 16 with 44 years of experience")
            print("I am sweet 16 with 44 years of experience")

        elif 'play music' in statement or 'songs' in statement:
            speak("playing music")
            print("playing music")
            songs_dir = ('D:\\music')
            songs = os.listdir(songs_dir)
            os.startfile(os.path.join(songs_dir,songs[1])) 

        elif 'breaking bad' in statement:
            speak("playing Breaking Bad")
            print("playing Breaking Bad")
            video_dir = ('D:\\TV\\Breaking Bad Season 1-5\\Breaking Bad Season 1')
            video = os.listdir(video_dir)
            os.startfile(os.path.join(video_dir,video[0]))        
                       
        elif "log off" in statement or "sign out" in statement or "shut down" in statement:
            speak("Ok, your PC  will shut down in 10 seconds - make sure you have saved and exit from all applications")
            subprocess.call(['shutdown',"/1"])
            
time.sleep(3)            
            
            
            
            
            
            
            
            
            
            
            














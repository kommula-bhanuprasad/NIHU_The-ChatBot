import pyttsx3
import webbrowser
import wikipedia
import speech_recognition as sr
import os
import datetime

print("initializing NIHU")

engine=pyttsx3.init("sapi5")
voice=engine.getProperty('voices')
engine.setProperty('voice', voice[1].id)


def speak(text):
    engine.say(text)
    engine.runAndWait()
    
    
def wishme():
    hr =int(datetime.datetime.now().hour)
    
    
    if hr>=0 and hr<12:
        speak("GOOD MORNING BHANU")
    elif hr>=12 and hr < 18:
        speak("good afternoon BHANU")
    else:
        speak("good evening  BHAANNU ...")
    
    speak("I am your Assistant NEEHU....")
    

def com():
    r = sr.Recognizer()
    with sr.Microphone() as source:
         print("listening...")
         r.pause_threshold = 1
         audio = r.listen(source)
         
    try:
        print("recognizing...")
        query = r.recognize_google(audio, language ='en-in')
        print(f"BHANU  : ", query)
    except Exception as e:
        print(e)
        speak("Sorry BHANU , తప్పకుండా can you repeat that again?")
        return "None"
    return query


print("initializing NIHU")
speak("initializing NEEHU")


if __name__ == "__main__":
    wishme()
    while True:
        #speak("How can i help you?")
        query = com().lower()
        if 'wikipedia' in query:
                speak("searching in wikipedia")
                query = query.replace("wikipedia", "")
                results = wikipedia.summary(query, sentences = 2)
                speak("According to wikipedia")
                print(results)
                speak(results)

        elif 'open youtube' in query:
            url="youtube.com"
            chrome_path="C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"
            webbrowser.get(chrome_path).open(url)
            speak("youtube is opened")
        elif 'google' in query:
            webbrowser.open("google.com")
            speak("google is opened")
        elif 'anything' in query:
            speak(" its may, 2 . its my birth day, and you forgot my birthday.")
        elif 'sorry' in query:
            speak("""am soo soo sorry SISTER. PRASHANTHII sis """)
        elif 'sister' in query:
            speak("""truly am so sorry SISTER, SAY A THING WHY WE THOSE FOOLISH STUFF. LETS CARE ABOUT OUR LIFES. WE R WE . PRASHANTHII sis """)
        elif 'been' in query:
            speak("OK  తప్పకుండా")
        elif 'i ' in query:
            speak("i knew her arrival, just waiting for attention. welcome back SIS, HOW ARE YOU, HOW IS BAVA BAAVVAA ")

        elif 'gmail' in query:
            webbrowser.open("gmail.com")
            speak("gmail is opened")
        elif 'song' in query:
            music_dir = 'D:\\music\\baahubali2'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[2]))
            speak("music is being played")
        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"the time is {strTime}")
        
        elif ' take care ' in query:
            speak("bye, see you soon BHANU")
            exit()
        else :
            speak("")
      

import webbrowser
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os

engine = pyttsx3.init("sapi5")
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wish():
    time = int(datetime.datetime.now().hour)
    if time >= 0 and time < 12:
        print("Good Morning")
        speak("Good Morning")
    elif time >=12 and time < 18:
        print("Good Afternoon")
        speak("Good Afternoon")
    else:
        print("Good Evening")
        speak("Good Evening")
    print("Hello my name is Alex. How can I help you?")
    speak("Hello my name is Alex. How can I help you?")

def input():
    r = sr.Recognizer() 
    with sr.Microphone() as source:
        print("Listening......")
        r.pause_threshold = 1
        input = r.listen(source)

    try:
        print("Processing....")
        query = r.recognize_google(input, language='en-in')
        print("Your Input: ",query)

    except:
        return "None"
    return query


if __name__ == "__main__":
    wish()
    while True:
        query = input().lower()
        if 'how are you' in query:
            speak("I am fine sir. How are you?")
        elif 'fine' in  query:
            speak("Well good sir.How can i help you")
        elif 'open youtube' in query:
            speak("Opening youtube")
            webbrowser.open('youtube.com')
        elif 'open gmail' in query:
            speak("Opening Gmail")
            webbrowser.open('gmail.com')
        elif 'open google' in query:
            speak("Opening Google")
            webbrowser.open('google.com')
        elif 'open whatsapp' in query:
            whatsapp_path = "C:\\Program Files\\WindowsApps\\5319275A.WhatsAppDesktop_2.2226.6.0_x64__cv1g1gvanyjgm\\app\\WhatsApp.exe"
            speak("Opening Whatsapp")
            os.startfile(whatsapp_path)
        elif 'open camera' in query:
            camera_path = "C:\\Program Files\\WindowsApps\\Microsoft.WindowsCamera_2022.2206.2.0_x64__8wekyb3d8bbwe\\WindowsCamera.exe"
            speak("Opening camera")
            os.startfile(camera_path)
        elif 'open calculator' in query:
            calculator_path = "C:\\Program Files\\WindowsApps\\Microsoft.WindowsCalculator_11.2206.0.0_x64__8wekyb3d8bbwe\\CalculatorApp.exe"
            speak("Opening calculator")
            os.startfile(calculator_path)
        elif 'the time' in query:
            time = datetime.datetime.now().strftime("%H:%M:%S")
            print("The time is ",time)
            speak(f"The time is {time}")
        elif 'search' in query:
            query = query.replace("alex search","")
            query = query.replace("search","")
            query = query.replace("google search","")
            query = query.replace("google","")
            speak("According to wikipedia..")
            result = wikipedia.summary(query,2)
            print(result)
            speak(result)
        elif 'thank you' or 'thanks' in query:
            speak("Thank You Sir")
            break

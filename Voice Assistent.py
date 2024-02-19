import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
import os
import tkinter as tk

#convert text into speech. 
def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

# It attempts to recognize speech using Google's Speech Recognition service
def get_audio():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source, duration=1)
        audio = recognizer.listen(source)

        try:
            print("Recognizing...")
            query = recognizer.recognize_google(audio)
            print(f"User: {query}")
            return query.lower()
        except sr.UnknownValueError:
            print(f"Sorry, I did not hear your request. Please repeat.")
            return ""
        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition service; {e}")
            return ""

def assistant(command):
    if "open youtube" in command:
        webbrowser.open("https://www.youtube.com/")
        print("youtube")
    elif "open google" in command:
        webbrowser.open("https://www.google.com/")
    elif "on google" in command and "search" in command:
            search_url = "https://www.google.com/search?q="
            search = command.replace("search", "").replace("on google", "").strip()
            search = "+".join(search.split())
            url = search_url + search
            webbrowser.open(url)

    elif "tell me the time" in command or "what time it is" in command:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"The current time is {current_time}")
    # elif "open" in command:
    #     prog = command.replace("open", "").strip()
    #     os.system(prog)
    elif "exit" in command or "quit" in command:
        speak("Goodbye!")
        exit()
    else:
        speak(f"I'm sorry, I don't understand that command.")

if __name__ == "__main__":
    window = tk.Tk()
    greeting = tk.Label(text="Hello! How can I assist you today?")
    greeting.pack()
    speak("Hello! How can I assist you today?")
    
    while True:
        user_command = get_audio()

        if user_command:
            assistant(user_command)
            
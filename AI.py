import pyttsx3 
import speech_recognition as sr 
import datetime
import os 
import webbrowser 
import wikipedia 
import subprocess
from selenium import webdriver

#Defining the engine i.e. sapi5
engine = pyttsx3.init('sapi5') #Speech Interface provided by Microsoft
voices = engine.getProperty('voices') 
engine.setProperty('voice', voices[1].id) #Setting up the voice property and choosing voice 1 here


#To activate the speak function
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    

#For Speech Recognition - It takes microphone input from the user and returns string output
def takeCommand():
    
    #This shows that the microphone is now active
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("\nI am listening...")
        r.pause_threshold = 0.5
        r.operation_timeout = 50
        r.energy_threshold = 1000
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)
        
    #To check if the system is able to take input from us
    try:
        print("\nProcessing...\n")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}")

    except Exception as e:
        print("Say that again, please...")
        speak("Say that again please")  
        return "None"
    return query

#Function made for greeting the user
def greetings():
    hour = int(datetime.datetime.now().hour)
    #For Morning
    if hour>=0 and hour<12:
        speak("Good Morning!")

    #For Afternoon
    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    #For Evening
    else:
        speak("Good Evening!")  

def note(text):
    date = datetime.datetime.now()
    file_name = str(date).replace(':', "-") + "-note.txt"
    with open(file_name, "w") as f:
        f.write(text)

    subprocess.Popen(["notepad.exe", file_name])


class yt():
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path="C:/Users/nihal/.wdm/drivers/chromedriver/win32/100.0.4896.60/chromedriver.exe")
    def play(self, query):
        self.query = query
        self.driver.get(url="https://www.youtube.com/results?search_query=" + query)
        video = self.driver.find_element_by_xpath('//*[@id="dismissible"]')
        video.click()
    
class goog():
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path="C:/Users/nihal/.wdm/drivers/chromedriver/win32/100.0.4896.60/chromedriver.exe")
    def sea(self, query):
        self.query = query
        self.driver.get(url="https://www.google.com/")
        link = self.driver.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input')
        link.click()
        link.send_keys(query)
        enter = self.driver.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[2]/div[2]/div[5]/center/input[1]')
        enter.click()


        

if __name__ == "__main__":

    greetings()
    # speak("This program is built to help people access their computers hands-free just by giving voice commands. Hope you enjoy using it.")       
    # speak("Please provide a task to perform.")
    
    print("\nList of commands")
    print("1. Hello")
    print("2. What is your name?")
    print("3. How are you?")
    print("4. Tell me the time.")
    print("5. Wikipedia - *Whatever you want to wiki*")
    print("6. Open youtube - To open Youtube in your browser")
    print("7. Open Google - To open google in your browser")
    print("8. Open Code editor - To VS Code")
    print("9. Search youtube - for playing a video on youtube")
    print("10. Search google - To search anything on google")
    print("11. Make a note for me / Write this down for me / Jot this down / Remember this - To make the bot write a note")
    print("12. Go to sleep - To deactivate the bot")
    print("13. Activate - To activate the bot")
    print("14. Give me the list of commands - To get the list of commands")

    while True:
    # if 1:        
        query = takeCommand().lower()
  


        if "hello" in query.lower():
            speak("Hi. How are you?")

        elif "what about you" in query.lower():
            speak("I am doing well.")
        
        elif "your name" in query.lower():
            speak("I am a bot and I have not been named yet.")
        
        elif "greet" in query:
            greetings()
            speak("I hope you are doing well.")

        elif "how are you" in query:
            speak("I am doing well.")

        elif 'time' in query.lower():
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"The current time is {strTime}")

        
        
#ADVANCE QUERIES
        #To search wikipedia
        elif 'wikipedia' in query.lower():
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        #To open youtube in browser
        elif 'open youtube' in query.lower():
            webbrowser.open("youtube.com")
            print("\nOpening Youtube")

        elif 'open google' in query.lower():
            webbrowser.open("google.com")
            print("\nOpening Google")

        
#MANUAL SEARCHING IN BROWSER 
        #Searching youtube videos and playing them
        elif 'search youtube' in query.lower():
            r = sr.Recognizer()
            with sr.Microphone() as source:
                speak("What do you want me to play")
                print("\nwhat do you want me to play\n")
                r.pause_threshold = 1
                r.operation_timeout = 50
                r.energy_threshold = 500
                audio = r.listen(source)
            
                print("\n...\n")    
                query = r.recognize_google(audio, language='en-in')
                print(f"You said: {query}")
            
            
            p1 = yt()
            p1.play(query)


        #Input searching
        elif 'search google' in query.lower():
            r = sr.Recognizer()
            with sr.Microphone() as source:
                speak("What do you want me to search")
                print("\nwhat do you want me to search\n")
                r.pause_threshold = 1
                r.operation_timeout = 50
                r.energy_threshold = 10000
                audio = r.listen(source)
            
                print("\n...\n")    
                query = r.recognize_google(audio, language='en-in')
                print(f"You said: {query}")

            p2 = goog()
            p2.sea(query)
  

#MIC MANIPULATION
    #For activation and deactivation of mic
        elif 'go to sleep' in query.lower():
            speak("going into sleep mode")
            while query != 'activate':
                r = sr.Recognizer()
                with sr.Microphone() as source:
                    print("\nBot is sleeping")
                    r.pause_threshold = 1
                    r.operation_timeout = 50
                    r.energy_threshold = 500
                    audio = r.listen(source)
        
                try:
                    print("\n...\n")    
                    query = r.recognize_google(audio, language='en-in')
                    print(f"You said: {query}")

                except Exception as e:
                    print("\n...") 
            
            speak("I am back online.")
            print("\nI am back online.")


        elif 'open editor' in query.lower():
            codePath = "D:\Microsoft VS Code\Code.exe"
            os.startfile(codePath)
            print("\nOpening VS Code now.")

        elif 'open notepad' in query.lower():
            os.startfile("notepad.exe")
            print("\nOpening Notepad.")
        
        elif 'open calculator' in query.lower():
            codePath = "C:\Program Files\WindowsApps\Microsoft.WindowsCalculator_11.2201.4.0_x64__8wekyb3d8bbwe\CalculatorApp.exe"
            os.startfile(codePath)
            print("\nOpening Calculator.")

        elif 'open camera' in query.lower():
            codePath = "C:\Program Files\WindowsApps\Microsoft.WindowsCamera_2022.2201.4.0_x64__8wekyb3d8bbwe\WindowsCamera.exe"
            os.startfile(codePath)
            print("\nOpening Camera.")
        
        elif 'open maps' in query.lower():
            codePath = "C:\Program Files\WindowsApps\Microsoft.WindowsMaps_11.2202.6.0_x64__8wekyb3d8bbwe\Maps.exe"
            os.startfile(codePath)
            print("\nOpening Maps.")
        
        elif 'open terminal' in query.lower():
            codePath = "C:\Program Files\WindowsApps\Microsoft.WindowsTerminal_1.6.10571.0_x64__8wekyb3d8bbwe\OpenConsole.exe"
            os.startfile(codePath)
            print("\nOpening Terminal.")

        elif 'open my pc' in query.lower():
            codePath = "C:\Windows\explorer.exe"
            os.startfile(codePath)
            print("\nOpening My PC")
        

    #NOTEPAD CONTROLS    
        #To make a note in notepad
        NOTE_STRS = ["make a note", "write this down", "remember this", "jot this down"]
        for phrase in NOTE_STRS:
            if phrase in query:
                speak("What would you like me to write down?")
                note_text = takeCommand().lower()
                note(note_text)
                speak("I've made a note of that.")
            



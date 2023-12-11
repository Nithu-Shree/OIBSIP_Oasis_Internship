import pyttsx3
import speech_recognition as sr
import webbrowser
import datetime
import wikipedia
import pyjokes
from ecapture import ecapture as ec
from colorama import init, Fore, Style
from rich.console import Console
from time import sleep

console = Console()


init(autoreset=True)


def speak_and_print(text, color=Fore.WHITE, align_right=False):
    formatted_text = f"{color}Eliza: {text}{Style.RESET_ALL}"
    if align_right:
        formatted_text = formatted_text.rjust(200)
    print(formatted_text)
    speak(text)


def take_command():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎤 Listening..".rjust(200) ,Fore.CYAN)
        recognizer.pause_threshold = 0.7
        audio = recognizer.listen(source)

    try:
        print("⌛Recognizing...".rjust(200), Fore.CYAN)
        query = recognizer.recognize_google(audio, language="en-in")
        print(f"{Fore.BLUE}You said: {query}{Style.RESET_ALL}".rjust(200), Fore.GREEN)

    except Exception as e:
        speak_and_print(str(e), Fore.RED, align_right=True)
        speak_and_print(
            "Sorry, I didn't catch that. Can you please repeat?",
            Fore.YELLOW,
            align_right=True,
        )
        return "None"

    return query.lower()


def speak(text):
    engine = pyttsx3.init()
    voices = engine.getProperty("voices")
    engine.setProperty("voice", voices[1].id)
    engine.say(text)
    engine.runAndWait()


def tell_time():
    time_now = datetime.datetime.now()
    formatted_time = time_now.strftime("%H:%M")
    speak_and_print(f"The current time is {formatted_time}", Fore.YELLOW)
    print("🕒")


def greeting():
    hour = datetime.datetime.now().hour
    if 0 <= hour < 12:
        speak_and_print("Good morning!", Fore.GREEN)
        print("🌅")
    elif 12 <= hour < 18:
        speak_and_print("Good afternoon!", Fore.YELLOW)
        print("☀️")
    else:
        speak_and_print("Good evening!", Fore.RED)
        print("🌙")

    speak_and_print("I am Eliza, your voice assistant.", Fore.CYAN)
    speak_and_print("May I know your name?", Fore.CYAN)
    uname = take_command()
    speak_and_print(f"Welcome, {uname}!", Fore.GREEN)
    print("😊")


def main():
    data = [1, 2, 3]
    with console.status("[bold green]Fetching data...") as status:
        while data:
            num = data.pop(0)
            sleep(1)
            console.log(f"[green]Finish fetching data[/green] {num}")

    console.log(f'[yellow][yellow]Done!')
    greeting()

    while True:
        query = take_command()

        if "open google" in query:
            speak_and_print("Opening Google.", Fore.GREEN)
            print("🔍")
            webbrowser.open("https://www.google.com")

        elif "hello" in query:
            speak_and_print(
                "Hi there, I'm Eliza 1.0 at your service! How can I assist you today?",
                Fore.GREEN,
            )
            print("👋")

        elif "date" in query:
            today_date = datetime.datetime.now().strftime("%A, %B %d, %Y")
            speak_and_print(f"The current date is {today_date}.", Fore.YELLOW)
            print("📅")

        elif "time" in query:
            tell_time()

        elif "exit" in query or "bye" in query:
            speak_and_print(
                "Goodbye! If you have more questions in the future, feel free to ask. Take care!",
                Fore.CYAN,
            )
            print("👋")
            exit()

        elif "from wikipedia" in query:
            speak_and_print("Searching Wikipedia.", Fore.YELLOW)
            print("🌐")
            query = query.replace("wikipedia", "")
            result = wikipedia.summary(query, sentences=3)
            speak_and_print("According to Wikipedia", Fore.CYAN)
            speak_and_print(result, Fore.GREEN)

        elif "name" in query:
            speak_and_print(
                "You can call me Eliza. How can I help you today?", Fore.CYAN
            )
            print("📛")

        elif "youtube" in query:
            speak_and_print("Opening Youtube.", Fore.GREEN)
            print("▶️")
            webbrowser.open("https://www.youtube.com")

        elif "how are you" in query:
            speak_and_print("I am fine, thank you. How about you?", Fore.CYAN)
            print("😊")

        elif "fine" in query or "good" in query:
            speak_and_print("It's good to know that you're fine.", Fore.GREEN)
            print("😊")

        elif "joke" in query:
            joke = pyjokes.get_joke()
            speak_and_print(joke, Fore.CYAN)
            print("😂")

        elif "who made you" in query or "who created you" in query:
            speak_and_print("I have been created by Nithu Shree.", Fore.YELLOW)
            print("😊")

        elif "camera" in query or "take a photo" in query:
            speak_and_print("Capturing a photo.", Fore.GREEN)
            print("📷")
            ec.capture(0, "Eliza Camera ", "img.jpg")


if __name__ == "__main__":
    main()

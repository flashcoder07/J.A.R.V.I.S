import openai
import pyttsx3
import speech_recognition as sr
import webbrowser

openai.api_key = "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"

# Initializing text-to-speech engine
engine = pyttsx3.init('sapi5')
voice = engine.getProperty('voices')
engine.setProperty('voices', voice[0].id)


def answer(question):
    prompt = f"{question}\n"
    response = openai.Completion.create(prompt=prompt, engine="text-davinci-002")
    aans = response.choices[0].text.strip()
    return aans


def talk(text):
    engine.say(text)
    engine.runAndWait()


def openwebsite(url):
    webbrowser.open(url)
    talk(f"Opening {url}")


def listen_and_reply():
    recognizer = sr.Recognizer()

    try:
        with sr.Microphone() as source:
            print("Listening for 'Jarvis'...")
            audio = recognizer.listen(source)

            command = recognizer.recognize_google(audio).lower()

            if 'jarvis' in command:
                print("Jarvis activated. Listening...")
                talk("Hello, how can i help you sir")

                while True:
                    audio = recognizer.listen(source)
                    query = recognizer.recognize_google(audio).lower()

                    if 'shutdown' in query:
                        print("Shutting down Jarvis.")
                        talk("Goodbye Sir")
                        break
                    elif 'open website' in query:
                        website_name = query.split('open website')[1].strip()
                        if 'google' in website_name:
                            openwebsite('https://www.google.com')
                        elif 'youtube' in website_name:
                            openwebsite('https://www.youtube.com')
                        elif 'chess' in website_name:
                            openwebsite('https://www.chess.com/play/online')
                        elif 'spotify' in website_name:
                            openwebsite('https://open.spotify.com')
                        elif 'game1' in website_name:
                            openwebsite('https://skribbl.io')
                        elif 'game2' in website_name:
                            openwebsite('https://www.geoguessr.com')

                    else:
                        print(f"You said: {query}")
                        ans = answer(query)
                        talk(ans)

    except sr.UnknownValueError:
        print("Sorry, there is trouble in your audio.")
    except sr.RequestError as e:
        print(f"ERROR; {e}")


if __name__ == "__main__":
    listen_and_reply()

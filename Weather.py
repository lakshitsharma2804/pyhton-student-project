import requests
import asyncio
import edge_tts
import pygame
import os

pygame.mixer.init()

API_KEY = "30cbc22607ff7589cd041a53fde99839"


async def speak(text):
    file = "voice.mp3"

    try:
        communicate = edge_tts.Communicate(text, "en-US-AriaNeural")
        await communicate.save(file)

        pygame.mixer.music.load(file)
        pygame.mixer.music.play()

        while pygame.mixer.music.get_busy():
            await asyncio.sleep(0.1)

        pygame.mixer.music.stop()
        pygame.mixer.music.unload()

        if os.path.exists(file):
            os.remove(file)

    except Exception:
        pass


def get_weather():
    city = input("\nEnter City Name: ").strip()

    if city == "":
        print("Please enter a city name.")
        return

    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

    try:
        response = requests.get(url, timeout=10)
        data = response.json()

        if response.status_code == 200:
            temperature = round(data["main"]["temp"], 1)

            print(f"\nTemperature of {city.title()} is {temperature}°C")

            asyncio.run(
                speak(
                    f"The temperature of {city} is {temperature} degree Celsius"
                )
            )

        else:
            print("\nCity Not Found")
            asyncio.run(speak("City not found"))

    except requests.exceptions.ConnectionError:
        print("\nNo Internet Connection")

    except requests.exceptions.Timeout:
        print("\nRequest Timed Out")

    except Exception:
        print("\nSomething Went Wrong")


print("=" * 40)
print("      WEATHER TEMPERATURE APP")
print("=" * 40)

while True:
    get_weather()

    choice = input("\nDo you want to check another city? (Y/N): ").strip().lower()

    if choice == "n":
        asyncio.run(speak("Thank you for using Weather App. Goodbye"))
        print("\nThank You For Using Weather App")
        break

    elif choice != "y":
        print("\nInvalid Choice")
import asyncio
import edge_tts
import pygame
import os

pygame.mixer.init()

VOICE = "en-US-AriaNeural"

async def speak(text):
    file = "voice.mp3"
    communicate = edge_tts.Communicate(text, VOICE)
    await communicate.save(file)

    pygame.mixer.music.load(file)
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        await asyncio.sleep(0.1)

    pygame.mixer.music.unload()
    os.remove(file)

print("Welcome To RoboSpeaker 2.0 Created By Lakshit")

while True:
    text = input("Enter What You Want Me To Speak: ")

    if text.lower() == "q":
        asyncio.run(speak("Bye Bye Friend"))
        break

    asyncio.run(speak(text))
import pygame
import keyboard
import os
import time  

pygame.mixer.init()

MUSIC_FOLDER = r"C:\\Users\\ospan\\OneDrive\\Рабочий стол\\PP2\\Ospanali-PP2-fall\\lab07\\music"
songs = [os.path.join(MUSIC_FOLDER, song) for song in os.listdir(MUSIC_FOLDER) if song.endswith(".mp3")]

if not songs:
    print("No music!")
    exit()

current_song = 0

def play():
    pygame.mixer.music.load(songs[current_song])
    pygame.mixer.music.play()
    print(f"Playing: {os.path.basename(songs[current_song])}")

def stop():
    pygame.mixer.music.stop()
    print("Music stopped.")

def next_song():
    global current_song
    current_song = (current_song + 1) % len(songs)
    play()

def prev_song():
    global current_song
    current_song = (current_song - 1) % len(songs)
    play()

print("Нажмите P - Play, S - Stop, N - Next, B - Previous, Q - Exit")

while True:
    if keyboard.is_pressed("p"):
        play()
        time.sleep(0.2)  

    elif keyboard.is_pressed("s"):
        stop()
        time.sleep(0.2)

    elif keyboard.is_pressed("n"):
        next_song()
        time.sleep(0.2)

    elif keyboard.is_pressed("b"):
        prev_song()
        time.sleep(0.2)

    elif keyboard.is_pressed("q"):
        print("Exit the program.")
        break
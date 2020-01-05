import os, time, sys
os.system("clear")
import pygame

pygame.init()
pygame.mixer.init()
sounda= pygame.mixer.Sound(r"C:\Users\Mike Strain\Desktop\PythonGeneralAssembly\CLASS7\Jukebox Homework\Carry On.mp3")

sounda.play()

# class Jukebox():
    
#     files_in_folder = os.listdir()
#     directory = os.getcwd()
#     mixer.init()
#     mixer.music.set_volume(0.05)
#     print(mixer.music.get_volume())

#     # def __init__(self):

#     #list the available songs
#     def list_songs(self):
#         while True:
#             for song in range(len(Jukebox.files_in_folder)):
#                 if Jukebox.files_in_folder[song][-3:] == 'mp3':
#                     print(str(song+1)+'.\t',Jukebox.files_in_folder[song][0:-4])
#             goBack = input("\nType 0 to go back..")
#             if goBack == str(0): 
#                 os.system("clear")
#                 break

#     #play a song
#     def play_a_song(self):
#         while True:
#             song_picked = input('Pick a song to play:')
#             try: 
#                 song_index = int(song_picked)-1
#                 break
#             except: print("Please pick an integer!")

#         song_path = os.path.join(Jukebox.directory,Jukebox.files_in_folder[song_index])
#         # print(song_path)
#         # mixer.Sound(song_path).play()
#         mixer.init()
#         mixer.Sound(Jukebox.files_in_folder[song_index])

#     #stop playback
#     def stop_playback(self):
#         mixer.music.stop()
    
#     #if music is playing, pause playback. Otherwise, unpause playback.
#     def pause_playback(self):
#         if mixer.music.get_busy(): mixer.music.pause()
#         else: mixer.music.unpause()

#     #next or previous song

#     #turn volume up or down
#     def set_volume(self):
#         mixer.music.set_volume()


# juke = Jukebox()

# while True:
#     print('\n')
#     print("_______ Welcome to the Jukebox _______")
#     print("Please enter a number to navigate the program.")
#     print("1 = List songs")
#     print("2 = Play a song")
#     print("3 = Pause/unpause")
#     print("4 = Stop")
#     print("5 = Change volume")
#     print("6 = Quit")

#     while True:
#         choice = input()
#         try: 
#             choice = int(choice)
#             break
#         except: print("Sorry, please enter an integer...")

#     if choice == 1:
#         juke.list_songs()
#     elif choice == 2:
#         juke.play_a_song()
#     elif choice == 3:
#         juke.pause_playback()
#     elif choice == 6:
#         break
#     else:
#         print('what?')


# # time.sleep(5)




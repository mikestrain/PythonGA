import os, time, sys
os.system("cls")
from pygame import mixer

class Jukebox():
    
    files_in_folder = os.listdir()
    directory = os.getcwd()
    mixer.init()
    mixer.music.set_volume(0.05)

    paused = 0
    song_playing = 0

    #list the available songs
    def list_songs(self):

        while True:
            os.system("cls")
            print("List of available songs:")
            for song in range(len(Jukebox.files_in_folder)):
                if Jukebox.files_in_folder[song][-3:] == 'mp3':
                    print(str(song+1)+'.\t',Jukebox.files_in_folder[song][0:-4])
            goBack = input("\nType 0 to go back..")
            if goBack == str(0): 
                os.system("cls")
                break

    #play a song
    def play_a_song(self,set_song="not assigned"):

        if set_song == "not assigned":
            while True:
                song_picked = input('Pick a song to play:')
                try: 
                    song_index = int(song_picked)-1
                    break
                except: print("Please pick an integer!")
        
        else: song_index = set_song

        song_path = os.path.join(Jukebox.directory,Jukebox.files_in_folder[song_index])
        mixer.music.load(song_path)
        mixer.music.play()
        Jukebox.song_playing = song_index

    #stop playback
    def stop_playback(self):
        mixer.music.stop()
    
    #if music is playing, pause playback. Otherwise, unpause playback.
    def pause_playback(self):
        if Jukebox.paused == 1:
            mixer.music.unpause()
            Jukebox.paused = 0
        elif mixer.music.get_busy(): 
            mixer.music.pause()
            Jukebox.paused = 1
        else: print("no music is playing.")

    #next or previous song
    def skip_song(self,direction):
        Jukebox.stop_playback(self)
        try:
            if direction == 'forward':
                Jukebox.play_a_song(self,Jukebox.song_playing+1)
                print(Jukebox.song_playing)
            else:
                Jukebox.play_a_song(self,Jukebox.song_playing-1)
        except:
            print("")


juke = Jukebox()

while True:
    os.system("cls")
    print("_______ Welcome to the Jukebox _______")
    print("Please enter a number to navigate the program.")
    print("1 = List songs")
    print("2 = Play a song")
    print("3 = Pause/unpause")
    print("4 = Next song")
    print("5 = Previous song")
    print("6 = Stop")
    print("7 = Quit")

    while True:
        choice = input()
        try: 
            choice = int(choice)
            break
        except: print("Sorry, please enter an integer...")

    if choice == 1:   juke.list_songs()
    elif choice == 2: juke.play_a_song()
    elif choice == 3: juke.pause_playback()
    elif choice == 4: juke.skip_song('forward')
    elif choice == 5: juke.skip_song('backward')
    elif choice == 6: juke.stop_playback()
    elif choice == 7: break
    else: print("sorry, that input isn't valid...")






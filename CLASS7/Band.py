import os
os.system("clear")


class Band():
    

    number_of_bands = 0
    known_genres = ["rock","pop","classical"]

    def __init__(self, genre, band_name, albums_released=0):
        self.genre = genre
        self.band_name = band_name
        self.albums_released = albums_released
        Band.number_of_bands += 1
        if not self.genre in Band.known_genres:
            print("This genre is unknown...")
    
    def print_stats(self):
        print("The",self.genre,"band",self.band_name, "has",self.albums_released,"albums.")

band1 = Band(genre = "rock", band_name="Queen", albums_released=15).print_stats()
band2 = Band(genre = "pop", band_name="The Beatles", albums_released=20).print_stats()
band3 = Band(genre = "rap", band_name="Wu Tang Clan", albums_released=20).print_stats()

print(Band.number_of_bands)
    

    

import pandas as pd

class MusicData:
    def __init__(self, file_path='tamil_songs.csv'):
        # Load the CSV file into a Pandas DataFrame
        self.data = pd.read_csv(file_path)

        # Display some info about the dataset
        print(self.data.head())  # Optional: to view the first few rows

    def get_songs(self):
        return self.data

    def get_song(self, song_id):
        return self.data.iloc[song_id]

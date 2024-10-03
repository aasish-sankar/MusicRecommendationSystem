import random
import numpy as np

class BanditAgent:
    def __init__(self, songs_df):
        self.songs_df = songs_df
        self.num_songs = len(songs_df)  # Get the number of filtered songs
        self.song_rewards = np.zeros(self.num_songs)  # Initialize cumulative rewards for each song
        self.total_rewards = 0
        self.n_trials = 0

    def recommend_song(self):
        # Randomly select a song index
        song_index = random.randint(0, self.num_songs - 1)
        song_data = self.songs_df.iloc[song_index]  # Get song data based on index
        return song_index, song_data

    def update_rewards(self, song_index, reward):
        self.song_rewards[song_index] += reward
        self.total_rewards += reward
        self.n_trials += 1

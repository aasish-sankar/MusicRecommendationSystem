from music_data import MusicData
from bandit_agent import BanditAgent
from user_feedback import UserFeedback

# Initialize MusicData and load songs
music_data = MusicData()  # Create an instance of the MusicData class
tamil_songs_df = music_data.get_songs()  # Get the DataFrame of songs

# Display the column names for debugging
print("Available columns:", tamil_songs_df.columns.tolist())  # Print the columns to identify 'actors'

# Ask user for preferred actor
preferred_actor = input("Enter your preferred actor: ")

# Filter songs by user-selected actor (ensure case-insensitive matching)
filtered_songs = tamil_songs_df[tamil_songs_df['actors'].str.contains(preferred_actor, case=False, na=False)]

if filtered_songs.empty:
    print(f"No songs found for the actor: {preferred_actor}")
else:
    # Initialize Bandit Agent with filtered songs
    agent = BanditAgent(filtered_songs)
    user_feedback = UserFeedback()

    # Recommend and provide feedback loop
    for i in range(10):  # Recommend 10 songs (modifiable)
        song_index, song_data = agent.recommend_song()
        print(f"Recommendation {i + 1}: {song_data['song_title']} from {song_data['movie']} (Actors: {song_data['actors']})")

        # Get feedback based on song rating
        feedback = user_feedback.get_feedback(song_data['song_rating'])  # Using song rating for feedback simulation
        agent.update_rewards(song_index, int(feedback))  # Update agent with feedback

        # Dynamically update user preferences based on feedback
        user_feedback.update_preferences(song_data['actors'], feedback)

        print(f"User feedback: {'Liked' if feedback else 'Disliked'}")

    # Summary of total rewards (liked songs) after the loop
    print(f"Total Rewards (Liked Songs): {agent.total_rewards}/{agent.n_trials}")

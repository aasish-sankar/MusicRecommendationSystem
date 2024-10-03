import numpy as np

class UserFeedback:
    def __init__(self):
        # Start with a default preference for all ratings (or actors if needed)
        self.rating_preferences = {}

    def get_feedback(self, rating):
        # Simulate user feedback based on song rating
        # Higher rating has a higher chance of being liked
        if rating >= 5.0:
            return True  # Simulate a "like" for songs with a rating of 5 or more
        else:
            return False  # Simulate a "dislike" for songs with a rating below 5

    def update_preferences(self, actors, liked):
        # Update user preferences based on actors (if you want to track preferences by actors)
        if actors not in self.rating_preferences:
            self.rating_preferences[actors] = 0.5  # Start with neutral preference

        if liked:
            self.rating_preferences[actors] = min(1.0, self.rating_preferences[actors] + 0.1)  # Increase preference
        else:
            self.rating_preferences[actors] = max(0.0, self.rating_preferences[actors] - 0.1)  # Decrease preference

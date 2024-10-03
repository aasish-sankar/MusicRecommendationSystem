# Tamil Song Recommendation System

## Overview
A personalized Tamil song recommendation system that utilizes user feedback and a multi-armed bandit approach to dynamically suggest songs based on user preferences.

## Features
- **Actor-based Recommendations:** Get song recommendations based on preferred actors.
- **User Feedback Loop:** Users can provide feedback on song recommendations, improving future suggestions.
- **Multi-Armed Bandit Approach:** Utilizes a multi-armed bandit algorithm to optimize song recommendations based on user feedback.

## Tech Stack
- **Python:** Programming language used for development.
- **Pandas:** Library for data manipulation and analysis.
- **CSV:** Used for storing song data.

## Getting Started

### Prerequisites
- Python 3.x
- Required Python packages:
  - pandas

### Input
- Enter actor name in Tamil for music recommendations.
- Uses dataset with songs until 2020

### Output

Available columns: ['movie', 'year', 'music', 'actors', 'movie_url', 'movie_image', 'movie_name_tamil', 'movie_name_eng', 'song_title', 'song_url', 'song_music', 'song_lyrics', 'song_singers', 'song_fulllyrics', 'song_rating']

Enter your preferred actor: விஜய்

Recommendation 1: En Deivathukke (என் தெய்வத்துக்கே) from Sivakasi (சிவகாசி) (Actors: விஜய், அசின், பிரகாஷ் ராஜ்) User feedback: Disliked

Recommendation 2: Kaathalae Kaathalae (காதலே காதலே) from 96 (96) (Actors: விஜய் சேதுபதி, த்ரிஷா கிருஷ்ணன், க ri ரி ஜி கிஷன்) User feedback: Disliked

Recommendation 3: Ennavale Ennavale (என்னவளே என்னவளே) from Ninaithen Vandhai (நினைத்தேன் வந்தாய்) (Actors: விஜய், ரம்பா, தேவயானி) User feedback: Liked

Recommendation 4: Oh My God (ஓ மை காட்) from Sangathamizhan (சங்கத்தமிழன்) (Actors: விஜய் சேதுபதி, ராஷி கண்ணா, நிவேதா பெதுராஜ், சூரி) User feedback: Liked

Recommendation 5: Pogatha Yennavittu (நீ போகாதே என்ன விட்டு) from Vikram Vedha (விக்ரம் வேதா) (Actors: ஆர். மாதவன், விஜய் சேதுபதி, வரலக்ஷ்மி சரத்குமார், ஷ்ரத்தா ஸ்ரீநாத், கதிர்) User feedback: Disliked

Recommendation 6: Lealakku Lealakku (லேலக்கு லேலக்கு) from Aadhi (ஆதி) (Actors: விஜய், த்ரிஷா கிருஷ்ணன்) User feedback: Liked

Recommendation 7: Rekkai Mulaiththen (ரெக்கை முளைத்தேன்) from Sundarapandian (சுந்தரபாண்டியன்) (Actors: எம். சசிகுமார், லட்சுமி மேனன், விஜய் சேதுபதி, சூரி) User feedback: Liked

Recommendation 8: Mannavanae Mannavanae (மன்னவனே மன்னவனே) from Puli (புலி) (Actors: விஜய், பிரபு, சுதீப் ஸ்ரீதேவி, ஸ்ருதி ஹாசன்) User feedback: Liked

Recommendation 9: Oh My God (ஓ மை காட்) from Sangathamizhan (சங்கத்தமிழன்) (Actors: விஜய் சேதுபதி, ராஷி கண்ணா, நிவேதா பெதுராஜ், சூரி) User feedback: Liked

Recommendation 10: Achchacho Punnagai (அச்சச்சோ புன்னகை) from Shahjahan (ஷாஜகான்) (Actors: விஜய், ரிச்சா பல்லோட், விவேக்) User feedback: Disliked

Total Rewards (Liked Songs): 6/10

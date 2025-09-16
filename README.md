🌦️ Weather App (Django)
-------------------------------------
A simple weather application built with Django, OpenWeather API, and Google Custom Search API.
Users can search for a city and view current weather conditions with a dynamic background image that matches the location.

✨ Features
-------------------------------
🔍 Search weather by city name

🌡️ Displays temperature, description, and weather icon

🖼️ Background image fetched dynamically using Google Custom Search API

🛡️ Default fallback image when city is not found or API fails

📅 Shows today’s date

❌ Error handling with user-friendly message

🛠️ Tech Stack
------------------------------------------
Backend: Django (Python)

APIs:

OpenWeather API
 → Weather data

Google Custom Search API
 → Background images

Frontend: HTML, CSS (frosted glass UI)



⚡ Setup Instructions
--------------------------------
1. Clone the repository
-----------------------------
git clone https://github.com/your-username/weather-app.git
cd weather-app

2 Create virtual environment & install dependencies
-------------------------------------------------------
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
pip install -r requirements.txt

3. Set environment variables
---------------------------------------------
Create a .env file in the root folder and add your keys:

OPENWEATHER_API_KEY=your_openweather_api_key
GOOGLE_API_KEY=your_google_api_key
SEARCH_ENGINE_ID=your_search_engine_id


Update views.py to read keys from .env.

4. Run migrations
-------------------------------
python manage.py migrate

5. Start the server
-------------------------------
python manage.py runserver


Visit 👉 http://127.0.0.1:8000

📸 Screenshots
--------------------------




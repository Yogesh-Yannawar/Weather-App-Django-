from django.shortcuts import render
import requests
from django.contrib import messages
import datetime

def index(request):
    if 'city' in request.POST:
        city = request.POST['city']
    else:
        city = 'indore'

    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid=bb9b3f3692cca58cbde934d58075d50c'
    PARAMS = {'units': 'metric'}
    day = datetime.date.today()

    API_KEY = 'AIzaSyAKIZmKJ2_vmUAGj6bjw7ZfWsCI9bUYhVY'
    SEARCH_ENGINE_ID = 'b576efd5031474fa5'

    query = city + " 1920x1080"
    page = 1
    start = (page - 1) * 10 + 1
    searchType = 'image'

    city_url = f'https://www.googleapis.com/customsearch/v1?key={API_KEY}&cx={SEARCH_ENGINE_ID}&q={query}&start={start}&searchType={searchType}&imgSize=xlarge'

    # Default fallback image
    fallback_img = "https://images.unsplash.com/photo-1502082553048-f009c37129b9"

    try:
        res = requests.get(city_url).json()
        search_items = res.get('items')
        image_url = search_items[1]['link'] if search_items else fallback_img

        data = requests.get(url, PARAMS).json()
        description = data['weather'][0]['description']
        icon = data['weather'][0]['icon']
        temp = data['main']['temp']

        return render(request, 'index.html', context={
            'description': description,
            'icon': icon,
            'temp': temp,
            'day': day,
            'city': city,
            'image_url': image_url
        })

    except Exception:
        messages.error(request, 'Search City information is not available, showing Indore weather')
        return render(request, 'index.html', context={
            'description': 'clear sky',
            'icon': '01d',
            'temp': 25,
            'day': day,
            'city': 'indore',
            'image_url': fallback_img,  # always provide this
            'exception': True
        })

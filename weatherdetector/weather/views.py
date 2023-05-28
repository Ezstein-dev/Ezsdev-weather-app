from django.shortcuts import render
import json
import urllib.request

# Create your views here.
def index(request):
    if request.method == 'POST':
        city  = request.POST['city']
        api_key = "4bfb7300e9f670716aeea462d34553e9" # replace with your OpenWeatherMap API key

        try:
            url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
            response = urllib.request.urlopen(url).read()
            json_data = json.loads(response)
        except urllib.error.HTTPError as e:
            print(f"HTTP Error {e.code}: {e.reason}")
        data = {
            "country_code": str(json_data['sys']['country']),
            "coordinate": str(json_data['coord']['lon']) + ' ' + str(json_data['coord']['lat']),
            "temperature": str(json_data['main']['temp'])+'k /'+f"{int(json_data['main']['temp']) - 273}"+"oC" ,
            "pressure": str(json_data['main']['pressure']),
            "humidity": str(json_data['main']['humidity']),
        }
    else:
        city = ""
        data = {}
    return render(request, 'index.html', {'city': city, 'data': data})
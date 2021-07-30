import requests


def stripSpace(word, char):
	word = word.replace(" ", char)

	return word

def getClimet(city):

	city = stripSpace(city, "+")

	response = requests.get(f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid=7e43286642d7564fd34746470da1219a")

	j_response = response.json()

	weather = j_response["weather"]

	mainWeather = weather[0]

	return mainWeather["main"]

import requests


def stripSpace(word, char):
	word = word.replace(" ", char)

	return word

def getClimet(city, city2 = None):

	if city2:
		city = city + city2

	response = requests.get(f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid=7e43286642d7564fd34746470da1219a")

	j_response = response.json()

	coord = j_response["coord"]

	weather = j_response["weather"]

	mainWeather = weather[0]

	returnes = [mainWeather["main"], coord]

	return returnes[0], returnes[1]


print(getClimet("Mano"))

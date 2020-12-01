import requests
from flask import Flask, render_template, request
from calculate import kelvin_to_fahr
import os

app = Flask(__name__)
api_key = os.environ.get('OPENWEATHER_API_KEY')
print('api_key:', api_key)

@app.route('/temperature', methods=['POST'])
def temperature():
	if 'zip' in request.form:
		zipcode = request.form['zip']
		r = requests.get(f'http://api.openweathermap.org/data/2.5/weather?zip={zipcode},us&appid={api_key}').json()
		return render_template('temperature.html', temp=f"{kelvin_to_fahr(r):.1f}")
	
	elif 'city' in request.form and 'state' in request.form:
		city = request.form['city']
		state = request.form['state']
		r = requests.get(f'http://api.openweathermap.org/data/2.5/weather?q={city},{state}&appid={api_key}').json()
		return render_template('temperature.html', temp=f"{kelvin_to_fahr(r):.1f}")

@app.route('/')
def index():
	return render_template('index.html')


if __name__ == '__main__':
	app.run()
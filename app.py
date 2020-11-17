import requests
from flask import Flask, render_template, request
from calculate import kelvin_to_fahr
# How we call to APIs and other URLs

app = Flask(__name__)
api_key = 'a641de02f55d14465d55e5fd6edb7506'

@app.route('/temperature', methods=['POST'])
def temperature():
	if 'zip' in request.form:
		zipcode = request.form['zip']
		r = requests.get(f'http://api.openweathermap.org/data/2.5/weather?zip={zipcode},us&appid={api_key}')
		json_object = r.json()
		temp_k = float(json_object['main']['temp'])
		temp_f = (temp_k - 273.15) * 1.8 + 32
		return render_template('temperature.html', temp=f"{temp_f:.1f}")
	
	elif 'city' in request.form and 'state' in request.form:
		city = request.form['city']
		state = request.form['state']
		r = requests.get(f'http://api.openweathermap.org/data/2.5/weather?q={city},{state}&appid={api_key}').json()
		# return r
		return render_template('temperature.html', temp=f"{kelvin_to_fahr(r):.1f}")

@app.route('/')
def index():
	return render_template('index.html')


if __name__ == '__main__':
	app.run()
import requests
from flask import Flask, render_template, request
# How we call to APIs and other URLs

app = Flask(__name__)

@app.route('/temperature', methods=['POST'])
def temperature():
	zipcode = request.form['zip']
	r = requests.get(f'http://api.openweathermap.org/data/2.5/weather?zip={zipcode},us&appid=a641de02f55d14465d55e5fd6edb7506')
	json_object = r.json()
	temp_k = float(json_object['main']['temp'])
	temp_f = (temp_k - 273.15) * 1.8 + 32
	return render_template('temperature.html', temp=f"{temp_f:.1f}")

@app.route('/')
def index():
	return render_template('index.html')


if __name__ == '__main__':
	app.run()
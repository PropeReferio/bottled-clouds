def kelvin_to_fahr(json):
	return (float(json['main']['temp']) - 273.15) * 1.8 + 32
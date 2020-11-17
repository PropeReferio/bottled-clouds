def kelvin_to_fahr(json):
	# temp_k = float(json_object['main']['temp'])
	# temp_f = (temp_k - 273.15) * 1.8 + 32
	return (float(json['main']['temp']) - 273.15) * 1.8 + 32
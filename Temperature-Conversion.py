def temperature_conversion(temp, scale_from, scale_to):
    if scale_from == 'Fahrenheit' and scale_to == 'Celsius':
        return (temp - 32) * 5/9
    elif scale_from == 'Fahrenheit' and scale_to == 'Kelvin':
        return (temp - 32) * 5/9 + 273.15
    elif scale_from == 'Celsius' and scale_to == 'Fahrenheit':
        return (temp * 9/5) + 32
    elif scale_from == 'Celsius' and scale_to == 'Kelvin':
        return temp + 273.15
    elif scale_from == 'Kelvin' and scale_to == 'Fahrenheit':
        return (temp - 273.15) * 9/5 + 32
    elif scale_from == 'Kelvin' and scale_to == 'Celsius':
        return temp - 273.15
    else:
        return 'Invalid scale'
    
print(temperature_conversion(98.6, 'Fahrenheit', 'Celsius'))
print(temperature_conversion(329.7, 'Kelvin', 'Fahrenheit'))
print(temperature_conversion(-60.9, 'Celsius', 'Kelvin'))

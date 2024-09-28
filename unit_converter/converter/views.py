# converter/views.py
from django.shortcuts import render

# Diccionarios con las conversiones, se hace así para poder agregar más unidades a futuro.
CONVERSION_FACTORS_LENGTH = {
    'meter': 1,
    'kilometer': 1000,
}
CONVERSION_FACTORS_WEIGHT = {
    'gram': 1,
    'kilogram': 1000,
}


def length_conversion(request):
    context = {}

    if request.method == 'POST':
        # Obtenemos los valores del formulario
        value = float(request.POST.get('value'))
        from_unit = request.POST.get('from_unit')
        to_unit = request.POST.get('to_unit')

        # Convertir de la unidad origen a metros
        value_in_meters = value * CONVERSION_FACTORS_LENGTH[from_unit]

        # Convertir de metros a la unidad destino
        converted_value = value_in_meters / CONVERSION_FACTORS_LENGTH[to_unit]

        context = {
            'converted_value': converted_value,
            'from_unit': from_unit,
            'to_unit': to_unit,
            'value': value,
        }

    return render(request, 'converter/length.html', context)

def weight_conversion(request):
    context = {}
    if request.method == 'POST':
        value = float(request.POST.get('value'))
        from_unit = request.POST.get('from_unit')
        to_unit = request.POST.get('to_unit')

        # Convertir de la unidad origen a gramos
        value_in_meters = value * CONVERSION_FACTORS_WEIGHT[from_unit]

        # Convertir de gramos a la unidad destino
        converted_value = value_in_meters / CONVERSION_FACTORS_WEIGHT[to_unit]

        context = {
            'converted_value': converted_value,
            'from_unit': from_unit,
            'to_unit': to_unit,
            'value': value,
        }
    return render(request, 'converter/weight.html', context)

def temperature_conversion(request):
    context = {}

    if request.method == 'POST':
        value = float(request.POST.get('value'))
        from_unit = request.POST.get('from_unit')
        to_unit = request.POST.get('to_unit')

        if from_unit == 'celsius':
            if to_unit == 'fahrenheit':
                converted_value = (value * 9/5) + 32
            elif to_unit == 'kelvin':
                converted_value = value + 273.15
            else:
                converted_value = value

        elif from_unit == 'fahrenheit':
            if to_unit == 'celsius':
                converted_value = (value - 32) * 5/9
            elif to_unit == 'kelvin':
                converted_value = (value - 32) * 5/9 + 273.15
            else:
                converted_value = value

        elif from_unit == 'kelvin':
            if to_unit == 'celsius':
                converted_value = value - 273.15
            elif to_unit == 'fahrenheit':
                converted_value = (value - 273.15) * 9/5 + 32
            else:
                converted_value = value

        context = {
            'converted_value': converted_value,
            'from_unit': from_unit,
            'to_unit': to_unit,
            'value': value,
        }

    return render(request, 'converter/temperature.html', context)

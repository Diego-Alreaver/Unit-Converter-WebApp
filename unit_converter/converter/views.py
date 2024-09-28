# converter/views.py
from django.shortcuts import render

# Diccionario con las conversiones a metros
CONVERSION_FACTORS_LENGTH = {
    'meter': 1,
    'kilometer': 1000,
}
CONVERSION_FACTORS_WEIGHT = {
    'gram': 1,
    'kilogram': 1000,
}
CONVERSION_FACTORS_TEMPERATURE = {
    'meter': 1,
    'kilometer': 1000,
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
    if request.method == 'POST':
        # Lógica para convertir temperaturas
        context = {'converted_value': "Resultado de temperatura"}
    else:
        context = {}
    return render(request, 'converter/temperature.html', context)

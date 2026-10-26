# Working With Dictionaries
from pyscript import display, document


def countries_capital(e):
    document.getElementById('output').innerHTML = ' '
    user_input = document.getElementById('input1').value.capitalize().strip()

    countries = {
    'Madagascar': 'Antananarivo',
    'Mongolia': 'Ulanbaatar',
    'Egypt': 'Cairo',
    'Philippines':'Manila',
    'USA': 'Washinton D.C.',
    'Denmark': 'Copenhagen',
    'Chile': 'Santiago'
    }

    message = countries.get(user_input, f'Sorry, {user_input} is not in the list')
    display(message, target = 'output')
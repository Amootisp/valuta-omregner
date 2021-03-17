import PySimpleGUI as sg                        # Part 1 - The import
import xml.etree.ElementTree as ET
import requests

url = 'https://www.nationalbanken.dk/_vti_bin/DN/DataService.svc/CurrencyRatesXML?lang=da'
r = requests.get(url, allow_redirects=True)

open('CurrencyRatesXML.xml', 'wb').write(r.content)

country_codes = []
country_names = []
rates = []

root_node = ET.parse('CurrencyRatesXML.xml').getroot()

for tag in root_node.findall('dailyrates/currency'):
    # Get the value from the attribute 'name'
    country_code = tag.attrib['code']
    country_name = tag.attrib['desc']
    rate = tag.attrib['rate']
    country_codes.append(country_code)
    country_names.append(country_name)
    rates.append(rate)
    

# Define the window's contents
layout = [  [sg.Combo([country_codes[0], country_codes[1], country_codes[2], country_codes[3], country_codes[4], country_codes[5], country_codes[6], country_codes[7], country_codes[8], country_codes[9], country_codes[10], country_codes[11], country_codes[12], country_codes[13], country_codes[14], country_codes[15], country_codes[16], country_codes[17], country_codes[18], country_codes[19], country_codes[20], country_codes[21], country_codes[22], country_codes[23], country_codes[24], country_codes[25], country_codes[26], country_codes[27], country_codes[28], country_codes[29], country_codes[30], country_codes[31], country_codes[32]], enable_events=True, key='code'),
            sg.Combo([country_codes[0], country_codes[1], country_codes[2], country_codes[3], country_codes[4], country_codes[5], country_codes[6], country_codes[7], country_codes[8], country_codes[9], country_codes[10], country_codes[11], country_codes[12], country_codes[13], country_codes[14], country_codes[15], country_codes[16], country_codes[17], country_codes[18], country_codes[19], country_codes[20], country_codes[21], country_codes[22], country_codes[23], country_codes[24], country_codes[25], country_codes[26], country_codes[27], country_codes[28], country_codes[29], country_codes[30], country_codes[31], country_codes[32]], enable_events=True, key='combo')],     # Part 2 - The Layout
            [sg.Input('Skriv tal ellers crash', key='input')],
            [sg.Text('My layout', key='-TEXT-')],
            [sg.Button('Ok')] ]

# Create the window
window = sg.Window('Valuta omregner', layout)      # Part 3 - Window Defintion

# Display and interact with the Window
while True:
    event, values = window.Read()
    if event is None or event == 'Exit':
        break

    if event == 'Ok':
        combo = values['combo']  # use the combo key
        code = values['code']
        num1 = country_codes.index(code)
        num2 = country_codes.index(combo)
        print(num1)
        print(num2)
        convert1 = rates[int(num1)]
        convert2 = rates[int(num2)]
        calnum1 = convert1.replace(',','.')
        calnum2 = convert2.replace(',','.')
        print(calnum1)
        print(calnum2)
        print((float(calnum1) / 100) * (100 / float(calnum2)))
        window['-TEXT-'].update((float(calnum1) / 100) * (100 / float(calnum2)) * float(values['input']))
        

# Finish up by removing from the screen
window.close()    
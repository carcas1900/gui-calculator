import PySimpleGUI as sg

#global variables
num1 = None 
operator = ''
num2 = None
expression = ''

#Helper function to do math
def calculate(num1, operator, num2):
    if operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        return num1 // num2
    else:
        return num1 + num2

#Set up the window
layout = [[sg.Text('', key = '-OUT-')],
          [sg.Button('1'), sg.Button('2'), sg.Button('3'), sg.Button('4'), sg.Button('5'), sg.Button('6'), sg.Button('7'), sg.Button('8'), sg.Button('9'), sg.Button('0'), sg.Button('+'), sg.Button('-'), sg.Button('*'), sg.Button('/'), sg.Button('='), sg.Button('Clear'), sg.Exit()]]

window = sg.Window('Calculator', layout)

while True:
    event, values = window.read()
    print(event, values, expression, num1, operator, num2)
    if event == sg.WIN_CLOSED or event =='Exit':
        break
    elif event == 'Clear':
        num1 = None
        operator = ''
        num2 = None
        expression = ''
        window['-OUT-'].update(expression)
    elif event == '+' or event == '-' or event == '*' or event == '/':
        num1 = int(expression)
        operator = str(event)
        expression += event
        window['-OUT-'].update(expression)
    elif event == '=':
        num2 = int(expression.split(operator)[1])
        expression = str(calculate(num1, operator, num2))
        window['-OUT-'].update(expression)
        num1 = None
        operator = ''
        num2 = None
        expression = ''
    else:
        expression += event
        window['-OUT-'].update(expression)

window.close()

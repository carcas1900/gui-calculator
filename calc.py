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
        return num1 / num2
    else:
        return num1 + num2

#Helper function to reset global variables
def fullReset():
    num1 = None
    operator = ''
    num2 = None
    expression = ''

#Set up the window
layout = [[sg.Text('', key = '-OUT-')],
          [sg.Button('1'), sg.Button('2'), sg.Button('+'), sg.Button('Clear'), sg.Exit()]]

window = sg.Window('Calculator', layout)

while True:
    event, values = window.read()
    print(event, values, expression)
    if event == sg.WIN_CLOSED or event =='Exit':
        break
    elif event == 'Clear':
        fullReset()
        window['-OUT-'].update(expression)
    elif event == '+':
        expression = calculate(int(expression), '+', 2)
        window['-OUT-'].update(str(expression))
    else:
        expression += event
        window['-OUT-'].update(expression)

window.close()

import PySimpleGUI as sg
import math
"""
Can calculate the combination of grades for a certain GPA
calculate the gpa from given grades

"""

sg.theme('DarkAmber')   # Add a touch of color
# All the stuff inside your window.
layout = [  [sg.Text('GPA of first class'), sg.InputText(k='-GPA1-')],
            [sg.Text('GPA of second class'), sg.InputText(k='-GPA2-')],
            [sg.Text('GPA of third class'), sg.InputText(k='-GPA3-')],
            [sg.Text('GPA of fourth class'), sg.InputText(k='-GPA4-')],
            [sg.Text('GPA of fifth class'), sg.InputText(k='-GPA5-')],
            [sg.Button('Ok',enable_events=True, k='-CALCGPA-'), sg.Button('Cancel')] ]

# Create the Window
def calc_gpa(sum):
    return float(sum/5)

window = sg.Window('Window Title', layout)
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
        break
    if event == '-CALCGPA-':
        gpa = float(values['-GPA1-'])+float(values['-GPA2-'])+float(values['-GPA3-'])+float(values['-GPA4-'])+float(values['-GPA5-'])
        g=float(calc_gpa(float(gpa)))
        print('Average GPA: %.2f'%g)
    

window.close()
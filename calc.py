import PySimpleGUI as sg
import math
import random
"""
Can calculate a random combination of grades for a certain minimum GPA
e.g

class 1: A-
class 2: A
class 3: B+


calculate the gpa from given grades
clear button

How much improvement needed for a certain grade

"""

sg.theme('DarkAmber')   # Add a touch of color
# All the stuff inside your window.
layout = [  [sg.Button('GPA Scale',enable_events=True, k='-GPASCALE-')],
            [sg.Text('GPA 1'), sg.InputText(k='-GPA1-',size=(4,5))],
            [sg.Text('GPA 2'), sg.InputText(k='-GPA2-',size=(4,5))],
            [sg.Text('GPA 3'), sg.InputText(k='-GPA3-',size=(4,5))],
            [sg.Text('GPA 4'), sg.InputText(k='-GPA4-',size=(4,5))],
            [sg.Text('GPA 5'), sg.InputText(k='-GPA5-',size=(4,5))],
            [sg.Button('Calculate',enable_events=True, k='-CALCGPA-')],
            [sg.Text('Target GPA'), sg.InputText(k='-TGPA-',size=(4,5))],
            [sg.Text('# Classes'), sg.InputText(k='-#TGPA-',size=(3,5))],
            [sg.Button('Find',enable_events=True, k='-FINDGRADE-')],
            [sg.Text('Target GPA'), sg.InputText(k='-TGPA2-',size=(4,5))],
            [sg.Text('Current GPA'), sg.InputText(k='-CGPA-',size=(4,5))],
            [sg.Button('Improvement',enable_events=True, k='-FINDIMPROVEMENT-')],
            [sg.Button('Clear',enable_events=True, k='-CLEAR-')],
            [sg.Button('Exit')]  ]

# Create the Window
def calc_gpa(sum,num):
    if num!=0:
        return float(sum/num)
    else:
        return 0
#### GPA calculation functions
# Trys to check for a float in the input and checks if the input value is true
def check_float(input):
    try:
        check_valid(float(input))
        return True
    except ValueError:
        return False

def check_valid(value):
    if value <0 or value > 4:
        sg.popup_error('Invalid input: '+str(value), title='Error')

def convert_l_to_gpa(value):
    if value=='A' or value=='A+':
        return 4.0
    elif value=='A-':
        return 3.7
    elif value == 'B+':
        return 3.3
    elif value == 'B':
        return 3.0
    elif value == 'B-':
        return 2.7
    elif value == 'C+':
        return 2.3
    elif value == 'C':
        return 2.0
    elif value == 'C-':
        return 1.7
    elif value == 'D+':
        return 1.3
    elif value == 'D':
        return 1.0
    elif value == 'F':
        return 0.0
    else:
        sg.popup_error('Invalid input: '+str(value), title='Error')
        return None
    
##### Find combination functions
#check for positive int
def check_int_comb(input):
    try:
        if int(input) > 0:
            return True
        else:
            sg.popup_error('Invalid input: '+str(input), title='Error')
            return False
    except ValueError:
        sg.popup_error('Invalid input: '+str(input), title='Error')
        return False    

def find_comb(target_gpa,num_courses):
    grading_scale = {'A': 4.0, 'A-':3.7,'B+':3.3, 'B': 3.0,'B-':2.7,'C+':2.3, 'C': 2.0, 'C-':1.7, 'D+':1.3, 'D': 1.0, 'F': 0.0}

    #Initialize a list storing random grades
    random_grades = []

    # Generate random grades until the GPA is above the target
    """
    while len(random_grades) == 0 or sum(random_grades) / len(random_grades) < target_gpa:
        random_grades = [grading_scale[random.choice(list(grading_scale))] for _ in range(num_courses)]
    """
    while True:
        random_grades = [random.choice(list(grading_scale.values())) for _ in range(num_courses)]
        average_gpa = sum(random_grades) / num_courses

        if average_gpa >= target_gpa:
            break

    output=""
    class_num=1
    for grade in random_grades:
        output+='Class'+str(class_num)+': ' +str(convert_to_letter(grade)) + '\n'
        class_num+=1
    sg.popup_ok_cancel(output,  title="GPA Scale")

def convert_to_letter(gpa):
    grading_scale = {4.0: 'A', 3.7: 'A-', 3.3: 'B+', 3.0: 'B', 2.7: 'B-', 2.3: 'C+', 2.0: 'C', 1.7: 'C-', 1.3: 'D+', 1.0: 'D', 0.0: 'F'}
    #letter_grade = min(grading_scale, key=lambda x: abs(x - gpa))
    return grading_scale[gpa]

#### Find improvement functions
def find_improvement(target_gpa,current_gpa):
    required_gpa=round((target_gpa*2)-current_gpa,2)
    if required_gpa>4:
        sg.popup_error('Your target GPA of '+str(target_gpa)+' is impossible for your current GPA of '+str(current_gpa), title='Error')
    else:
        sg.popup_ok_cancel('You require a GPA of '+str(required_gpa)+' to reach your target',  title="GPA Scale")




#### Window building
window = sg.Window('GPA Calculator', layout)
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
        break
    if event == '-CLEAR-':
        for key in ['-GPA1-', '-GPA2-', '-GPA3-', '-GPA4-', '-GPA5-', '-TGPA-', '-#TGPA-', '-TGPA2-', '-CGPA-']:
            window[key].update('')
    if event == '-GPASCALE-':
        sg.popup_ok_cancel("A+ = 4.00", "A = 4.00", "A- = 3.70", "B+ = 3.30", "B = 3.00", "B- = 2.70", "C+ = 2.30", "C = 2.00", "C- = 1.70", "D+ = 1.30", "D = 1.00", "F = 0.00",  title="GPA Scale")
    if event == '-FINDIMPROVEMENT-':
         if check_float(values['-TGPA2-']) and check_float(values['-CGPA-']):
             find_improvement(float(values['-TGPA2-']),float(values['-CGPA-']))
    if event == '-FINDGRADE-':
        # if the values are valid
        if values['-TGPA-']!='' and values['-#TGPA-']!='':
            if check_float(values['-TGPA-']) and check_int_comb(values['-#TGPA-']):
                find_comb(float(values['-TGPA-']),int(values['-#TGPA-']))
        else:
            sg.popup_error('Both Target GPA and # Classes must be filled!', title='Error')
    # Calculate GPA Event
    if event == '-CALCGPA-':
        num_gpa=0
        gpa1=gpa2=gpa3=gpa4=gpa5=0

        if values['-GPA1-']!='':
            num_gpa+=1
            if check_float(values['-GPA1-'])==True:
                gpa1= float(values['-GPA1-'])
            else:
                if convert_l_to_gpa(values['-GPA1-']) is not None:
                    gpa1=convert_l_to_gpa(values['-GPA1-'])
        if values['-GPA2-']!='':
            num_gpa+=1
            if check_float(values['-GPA2-'])==True:
                gpa2=float(values['-GPA2-'])
            else:
                if convert_l_to_gpa(values['-GPA2-']) is not None:
                    gpa2=convert_l_to_gpa(values['-GPA2-'])
        if values['-GPA3-']!='':
            num_gpa+=1
            if check_float(values['-GPA3-']):
                gpa3=float(values['-GPA3-'])
            else:
                if convert_l_to_gpa(values['-GPA3-']) is not None:
                    gpa3=convert_l_to_gpa(values['-GPA3-'])
        if values['-GPA4-']!='':
            num_gpa+=1
            if check_float(values['-GPA4-']):
                gpa4=float(values['-GPA4-'])
            else:
                if convert_l_to_gpa(values['-GPA4-']) is not None:
                    gpa4=convert_l_to_gpa(values['-GPA4-'])
        if values['-GPA5-']!='':
            num_gpa+=1
            if check_float(values['-GPA5-']):
                gpa5=float(values['-GPA5-'])
            else:
                if convert_l_to_gpa(values['-GPA5-']) is not None:
                    gpa5=convert_l_to_gpa(values['-GPA5-'])

        gpa = gpa1+gpa2+gpa3+gpa4+gpa5
        g=calc_gpa(float(gpa),num_gpa)
        print('Average GPA: %.2f'%g)
    

window.close()
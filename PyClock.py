from time import localtime, strftime, sleep
from os import system, name
import random
from sys import argv

def clear(): 
    if name == 'nt': 
        _ = system('cls') 
    else: 
        _ = system('clear')

# list0 = [' ▄▄▄▄▄▄▄ ', '█  ▄    █', '█ █ █   █', '█ █ █   █', '█ █▄█   █', '█       █', '█▄▄▄▄▄▄▄█']
# list1 = ['    ▄▄▄▄ ', '   █    █', '    █   █', '    █   █', '    █   █', '    █   █', '    █▄▄▄█']
# list2 = [' ▄▄▄▄▄▄▄ ', '█       █', '█▄▄▄▄   █', ' ▄▄▄▄█  █', '█ ▄▄▄▄▄▄█', '█ █▄▄▄▄▄ ', '█▄▄▄▄▄▄▄█']
# list3 = [' ▄▄▄▄▄▄▄ ', '█       █', '█▄▄▄    █', ' ▄▄▄█   █', '█▄▄▄    █', ' ▄▄▄█   █', '█▄▄▄▄▄▄▄█']
# list4 = [' ▄   ▄▄▄ ', '█ █ █   █', '█ █▄█   █', '█       █', '█▄▄▄    █', '    █   █', '    █▄▄▄█']
# list5 = [' ▄▄▄▄▄▄▄ ', '█       █', '█   ▄▄▄▄█', '█  █▄▄▄▄ ', '█▄▄▄▄▄  █', ' ▄▄▄▄▄█ █', '█▄▄▄▄▄▄▄█']
# list6 = [' ▄▄▄     ', '█   █    ', '█   █▄▄▄ ', '█    ▄  █', '█   █ █ █', '█   █▄█ █', '█▄▄▄▄▄▄▄█']
# list7 = [' ▄▄▄▄▄▄▄ ', '█       █', '█▄▄▄    █', '    █   █', '    █   █', '    █   █', '    █▄▄▄█']
# list8 = ['  ▄▄▄▄▄  ', ' █  ▄  █ ', ' █ █▄█ █ ', '█   ▄   █', '█  █ █  █', '█  █▄█  █', '█▄▄▄▄▄▄▄█']
# list9 = [' ▄▄▄▄▄▄▄ ', '█  ▄    █', '█ █ █   █', '█ █▄█   █', '█▄▄▄    █', '    █   █', '    █▄▄▄█']
# listcolon = ['      ', ' ▄▄▄  ', '█   █ ', '█▄▄▄█ ', ' ▄▄▄  ', '█   █ ', '█▄▄▄█ ']

list0 = ['   ██████ ', '  ███   ██', '  ████  ██', '  ██ ██ ██', '  ██  ████', '  ██   ███', '   ██████ ']
list1 = ['      ██  ', '    ████  ', '      ██  ', '      ██  ', '      ██  ', '      ██  ', '    ██████']
list2 = ['   ██████ ', '  ██    ██', '        ██', '   ██████ ', '  ██      ', '  ██      ', '  ████████']
list3 = ['   ██████ ', '  ██    ██', '        ██', '    █████ ', '        ██', '  ██    ██', '   ██████ ']
list4 = ['  ██    ██', '  ██    ██', '  ██    ██', '  ████████', '        ██', '        ██', '        ██']
list5 = ['  ███████ ', '  ██      ', '  ██      ', '  ███████ ', '        ██', '  ██    ██', '   ██████ ']
list6 = ['   ██████ ', '  ██    ██', '  ██      ', '  ███████ ', '  ██    ██', '  ██    ██', '   ██████ ']
list7 = ['  ████████', '       ██ ', '      ██  ', '     ██   ', '    ██    ', '   ██     ', '  ██      ']
list8 = ['   ██████ ', '  ██    ██', '  ██    ██', '   ██████ ', '  ██    ██', '  ██    ██', '   ██████ ']
list9 = ['   ██████ ', '  ██    ██', '  ██    ██', '   ███████', '        ██', '  ██    ██', '   ██████ ']
listcolon = ['    ', '    ', '  ██', '    ', '    ', '  ██', '    ']

dict0 = {'0':list0,'1':list1,'2':list2,'3':list3,'4':list4,'5':list5,'6':list6,'7':list7,'8':list8,'9':list9,':':listcolon}

def split(string):
    return list(string)

clear()

choice1text = '''Choose your color mode:
1: White (default)
2: Solid Colors
3: Per-line Colors
4: 'Crazy Colors'
5: Fixed Color
Blank: <Random Choice>
Make your selection: '''

choice2text = '''Choose refresh rate (1-30)
(leave blank to randomize between 1-30)'''

global fps
global choice1
global choice2

choice1 = 0
choice2 = 0

if len(argv) > 1:
    choice1 = int(argv[1])
    if len(str(choice1)) == 0 or int(choice1) < 1 or int(choice1) > 5:
        choice1 = int(random.randint(1,5))
    if len(argv) > 2:
        choice2 = int(argv[2])
        if len(str(choice2)) == 0 or int(choice2) < 1 or int(choice2) > 30:
            choice2 = int(random.randint(1,30))
        fps = float(1/choice2)
else:
    choice1 = 0
    try:
        choice1 = int(input(choice1text))
    except:
        choice1 = int(random.randint(1,5))
    if len(str(choice1)) == 0 or int(choice1) < 1 or int(choice1) > 5:
        choice1 = int(random.randint(1,5))
    clear()
    if choice1 == 5 or choice1 == 1:
        choice2 = 5
    else:
        choice2 = 0
        try:
            choice2 = int(input(choice2text))
        except:
            choice2 = int(random.randint(1,30))
        if len(str(choice2)) == 0 or int(choice2) < 1 or int(choice2) > 30:
            choice2 = int(random.randint(1,30))
    fps = float(1/choice2)
    clear()
    print(choice1)
    print('')
    print(f'1/{choice2}={round(fps, 4)}')
    sleep(3)

number = random.randrange(31,37)

while True:
    USERINPUT = strftime("%H:%M:%S", localtime())

    USERLIST = list(split(USERINPUT))

    USEROUTPUT = []


    for char in USERLIST:
        if char in dict0:
            USEROUTPUT.append(dict0[char])
        else:
            USEROUTPUT.append('')
    

   
    clear()
    print(' ')
    if choice1 == 5:
        for i in range(7):
            function0 = ' '+' '.join([f"\033[1;{number};40m{x[i]}" for x in USEROUTPUT])
            print(function0)
    elif choice1 == 4:
        for i in range(7):
            function0 = ' '+' '.join([f"\033[1;{random.randrange(31,38)};40m{x[i]}" for x in USEROUTPUT])
            print(function0)
    elif choice1 == 3:
        for i in range(7):
            function0 = ' '+' '.join([x[i] for x in USEROUTPUT])
            print(f"\033[1;{random.randrange(31,38)};40m{function0}")
    elif choice1 == 2:
        number = random.randrange(31,38)
        for i in range(7):
            function0 = ' '+' '.join([x[i] for x in USEROUTPUT])
            print(f"\033[1;{number};40m{function0}")
    else:
        for i in range(7):
            function0 = ' '+' '.join([x[i] for x in USEROUTPUT])
            print(function0)
    sleep(fps)
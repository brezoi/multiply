#!/usr/bin/python
import random

#https://www.geeksforgeeks.org/print-colors-python-terminal/
class colors: 
    reset='\033[0m'
    bold='\033[01m'
    underline='\033[04m'
    class fg: 
        red='\033[31m'
        green='\033[32m'
        cyan='\033[36m'
        yellow='\033[93m'

prompts=["Please provide the solution.","Know the answer?", "How smart are you?",'''This one's easy!''',"Go forward and multiply!", "Need a hint? Sorry.", "Answer please.", "You know this one.", "Can it get any easier?","Give it a shot.", '''What's the answer?''',"No calculators!","Watch out for zero. 0 eats everything.",'''Isn't this fun!''']

correct=["Good job!","Nice work!",'''That's correct!''',"You are awesome!","How smart!","Great work!","A multiplication star!","No problem for you!"]

incorrect=["Wrong","Oops","Ouch","Whoops","No Silly","Better luck next time","Incorrect","You should have known","Time to sudy"]

hit=0 
miss=0

def score():
    print(colors.reset)
    s=((hit/(hit+miss))*100)
    si=int(s)

    if si in range(90,101):
        g='A'
    elif si in range(80,91):
        g='B'
    elif si in range(70,81):
        g='C'
    elif si in range(60,71):
        g='D'
    else:
        g='F'
    print("Grade: %s Hit: %i Miss: %i Percentage: %f" % (g,hit,miss,s))

intro=" Welcome to Multiply!!! Good luck! "
use='''To play: answer the question, then at the prompt:
Type n for the next question. Type r for rundown mode.
Type a number between 0 and 12 to see that number's table.
Enter any other key to quit.'''
print()
print(colors.fg.yellow,colors.bold,colors.underline)
print(intro.center(75,'*'))
print(colors.reset)
print()
print(colors.fg.cyan,colors.bold)
print(use)

choice="n"

while choice == "n":
    print()
    print(colors.reset)
    print(colors.fg.yellow,colors.bold)
    prompt=prompts[random.randint(0,len(prompts)-1)]
    a = random.randint(0,12)
    b = random.randint(0,12)
    solution=a*b
    equation="%i X %i = "
    print(prompt)
    print(equation % (a,b), end='')
    i=input()
    try:
        j=int(i)
        if  j == solution:
            print(colors.fg.green,colors.bold)
            say=correct[random.randint(0,len(correct)-1)]
            print(say)
            hit = hit + 1
        else:
            print(colors.fg.red,colors.bold)
            say=incorrect[random.randint(0,len(incorrect)-1)]
            print("%s, the answer is %i X %i = %i" % (say,a,b,solution))
            miss = miss + 1
    except:
        print(colors.fg.red,colors.bold)
        print("That's not a number!")
        print("%i X %i = %i" % (a,b,solution))
        miss = miss + 1
    
    print()
    print(colors.fg.yellow,colors.bold)
    choice=input(":")
    if choice == "n":
        continue
    if choice == "r":
        y=0
        x=random.randint(0,12)
        while y < 13:
            solution=x*y
            print(colors.fg.yellow,colors.bold)
            print("%i X %i =" % (x,y), end='')
            try:
                choice=input()
                if int(choice) != solution:
                    print(colors.fg.red,colors.bold)
                    print("Actually: %i x %i = %i" % (x,y,solution))
                    miss = miss + 1
                else:
                    hit = hit + 1
            except:
                print(colors.red.bold,colors.bold)
                print("That's not a number!")
                miss = miss + 1
            y=y+1
        choice='n'
    else:
        try: 
            if int(choice) in range(13):
                x=0
                print(colors.fg.cyan,colors.bold)
                while x < 13:
                    print("%s X %s = %s" % (choice,x,(int(choice)*int(x))))
                    x=x+1
                choice="n"
            else:
                score()
                exit()
                
        except:
            if choice != "n":
                score()
                exit()
            else:
                choice="n"
        

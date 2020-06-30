#!/usr/bin/python
import random

prompts=["Please provide the solution.","Know the answer?", "How smart are you?",'''This one's easy!''',"Go forward and multiply!", "Need a hint? Sorry.", "Answer please.", "You know this one.", "Can it get any easier?","Give it a shot.", '''What's the answer?''',"No calculators!","Watch out for zero. 0 eats everything.",'''Isn't this fun!''']

correct=["Good job!","Nice work!",'''That's correct!''',"You are awesome!","How smart!"]

incorrect=["Wrong","Oops","Ouch","Whoops","No Silly","Better luck next time","Incorrect","You should have known","Time to sudy"]

hit=0 
miss=0

def score():
    print("Hit: %i Miss %i Score %f" % (hit,miss,(hit/(hit+miss)*100)))

choice="n"

while choice == "n":
    print()
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
            say=correct[random.randint(0,len(correct)-1)]
            print(say)
            hit = hit + 1
        else:
            say=incorrect[random.randint(0,len(incorrect)-1)]
            print("%s, the answer is %i X %i = %i" % (say,a,b,solution))
            miss = miss + 1
    except:
        print("That's not a number!")
        print("%i X %i = %i" % (a,b,solution))
        miss = miss + 1
    
    print()
    print("Type n for next, r for rundown, a number 0 to 12, or any other key to quit...")
    choice=input()
    if choice == "n":
        continue
    if choice == "r":
        y=0
        x=random.randint(0,12)
        while y < 13:
            solution=x*y
            print("%i X %i =" % (x,y), end='')
            try:
                choice=input()
                if int(choice) != solution:
                    print("Actually: %i x %i = %i" % (x,y,solution))
                    miss = miss + 1
                else:
                    hit = hit + 1
            except:
                print("That's not a number!")
                miss = miss + 1
            y=y+1
        choice='n'
    else:
        try: 
            if int(choice) in range(13):
                x=0
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
        

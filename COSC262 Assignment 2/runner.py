import subprocess
from time import clock
'''A little python 3 program that allows you to run other python programs via
the command line and collect their output. 
I wrote this on a windows 7 machine so the command line arguments may have to be 
changed for other systems.

Note: all the programs and files MUST be in the same directory 

Be warned it could take a long time to run on a slower computer, so feel free to 
change which programs and files are run :) 
I'm not completely sure about where the timer should stop, but if it is stopped
a line earlier it gives ridiculously fast times, and any later seems pointless
as the program will have finished running 
'''
IN = ".dat"
COMPARE = ".out"
programs = ["giftwrap.py","grahamscan.py","amethod.py"]
prefix = ["A_","B_"]
Numbers = ["10","50","500","1000","3000","6000","9000","12000"]

for program in programs:
    for Type in prefix:
        for number in Numbers:
            runs = 4
            run = 0
            timeTaken = 0.0
            while run < runs:
                t = clock() #Start timer
                p1 = subprocess.Popen("python "+program+" "+Type+number+IN, stdout = subprocess.PIPE) # the command line argument
                temp = str(p1.stdout.readline().strip()) #collecting from stdout
                timeTaken += clock() - t # stop timer
                temp = temp[2:-1] #gets rid of the nasty "b'" at the front and "'" at the end
                fopen = open(Type+number+COMPARE)
                ans = fopen.readline().strip()
                run += 1
            timeTaken = timeTaken/runs
            if temp == ans:
                result = " Passed "
            else:
                result = " Failed "
            print(program,result,Type,number,"Time:",timeTaken)

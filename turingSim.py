##AUTHOR: GARRETT BECKER
import sys
from time import sleep
import os
turingString = input("Enter a string of the form w#w \n")
turingString = turingString.strip()
tape = []
m=0
strLen = len(turingString)
if(strLen==1):
    if(turingString[0] == '#'):
        print("Acceptable:", turingString[0])
        sys.exit()
##first i'm going to write all the char to a list for easy access
for head in range(strLen):
    tape.append(turingString[head]) #write the string to the tape
print("Original string",tape, "\n")

done = False
head=0

while(done!=True):
    safe = tape[head] #save the element we're looking at
    tape[head] = 'x' #mark that index as x
    while(tape[head]!= '#'): #loop until we find a # and move a spot over
        head= head + 1
    head= head + 1 #move spot over
    if(tape[head] == 'x'): #loop through all the x's
        head= head + 1
        while(tape[head]== 'x'):
            head= head + 1
    if(safe == tape[head]): #check the element we saved with the element we're looking at
        tape[head] = 'x'
        while(tape[head]!= '#'): #Loop back through everything to get to the next element
            head= head - 1
        while(tape[head]!= 'x'):
            head= head - 1
        head = head + 1#move one over
    else:
        print("not equal")
        sys.exit()
    count =0
    #Checks if we're done
    for q in range(strLen):
        if(tape[q]=='x'):
            count = count+1
        if(count==strLen-1):
            print("equal")
            print(tape)
            sys.exit()










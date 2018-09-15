#  File: Handicap.py
#  Description: Calculates a bowler's average and handicap after three games.
#  Student's Name: Amanda Tran  
#  Student's UT EID: at35245
#  Course Name: CS 303E 
#  Unique Number: 51205
#
#  Date Created: 9/14/2018
#  Date Last Modified: 9/14/2018

def main():
    ##Initial Variables
    x = int(input ("Enter Game 1: "))
    y = int(input ("Enter Game 2: "))
    z = int(input ("Enter Game 3: "))

    #Equations Given
    average = int((x + y + z) / 3)
    handicap = int((200 - average) * 0.80)
    
    #End
    print()
    print("The bowler's average is: ", average)
    print("The bowler's handicap is: ", handicap)

main()
    

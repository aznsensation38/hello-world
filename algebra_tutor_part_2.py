import random

def greeting():
    print("\n###########################################")
    print("#     Beginning Algebra Tutor Program     #")
    print("#                 Part 2                  #")
    print("#             by: Tim Brunner             #")
    print("###########################################\n")

def generate_problem(value):
    m = random.randint(1,5)
    x = random.randint(1,10)
    b = random.randint(1,10)
    y = m * x + b
    if int(value) == 1:
        answer = y
        display_problem(value,y,m,x,b)
    elif int(value) == 2:
        answer = m
        display_problem(value,y,m,x,b)
    elif int(value) == 3:
        answer = b
        display_problem(value,y,m,x,b)
    
    return(answer)

def display_problem(value,y,m,x,b):
    if int(value) == 1:
        print("y = " + str(m) + " * " + str(x) + " + " + str(b))
    elif int(value) == 2:
        print(str(y) + " = " + "m * " + str(x) + " + " + str(b))
    elif int(value) == 3:
        print("3)      " + str(y) + " = " + str(m) + " * " + str(x) + " + b")
    elif int(value) == 4:
        return()
    
    return()

def verify(correct_answer,user_answer):
    if correct_answer == user_answer:
        print("Correct")
    elif correct_answer != user_answer:
        print("Incorrect --- The Correct answer is " + str(correct_answer))
    return()

def get_selection():
    selection= int(input("Select: "))
    while (int(selection) < 1 or int(selection) > 4):
        selection = input("Please select a Valid response: 1 , 2 , 3 , 4:  ")
    return(selection)

def run_main():
    greeting()
    # Creates variable 'selection' to open the loop. As long as "selection" 
    # does not equal 4, or resume_program = "n" , program will stay open
    selection = 0
    while (selection != 4):
        print("\nWhich problem would you like to solve?\n\n1) Solve for Y\n2) Solve for M\n3) Solve for B\n4) (Exit Program) \n")
        selection = get_selection()
        if selection == 4:
            break
        answer_key = str(generate_problem(selection))
        print("What is the answer?")
        user_answer = input()
        verify(answer_key, user_answer)   
        resume_program = (input("\nWhould you like to solve another? y/n: "))
        if resume_program == "n":
            break
        elif resume_program == "y":
            selection = 0
           
    return()

##    ///////////////////////////////////////
##    /////Start Part--2 Below This Line/////

run_main()
print("\nProgram Terminate.....Goodbye!")

##    ///////////////////////////////////////
##    /////Start Part--3 Below This Line/////

#def calculate_score(count_correct,count_wrong):
#    score = round(float(count_correct) / float(count_total), 2)
#    return(score)

#def hint(count_wrong):
#    if count_wrong == 3:
#        print("\nHint:\n\nTry to get the variable by itself.\n\nY = M * X + B   =====>   M = ( Y - B ) / X\nor\nY = M * X + B   =====>   B = M * X - Y")


import random

# ///// Part 2 Python Complete ///// Need JAVA Conversion

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
    print("What is the answer?")
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

def verify(outcome,answer_key, user_answer):
    if answer_key == user_answer:
        outcome = outcome + 1
        
    elif answer_key != user_answer:
        outcome = outcome + 1
    return(outcome)

def outcome_statement(answer_key, user_answer):
    if answer_key == user_answer:
        print("Correct")
        value = 1
    elif answer_key != user_answer:
        print("Incorrect --- The Correct answer is " + str(answer_key))
        value = 0
    return(value)

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
    score = str(run_main_program(selection))
    return(score)

def run_main_program(selection):
    # create variables to track total, correct, and wrong attempts -- Use integers 
    # to calculate grade and determine if a Hint should be given.
    correct_answers = 0
    total_attempts = 0
    wrong_answers = 0
    # selection variable set to 0 to start loop
    while (selection != 4):
        print("\nWhich problem would you like to solve?\n\n1) Solve for Y\n2) Solve for M\n3) Solve for B\n4) (Exit Program) \n")
        selection = get_selection()
        # selection = 4 is the Exit command
        if selection == 4:
            break
        answer_key = str(generate_problem(selection))
        user_answer = input()
        total_attempts = total_attempts + 1
        outcome = outcome_statement(answer_key, user_answer)
        if outcome == 1:
            correct_answers = correct_answers + 1
        elif outcome != 1:
            wrong_answers = wrong_answers + 1
        # Test prints
        print("CORRECT:" + str(correct_answers))
        print("WRONG:" + str(wrong_answers))
        print("TOTAL:" + str(total_attempts))
        # Test prints
        if wrong_answers == 3:
            give_hint() # Add Hint Text function call
        resume_program = (input("\nWhould you like to solve another? y/n: "))
        if resume_program == "n":
            break
        elif resume_program == "y":
            selection = 0
                
    get_grade(correct_answers,total_attempts)
    return()

def get_grade(correct_answers,total_attempts):
    grade = round((correct_answers / total_attempts), 2) * 100
    print("Your grade is " + str(grade) + "%")
    return()

def give_hint():
    print("\nHint:\n\nTry to get the variable by itself.\n\nY = M * X + B   =====>   M = ( Y - B ) / X\nor\nY = M * X + B   =====>   B = M * X - Y")
    return()

##    ///////////////////////////////////////
##    /////Start Part--3 Below This Line/////

run_main()
print("\nProgram Terminate.....Goodbye!")





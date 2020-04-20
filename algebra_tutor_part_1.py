import random
# // import java_algebra_tutor_python_file

# // PART 1 - Python complete # CONVERT TO JAVA

def greeting():
    print("\n###########################################")
    print("#     Beginning Algebra Tutor Program     #")
    print("#                 Part 1                  #")
    print("#             by: Tim Brunner             #")
    print("###########################################\n")

def problem_outcome(y, answer):
    
    count = 0
    while count != 1:# while loop added for full credit
        # Print statement depending on users answer compared to correct answer.
        if answer == y:
            out_come = str("Correct!")
        elif answer != y:
            out_come = str("Sorry, that is incorrect. The correct answer is " + str(y))
        # count added to end loop
        count = count + 1

    return(out_come)    

# Generate random numbers between 1 and 15

m = random.randint(1,15)
x = random.randint(1,15)
b = random.randint(1,15)
y = m * x + b               # Uses values m, x, and b to calculate value of y

greeting()
print("\n\t\ty = " + str(m) + " * " + str(x) + " + " + str(b) + "\n")
answer = int(input("\t\ty = "))
print("\n\t\t" + problem_outcome(y, answer) + "\n")

# ///// Program End ///// #



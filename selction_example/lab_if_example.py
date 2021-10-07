"""
#
# File    :.py
# created  :$ {Date} $ {Time}
# Author   : Neha Tripathi
# Version  :v1.0.0
# Licencing :
# Description :if
#
"""

if __name__ == '__main__':
    grade = input ("Enter a grade")

    grade = int(grade) # type cast - change the string grade to an integer and put it back in
    # the same variable!

    module_1 = "python"

    if grade >= 70 and module_1 == "Python":
        print('You have earned a Distinction!')

    elif grade >=60:
        print("You have earned a M.1")
    elif grade >=50:
        print("You have earned a M.2")
    elif grade>=40:
        print("You have Passed")
    else:
        print("Please try again")

'''
decision making statements

if 
else
elif
nested if
'''
'''
syntax:
if condition:
    statements
 else:
    statements   
'''
 
if True:
    print("if")
elif False:
    print("elif")
else:
    print("else")

#nested if
if True:
    print("outer if")
    if False:
        print("inner if")
    else:
        print("inner else")
else:
    print("outer else")
# practical example
age=18
if age>18:
    print("you can vote")
elif age==18:
    print("you can vote buddy")
else:
    print("wait")
def grade(n): # n is an integer.
    if 100>=n>=90:
        return "A"
    elif n>=80:
        return "B"    
    elif n>=70:
        return "C"
    elif n>60:
        return "D"
    else: 
        return "F"            

x = 56
letter_grade = grade(x)
print(letter_grade)         
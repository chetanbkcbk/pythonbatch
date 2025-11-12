def get_grade(mark):
    if mark>=85:
        return "A"
    elif mark>=65:
        return "B"
    elif mark>=45:
        return "C"
    else:
        return "D"

print(get_grade(35))

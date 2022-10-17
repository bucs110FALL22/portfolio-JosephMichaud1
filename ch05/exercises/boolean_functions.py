def percentage_to_letter(score):
    if score >= 90:
        return True
    elif score >90 and score >= 70:
        return True
    elif score > 70 and score <=60:
        return True
    elif score > 60 and score <=50:
        return False
    else:
        return False

score = int(input("What is your score?: "))
print(percentage_to_letter(score))


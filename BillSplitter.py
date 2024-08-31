#enter in a dictionary of who paid for what on a trip, program outputs who is owed what

d = {"John":40,"Devon":0,"Eric":100,"Hayden":35}

def split(d):
    names,money = list(d.keys()),list(d.values())
    size = len(money)
    av = sum(money)/size
    owes = [0]*size
    for i in range(1,size):
        owes[i] = owes[i-1] + money[i-1] - av
    ret = []
    for i in range(1,size):
        if owes[i] > 0:
            ret.append(f"{names[i]} owes {names[i-1]} {owes[i]} dollars")
        elif owes[i] < 0:
            ret.append(f"{names[i-1]} owes {names[i]} {owes[i]*-1} dollars")
    return ret

        

print(split(d))

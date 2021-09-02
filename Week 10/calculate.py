def Sum(List):
    S = 0
    for x in List:
        S+=x
    return S
def Avg(List):
    Avg = Sum(List)/len(List)
    return Avg 
def Grade(Avg):
    if Avg>90:
        return 'S'
    elif Avg>80:
        return 'A'
    elif Avg>70:
        return 'B'
    elif Avg>60:
        return 'C'
    elif Avg>50:
        return 'D'
    else:
        return 'F'
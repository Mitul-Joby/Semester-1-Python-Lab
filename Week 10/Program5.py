L = ['C','o','m','p','u','t','e','r']

def concat(x):
    if x == len(L)-1:
        return True
    else:
        L[x+1] = L[x] + L[x+1]

List = [ L[i] for i in range(len(L)) if concat(i)]
print(List)
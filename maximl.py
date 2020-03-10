string=input()
def distinct(s):
    i, j = 0, 0
    I, J = 0, 0
    Empty_set = set([])
    while j < len(s):
        if s[j] in Empty_set:
            Empty_set.remove(s[i])
            i += 1
        else:
            Empty_set.add(s[j])
            j += 1
        if J - I < j - i:
            I, J = i, j
    return s[I:J]
print(len(distinct(string)))
    

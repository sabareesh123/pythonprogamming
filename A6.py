import sys, string, math

def IsIso(string1, string2):
    W = len(string1)
    n = len(string2)
    if W != n:
        return False
    marked = [False] * 256
    map = [-1] * 256
    for J in range(n):
        if map[ord(string1[J])] == -1:
            if marked[ord(string2[J])] == True:
                return False
            marked[ord(string2[J])] = True
            map[ord(string1[J])] = string2[J]
        elif map[ord(string1[J])] != string2[J]:
            return False
    return True

# Driver program
s1,s2 = input().split()
if IsIso(s1,s2) : print('yes')
else :            print('no')


def reverse_number(n):
    rev = 0
    while n>0:
        rev = rev *10 + n % 10
        n //= 10
    return rev 

def beautifuldays(i,j,k):
    count = 0
    for day in range (i,j + 1):
        rev_day = reverse_number(day)
        if abs(day - rev_day) % k ==0:
            count +=1
    return count

i, j, k = map(int, input("Enter i, j, k: ").split())
print(beautifuldays(i, j, k))
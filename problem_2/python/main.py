last = 1
sum = current = 2

while(current < 4000000):
    tmp = last + current
    if tmp % 2 == 0:
        sum += tmp

    last = current
    current = tmp

print(sum)

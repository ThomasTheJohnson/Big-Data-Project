list = [0,0,0,0,0]
print list
count = 0
while count < 10:
    list.append(count)
    list.pop(0)
    count += 1
    print list

numbers=(12, 75, 150, 180, 145, 525, 500)
for num in numbers:
    if numbers % 5 == 0:
        print(num)
    if numbers > 150:
        print(num)
    if numbers > 500 :
        break       

new_list = [2,4,6, 'California']

for element in new_list:
    try: 
        print(element/2)
    except:
        print("The Element is Not a Number")

n = 4
while n > 0:
    print(n)
    n = n-1
    if n == 2:
        break

print("message")
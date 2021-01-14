n = 10
print(n)

def func():
    global n 
    n = 15
    print(n)
func()
print(n)

stack=[]
def push():
    num=int(input("Please enter the number"))
    stack.append(num)
    print(stack)
def pop():
    if not stack:
        print("Stack is empty.")
    else:
        e=stack.pop()
        print("Remover element: ",)
        print(stack)
while True:
    inter=int(input("Enter your input 1.push 2.pop 3.quit"))
    if inter==1:
        push()
    elif inter == 2:
        pop()
    elif inter == 3:
        print("By seee you again")
        break
    else:
        print("Please enter proper input:")


todos =[]
while True :
    user_action = input("Type add or show or exit: ")

    match user_action:
        case 'add':
            todo = input("enter todo : ")
            todos.append(todo)
        case 'show':
            print(todos)
        case 'exit':
            break
print("byeee")
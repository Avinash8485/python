
while True :
    user_action = input("Type add or show or edit or complete or exit: ")

    match user_action:
        case 'add':
            todo = input("enter todo : ")+ "\n"
            file = open('todos.txt','r')
            todos = file.readlines()
            file.close()
            todos.append(todo)
            file = open("todos.txt",'w')
            file.writelines(todos)
            file.close()

        case 'show':
            file = open('todos.txt','r')
            todos = file.readlines()
            file.close()
            for index,item in enumerate(todos):
                row = f"{index+1}-{item}"
                print(row)
        case 'edit':
            number = int(input("Number of the todo to edit : "))
            number = number -1
            print(todos[number])
            new_todo = input("Enter old todo : ")
            todos[number] = new_todo
        
        case 'complete':
            number = int(input("Enter the index"))
            todos.pop(number)

        case 'exit':
            break
print("byeee")
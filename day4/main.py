todos =['book','bag','notes']
while True :
    user_action = input("Type add or show or edit or exit: ")

    match user_action:
        case 'add':
            todo = input("enter todo : ")
            todos.append(todo)
        case 'show':
            print(todos)
        case 'edit':
            number = int(input("Number of the todo to edit : "))
            number = number -1
            print(todos[number])
            new_todo = input("Enter old todo : ")
            todos[number] = new_todo

        case 'exit':
            break
print("byeee")


filename =["1.raw.txt","2.report.txt","3.present.txt"]

for item in filename:
    item = item.replace('.','-',1)
    print(item)

print(filename)
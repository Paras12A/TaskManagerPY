while True:
    
    tasksArray = []
    userInput = ""
    def listTask():
        for element in tasksArray:
            print(element)
            
    def addTask():
        newTask = input("Which task you want to add : ")
        tasksArray.append(newTask)


    def menu():
        print("Enter 1 to List task")
        print("Enter 2 to Add a task")
        print("Enter q to quit")
        userInput = input("")
        return userInput

    userInput = menu()
       
    if userInput == "1":
        listTask()
    elif userInput == "2":
        addTask()
    elif userInput == "q":
        break
    else:
        print("Invalid choice")


tasksArray = []

while True:
    
    userInput = ""
    
    def listTask():
        for element in tasksArray:
            print("- ", element)
            print(" ")
            
    def addTask():
        newTask = input("Which task you want to add : ")
        tasksArray.append(newTask)


    def menu():
        print("Enter 1 to List task")
        print("Enter 2 to Add a task")
        print("Enter 3 to Check how many task do you have")
        print("Enter 4 to Delete a task")
        print("Enter q to quit")
        userInput = input("")
        return userInput
    
    def numberOfTask():
        print("You have", len(tasksArray), " tasks")

    def deleteTask():
        deletedTask = input("Which task you want to delete : ")
        tasksArray.remove(deletedTask)
        print(deletedTask, " has been deleted")
    
    userInput = menu()
       
    if userInput == "1":
        listTask()
    elif userInput == "2":
        addTask()
    elif userInput == "3":
        numberOfTask()
    elif userInput == "4":
        deleteTask()
    elif userInput == "q":
        break
    else:
        print("Invalid choice")

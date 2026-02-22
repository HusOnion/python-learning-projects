import json

def main():
    is_running = True
    ToDoList = []
    while is_running:
        
        print("******************************")
        print("          TO DO LIST          ")
        print("1.show list")
        print("2.add tasks")
        print("3.remove tasks")
        print("4.Export to a json file")
        print("5.Load from a json file")
        print("6.Mark as checked")
        print("7.Exit")
        user = input_handling(1,7)

        if user == 1:
            show_list(ToDoList)
        
        elif user == 2:
            ToDoList.append(input("Enter the task: "))
        
        elif user == 3:
            remove_task(ToDoList)
        
        elif user == 4:
            Ename = input("Enter the name of the file: ")
            with open(f"{Ename}.json", "w") as file:
                json.dump(ToDoList, file, indent=4)
            print(f"Exported to {Ename}.json successfully!")
        
        elif user == 5:
            try:
                name = input("Enter the name of the file: ")
                with open(f"{name}.json","r") as file:
                    ToDoList = json.load(file)
                print(f"Imported from {name}.json successfully!")
            except FileNotFoundError:
                print(f"There isn't a file named {name}.json")
                ToDoList = []
        
        elif user == 6:
            check_box(ToDoList)

        else:
            is_running = False

        
        
        
        


def show_list(ToDoList):
    print("TO DO:")
    for item in ToDoList:
        print(f"{ToDoList.index(item) + 1}. {item}")

    


def remove_task(ToDoList):
    if len(ToDoList) == 0:
        print("There is no tasks to remove")
    else:
        x = input_handling(1,len(ToDoList))
        x -= 1
        ToDoList.pop(x)
        print("DONE")
    

def check_box(ToDoList):
    if len(ToDoList) == 0:
        print("There is no tasks to check")
    else:
        x = input_handling(1, len(ToDoList))
        if "✅" not in ToDoList[x - 1]:
            ToDoList[x - 1] += " ✅"
            print("Task marked as done!")
        else:
            print("Task already completed.")



def input_handling(n1,n2):
    while True:
        x = input(f"Enter your choice({n1},{n2}): ")
        try:
            x = int(x)
            if x > n2 or x < n1:
                print("Exceeded the range")
                continue
            break
        except ValueError:
            print("Value Error, Enter a number")
    
    return x

        
        

if __name__ == "__main__":
    main()


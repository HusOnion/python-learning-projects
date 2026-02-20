def main():
    is_running = True
    ToDoList = []
    while is_running:
        
        print("******************************")
        print("          TO DO LIST          ")
        print("1.show list")
        print("2.add tasks")
        print("3.remove tasks")
        print("4.Exit")
        user = input_handling(1,4)

        if user == 1:
            show_list(ToDoList)
        elif user == 2:
            ToDoList.append(input("Enter the task: "))
        elif user == 3:
            remove_task(ToDoList)
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
        ToDoList.remove(ToDoList[x])
        print("DONE")
    





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

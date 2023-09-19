def add(task , option ):
    if option == 'Add'.lower():
        user_task = input("Enter the Task: ")
        task.append(user_task)
        return task
def task_remove(task, option):
    if option == 'remove'.lower():
        user_task = input("Enter the Task to Remove: ")
        task.remove(user_task)
        return task
def leave(option):
    if option == 'quit':
        return quit()

def main():
    task = []
    quit = True
    while quit:
        print("Add - Adding Task")
        print("Remove - To Remove the task")
        print("quit - To Quit")
        print("")
        user_option = input("Enter the option: ").lower()
        add(task, user_option)
        task_remove(task , user_option)
        leave(user_option)
        print("")
        print(task)
        print("")
main()

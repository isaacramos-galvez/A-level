task_list = ["hello", "goodbye"]

def complete_task():
    task_remove = input("What task do you want to remove?")
    task_list.remove(task_remove)
    print(task_list)

complete_task()
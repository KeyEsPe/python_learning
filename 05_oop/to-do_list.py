class Task:

    def __init__(self, task_description, task_status):
        self.task_description = task_description
        self.task_status = task_status

    def __str__(self):      # Here we added str method, which will return string with only description of a task, not the full representation. 
        return f"{self.task_description}"

class ToDoList:

    def __init__(self):
        self.todo_list = []        # We have to first create an empty list, where we can later add the tasks. 

    def add_new_task(self, new_task):
        self.todo_list.append(new_task)
        print(f"New task: {new_task} added.")
    
    def change_status(self, task_description, new_status):
        for task in self.todo_list:          # We have to use a loop to go thru all the tasks and find maching for changing the status. 
            if task.task_description == task_description:    # Using task.task_description we refer to the task description from the Task class. 
                task.task_status = new_status   # And we changing the task status to the new status. 
        print(f"Status of task {task_description} changed to {new_status}")

    def show_all_tasks(self):  # The goal is to separate done and undone tasks, so we create two empty lists to store them in. 
        self.done_tasks = []
        self.pending_tasks = []

        for task in self.todo_list:
            if task.task_status == "done":
                self.done_tasks.append(task)
            else:
                self.pending_tasks.append(task)
        
        print("Done tasks:")
        for task in self.done_tasks:
            print(f" - {task.task_description}")

        print("\nPending tasks:")
        for task in self.pending_tasks:
            print(f" - {task.task_description}")


my_list = ToDoList()      # We create my_list so ocject of our ToDoList class, so we can store the tasks in it. 

task1 = Task("Learn Python", "pending")    # Creatining new tasks, which are objects of Task class. 
task2 = Task("Buy groceries", "pending")
task3 = Task("Walk the dog", "done")

my_list.add_new_task(task1)   # We using method to add tasks to our list. 
my_list.add_new_task(task2)
my_list.add_new_task(task3)

my_list.show_all_tasks()   # We using method to print out all of the tasks befre modification. 

my_list.change_status("Learn Python", "done")      # Method for changing status of the task. 

my_list.show_all_tasks() 





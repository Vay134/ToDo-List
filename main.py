import os

class main_app():
    def __init__(self):
        self.get_data()
        self.print_info()

    def print_info(self):
        print("==================================================")
        print("                    To-Do list                    ")
        print("==================================================")
        return

    def get_data(self):
        if not os.path.exists("save_data.txt"): # Creates a new save file if it does not exist
            with open("save_data.txt", "w+") as f:
                f.write("0\n") # Max Task ID
                f.write("COMPLETED: \n")
                f.write("UNFINISHED: \n")

        with open("save_data.txt", "r") as f:
            lines = f.readlines()
            self.max_id = lines.pop(0).strip()
            self.completed = [id.strip() for id in (lines.pop(0).split(":")[1]).split(",") if id.strip().isdigit()]
            self.unfinished = [id.strip() for id in (lines.pop(0).split(":")[1]).split(",") if id.strip().isdigit()]
            self.id_task = dict([map(str.strip,line.split(":", 1)) for line in lines 
                                 if line.split(":",1)[0].strip().isdigit()])
        return
    
    def update_save_file(self):
        with open("save_data.txt", "w") as f:
            f.write(self.max_id + "\n")
            f.write("COMPLETED: " + ", ".join(self.completed) + "\n")
            f.write("UNFINISHED: " + ", ".join(self.unfinished) + "\n")
            f.write("\n")
            f.write("\n".join([str(id) + ": " + self.id_task[str(id)] for id in sorted([int(id) for id in self.id_task.keys()])]))
        return
        
    def print_tasks(self, task_type: list):
        print("--------------------------------------------------\n")
        print("                 ", end = "")
        print("Unfinished Tasks" if task_type == self.unfinished else "Completed Tasks", end = "")
        print("                  ")
        print("[U]: Unfinished")
        print("[C]: Completed")
        print("The number to the the left of each task it its ID")
        print("--------------------------------------------------")

        if len(task_type) == 0:
            print("You currently have no {} tasks!".format("unfinished" if task_type is self.unfinished else "completed"))
        else:
            task_status = "[U]" if task_type is self.unfinished else "[C]"
            for task_ID in task_type:
                print(task_status, task_ID, '-', self.id_task[task_ID])
        
        print("--------------------------------------------------")
    
    def print_all_tasks(self):
        print("--------------------------------------------------\n")
        print("                    All Tasks                     ")
        print("[U]: Unfinished")
        print("[C]: Completed")
        print("The number to the the left of each task it its ID")
        print("--------------------------------------------------")

        if len(self.unfinished) + len(self.completed) == 0:
            print("You have not added any tasks!")
        else:
            for unfinished_task_ID in self.unfinished:
                print("[U]", unfinished_task_ID, '-', self.id_task[unfinished_task_ID])
            
            for completed_task_ID in self.completed:
                print("[C]", completed_task_ID, '-', self.id_task[completed_task_ID])
        
        print("--------------------------------------------------")
    
    def view_tasks(self):
        task_view_mapper = {"c": (lambda: self.print_tasks(self.completed)), 
                            "u": (lambda:self.print_tasks(self.unfinished)), 
                            "a": self.print_all_tasks}
        print("--------------------------------------------------")
        print("All tasks: a")
        print("Unfinished tasks: u")
        print("Completed tasks: c")
        print("Back: x")
        print("--------------------------------------------------")
        inp = input("Which tasks would you like to view? ")
        while inp.lower() not in task_view_mapper and inp.lower() != 'x':
            inp = input("Invalid input, please enter a/u/c/x: ")
        if inp.lower() == 'x':
            print("--------------------------------------------------")
            return
        task_view_mapper[inp]()
        return

    def update_task(self):
        
        return

    def add_task(self):
        print("--------------------------------------------------")
        new_task = input("What task would you like to add? ")
        while new_task == "":
            print("Task name cannot be empty!")
            new_task = input("What task would you like to add? ")
        self.id_task[self.max_id] = new_task
        self.unfinished.append(self.max_id)
        print("Added task " + self.max_id + ": " + new_task)
        print("--------------------------------------------------")
        self.max_id = str(int(self.max_id) + 1)

        self.update_save_file()
        return

    def edit_task(self):
        print("--------------------------------------------------")
        if len(self.unfinished) + len(self.completed) == 0:
            print("You have not added any tasks!")
            print("--------------------------------------------------")
            return
        
        for unfinished_task_ID in self.unfinished:
            print("[U]", unfinished_task_ID, '-', self.id_task[unfinished_task_ID])
        
        for completed_task_ID in self.completed:
            print("[C]", completed_task_ID, '-', self.id_task[completed_task_ID])
        print("--------------------------------------------------")
        print("Which task would you like to update? ")

        inp = input("Enter task ID (x to cancel): ")
        while inp not in self.id_task and inp.lower() != 'x':
            inp = input("Invalid input, please enter a valid ID: ")
        if inp.lower() == 'x':
            return
        print(("[U] " if inp in self.unfinished else "[C] ")+ inp, '-', self.id_task[inp])

        new_task = input("Enter new task name: ")
        while new_task == "":
            print("Task name cannot be empty!")
            new_task = input("Enter new task name: ")
        self.id_task[inp] = new_task
        
        print("--------------------------------------------------")

        self.update_save_file()
        print("Updated tasks!")
        print("--------------------------------------------------")
        return

    def delete_task(self):
        print("B")
        pass

    def get_action(self):
        actions = {"v": self.view_tasks, "u": self.update_task, "a": self.add_task, 
                   "e": self.edit_task, "d": self.delete_task}
        print("View tasks: v")
        print("Update a task's status: u")
        print("Add a task: a")
        print("Edit a task: e")
        print("Delete a task: d")
        print("Exit: x")
        print("--------------------------------------------------")
        inp = input("What would you like to do? ")
        while inp.lower() not in actions and inp.lower() != 'x':
            inp = input("Invalid input, please enter v/u/a/e/d/x: ")
        if inp.lower() == 'x':
            return True
        actions[inp]()
        return False

app = main_app()
end_program = False
while end_program == False:
    end_program = app.get_action()
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

        with open ("save_data.txt", "r") as f:
            lines = f.readlines()
            self.max_id = lines.pop(0)
            self.completed = [id.strip() for id in (lines.pop(0).split(":")[1]).split(",") if id.strip().isdigit()]
            self.unfinished = [id.strip() for id in (lines.pop(0).split(":")[1]).split(",") if id.strip().isdigit()]
            self.id_task = dict([map(str.strip,line.split(":", 1)) for line in lines 
                                 if line.split(":",1)[0].strip().isdigit()])
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
            for task_ID in task_type:
                print(task_ID, self.id_task[task_ID])
        
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
                print("[U]", unfinished_task_ID, self.id_task[unfinished_task_ID])
            
            for completed_task_ID in self.completed:
                print("[C]", completed_task_ID, self.id_task[completed_task_ID])
        
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
        print("B")
        pass

    def edit_task(self):
        print("B")
        pass

    def delete_task(self):
        print("B")
        pass

    def get_action(self):
        actions = {"v": self.view_tasks, "u": self.update_task, "e": self.edit_task, "d": self.delete_task}
        print("View tasks: v")
        print("Update a task: u")
        print("Edit a task: e")
        print("Delete a task: d")
        print("Exit: x")
        print("--------------------------------------------------")
        inp = input("What would you like to do? ")
        while inp.lower() not in actions and inp.lower() != 'x':
            inp = input("Invalid input, please enter v/u/e/d: ")
        if inp.lower() == 'x':
            return True
        actions[inp]()
        return False

app = main_app()
end_program = False
while end_program == False:
    end_program = app.get_action()
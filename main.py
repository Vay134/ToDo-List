import os

class main_app():
    def __init__(self):
        self.print_info()
        self.get_data()
        self.print_tasks(self.unfinished)
        self.print_all_tasks()

    def print_info(self):
        print("==================================================")
        print("                    To-Do list                    ")
        print("==================================================")
        return

    def get_data(self):
        if not os.path.exists("save_data.txt"): # Createsa new save file if it does not exist
            with open("save_data.txt", "w+") as f:
                f.write("0\n") # Max Task ID
                f.write("COMPLETED: \n")
                f.write("UNFINISHED: \n")

        with open ("save_data.txt", "r") as f:
            lines = f.readlines()
            self.max_id = lines.pop(0)
            self.completed = {id.strip() for id in (lines.pop(0).split(":")[1]).split(",")}
            self.unfinished = {id.strip() for id in (lines.pop(0).split(":")[1]).split(",")}
            self.id_task = dict([map(str.strip,line.split(":", 1)) for line in lines 
                                 if line.split(":",1)[0].strip().isdigit()])
        return

    def print_tasks(self, task_type: list):
        print("                 ", end = "")
        print("Unfinished Tasks" if task_type == self.unfinished else "Completed Tasks", end = "")
        print("                  ")
        print("--------------------------------------------------")
        print("[U]: Unfinished")
        print("[C]: Completed")
        print("The number to the the left of each task it its ID\n")

        for task_ID in task_type:
            print(task_ID, self.id_task[task_ID])
        
        print("--------------------------------------------------\n")
    
    def print_all_tasks(self):
        print("                    All Tasks                     ")
        print("[U]: Unfinished")
        print("[C]: Completed")

        print("The number to the the left of each task it its ID")
        print("--------------------------------------------------")

        for unfinished_task_ID in self.unfinished:
            print("[U]", unfinished_task_ID, self.id_task[unfinished_task_ID])
        
        for completed_task_ID in self.completed:
            print("[C]", completed_task_ID, self.id_task[completed_task_ID])
        
        print("--------------------------------------------------\n")
    
    def get_action(self):
        print("View tasks: v")
        print("Update a task: u")
        print("Edit a task: e")
        print("Delete a task: d")
        inp = input("What would you like to do? ")
        if inp.lower() not in ('v', 'u', 'e', 'd'):
            inp = input("Invalid input, please enter v/u/e/d: ")
        return inp
        

app = main_app()

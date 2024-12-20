import os

def print_info():
    print("==================================================")
    print("                    To-Do list                    ")
    print("==================================================\n")
    return

def get_data():
    if not os.path.exists("save_data.txt"): # Createsa new save file if it does not exist
        with open("save_data.txt", "w+") as f:
            f.write("0\n") # Max Task ID
            f.write("COMPLETED: \n")
            f.write("UNFINISHED: \n\n")

    with open ("save_data.txt", "w+") as f:
        


get_data()
print_info()
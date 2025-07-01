import json
import os
try:
    op = int(input("Choose an option:\n 1. Read data.json file\n 2. Create data.json file\n 3. Edit data.json File \n 4. Delete data.json file\n"))
    if op == 1:
        if os.path.exists("data.json"):
            with open("data.json", "r") as f:
                data = json.load(f)
                print(data)
                print("File read successfully!")
        else:
            print("No such file doesn't exist")
    elif op == 2:
        try:
            id_i = int(input("Enter your id: "))
            name_i = input("Enter your name: ").strip()
            age_i =  int(input("Enter your age: "))
            if not name_i:
                print("Name cannot be left empty")
            user = {"id": id_i, "name": name_i, "age": age_i}
            l = [user]
            with open("data.json", "x") as f:
                json.dump(l, f)
                print("File created successfully!")
        except FileExistsError:
            print("This file already exist. Trying editing instead.")
        except ValueError:
            print("Enter integer for id and age; Enter string for name.")
    elif op == 3:
        
            if os.path.exists("data.json"):
                try:
                    with open("data.json", "r") as f:
                        z = json.load(f)
                        id_i = int(input("Enter your id: "))
                        name_i = input("Enter your name: ").strip()
                        age_i =  int(input("Enter your age: "))
                        if not name_i:
                            print("Name cannot be left empty")
                        new_user = {"id": id_i, "name": name_i, "age": age_i}
                        
                        duplicate = any(d["id"]==id_i for d in z)
                        if duplicate:
                            print("This id already exist")
                        else:
                            z.append(new_user)
                            with open("data.json", "w") as f:
                                json.dump(z, f)
                                print("Entry edited successfully!")
                except ValueError:
                    print("Enter integer for id and age; Enter string for name.")
            else:
                print("This file doesn't exist, try creating it.")
    elif op == 4:
        if os.path.exists("data.json"):
            os.remove("data.json")
        else:
            print("This file doesn't exist")
except ValueError:
    print("Input a valid option in form of integer")



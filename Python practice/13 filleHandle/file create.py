import os
def create_file(name):
    try:
        os.mkdir(name)
    except FileExistsError:
        print("File already exists")
    except Exception as e:
        print(e)
        
create_file("data.txt")

    
    
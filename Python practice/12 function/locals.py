def display(name):
    age = 24
    print(f"{name} is {age} years old")
    # locals() return a dictionary of local symbol table
    print(f"Length of locals: {len(locals())}")
    # variable is exist or not
    check = locals()
    print(f"Age is exist: {check['age']}")
    print(f"Name is exist: {check['name']}")
    print(f"Length of locals: {len(check)}")
    print(f"Age is exist: {check.get('age')}")
    print(f"Name is exist: {check.get('name')}")
    print(f"Length of locals: {check.get('age')}")
    # variable is exist or not
    print(f"Age is exist: {'age' in check}")
    print(f"Name is exist: {'name' in check}")
display("Faruk")
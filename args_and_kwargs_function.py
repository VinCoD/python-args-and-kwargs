def args_and_kwargs_function(*args, **kwargs):

    for arg in args:
        print(arg)
    
    for key, value in kwargs.items():
        print(f"{key}: {value}")


args_and_kwargs_function("Alice", "Bob", "Charlie", "Vincent", name1="Alice", name2="Bob", name3="Liz")
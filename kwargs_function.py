def kwargs_function(**kwargs):
    print(type(kwargs))

    for key, value in kwargs.items():
        print(f"{key}: {value}")


kwargs_function(name1="Alice", name2="Bob", name3="Liz")
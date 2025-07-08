def insert_data_to_db(age: int,name: str):
    if type(age) == int and type(name) == str:
        print(age)
        print(name)
        print("data inserted.....")
    else:
        raise TypeError("Enter right data....")


insert_data_to_db("30","dvcsd")
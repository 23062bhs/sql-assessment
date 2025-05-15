#docstring- Jason Huang- GPU database application
#imports
import sqlite3

#constants and variables
DATABASE = "GPU.db"

#functions
def print_all_gpu():
    '''print all the GPUs nicely'''
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = "SELECT * from gpu;"
    cursor.execute(sql)
    results = cursor.fetchall()
    #loop thorugh all the results
    print(f"name                          price memory  speed year")
    for gpu in results:
        print(f"{gpu[1]:<30}{gpu[2]:<8}{gpu[3]:<6}{gpu[4]:<6}{gpu[5]:<6}")
    #loop finished here
    db.close() 



def print_all_gpu_by_price():
    '''print all the GPUs sorted by price'''
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = "SELECT * from gpu ORDER BY price DESC;"
    cursor.execute(sql)
    results = cursor.fetchall()
    #loop thorugh all the results
    print(f"name                          price memory  speed year")
    for gpu in results:
        print(f"{gpu[1]:<30}{gpu[2]:<8}{gpu[3]:<6}{gpu[4]:<6}{gpu[5]:<6}")
    #loop finished here
    db.close()



def print_all_gpu_by_memory():
    '''print all the GPUs sorted by memory'''
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = "SELECT * from gpu ORDER BY memory DESC;"
    cursor.execute(sql)
    results = cursor.fetchall()
    #loop thorugh all the results
    print(f"name                          price memory  speed year")
    for gpu in results:
        print(f"{gpu[1]:<30}{gpu[2]:<8}{gpu[3]:<6}{gpu[4]:<6}{gpu[5]:<6}")
    #loop finished here
    db.close()



def print_all_gpu_by_speed():
    '''print all the GPUs sorted by speed'''
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = "SELECT * from gpu ORDER BY speed DESC;"
    cursor.execute(sql)
    results = cursor.fetchall()
    #loop thorugh all the results
    print(f"name                          price memory  speed year")
    for gpu in results:
        print(f"{gpu[1]:<30}{gpu[2]:<8}{gpu[3]:<6}{gpu[4]:<6}{gpu[5]:<6}")
    #loop finished here
    db.close()



def print_all_gpu_by_year():
    '''print all the GPUs sorted by year released'''
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = "SELECT * from gpu ORDER BY year_released DESC;"
    cursor.execute(sql)
    results = cursor.fetchall()
    #loop thorugh all the results
    print(f"name                          price memory  speed year")
    for gpu in results:
        print(f"{gpu[1]:<30}{gpu[2]:<8}{gpu[3]:<6}{gpu[4]:<6}{gpu[5]:<6}")
    #loop finished here
    db.close()



def print_all_gpu_by_manufacturer():
    #loop finished 
    '''print all the GPUs sorted by manufacturer'''
    manufacturer_name = input("Which manufacturer? ")
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    if manufacturer_name.upper() == "NVIDIA":
        sql = "SELECT * from gpu WHERE manufacturer_id == '1';"
        cursor.execute(sql)
        results = cursor.fetchall()
        #loop thorugh all the results
        print(f"name                          price memory  speed year")
        for gpu in results:
            print(f"{gpu[1]:<30}{gpu[2]:<8}{gpu[3]:<6}{gpu[4]:<6}{gpu[5]:<6}")
    elif manufacturer_name.upper() == "AMD":
        sql = "SELECT * from gpu WHERE manufacturer_id == '2';"
        cursor.execute(sql)
        results = cursor.fetchall()
        #loop thorugh all the results
        print(f"name                          price memory  speed year")
        for gpu in results:
            print(f"{gpu[1]:<30}{gpu[2]:<8}{gpu[3]:<6}{gpu[4]:<6}{gpu[5]:<6}")
    else:
        print("That was not an option")
        
    db.close()



def add_gpu():
    name = input("GPU name: ")
    price = int(input("price (NZD): "))
    memory = int(input("memory (GB): "))
    speed = int(input("speed (MHz): "))
    year = int(input("year released: "))
    manufacturer = int(input("manufacturer ID (1 = NVIDIA, 2 = AMD): "))

    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = "INSERT INTO gpu (gpu_name, price, memory, speed, year_released, manufacturer_id) VALUES (?, ?, ?, ?, ?, ?);"
    cursor.execute(sql, (name, price, memory, speed, year, manufacturer))
    db.commit()
    db.close()



def delete_gpu():
    name = input("Enter the name of the GPU to delete: ")
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = "DELETE FROM gpu WHERE gpu_name = ?"
    cursor.execute(sql, (name,))
    db.commit()
    if cursor.rowcount > 0:
        print("GPU deleted")
    else:
        print("GPU not found")
    db.close()



#main code
while True:
    user_input = input(
"""
What would you like to do.
1.Print all GPUs
2.Print all GPUs sorted by price
3.Print all GPUs sorted by memory
4.Print all GPUs sorted by speed
5.Print all GPUs sorted by year released
6.Print all GPUs sorted by manufacturer
7.Add a new GPU
8.Delete a GPU
9.Exit

""")
    if user_input == "1":
        print_all_gpu()
    elif user_input == "2":
        print_all_gpu_by_price()
    elif user_input == "3":
        print_all_gpu_by_memory()
    elif user_input == "4":
        print_all_gpu_by_speed()
    elif user_input == "5":
        print_all_gpu_by_year()
    elif user_input == "6":
        print_all_gpu_by_manufacturer()
    elif user_input == "7":
        add_gpu()
    elif user_input == "8":
        delete_gpu()
    elif user_input == "9":
        break
    else:
        print("That was not an option")

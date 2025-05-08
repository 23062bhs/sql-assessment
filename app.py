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
    print(f"name                          price memory  speed year manufacturer_id")
    for gpu in results:
        print(f"{gpu[1]:<30}{gpu[2]:<8}{gpu[3]:<6}{gpu[4]:<6}{gpu[5]:<6}{gpu[6]:<6}")
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
    print(f"name                          price memory  speed year manufacturer_id")
    for gpu in results:
        print(f"{gpu[1]:<30}{gpu[2]:<8}{gpu[3]:<6}{gpu[4]:<6}{gpu[5]:<6}{gpu[6]:<6}")
    #loop finished here
    db.close()



#main code
while True:
    user_input = input(
"""
What would you like to do.
1.Print all GPUs
2.Print all GPUs sorted by price
3.Exit

""")
    if user_input == "1":
        print_all_gpu()
    elif user_input == "2":
        print_all_gpu_by_price()
    elif user_input == "3":
        break
    else:
        print("That was not an option\n")

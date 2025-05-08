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
    print("name                          price memory  speed year manufacturer_id")
    for gpu in results:
        print(f"{gpu[1]:<30}{gpu[2]:<8}{gpu[3]:<6}{gpu[4]:<6}{gpu[5]:<6}{gpu[6]:<6}")
    #loop finished here
    db.close()

#main code
print_all_gpu()
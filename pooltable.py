#Pool table app

import time
import datetime
import json
from datetime import date
today = date.today()
pool_tables = []
pool_tables_as_dict = []
localtime = time.asctime( time.localtime(time.time()) )
print ("Local current time :", localtime)




class Pooltable:
    def __init__(self,table_number):
        self.table_number = table_number
        self.occupied = False
        self.start_time= 0
        self.end_time = 0
        self.elapsed_time = 0
        self.float_start_time = time.time()
        self.float_end_time = time.time()
        self.use_count = 0
        self.total_use_time = 0
        self.revenue = 0

    def revenue_per_table(self):
        self.revenue = self.total_use_time * .5 



    def assign_table(self):
        #self.check_table() gets overridden so ignoring for now 
        self.occupied = True
        print("*******************************************")
        print(f"Table {self.table_number} is Now Assigned")
        print("*******************************************")
        now= datetime.datetime.now()    
        self.start_time= now.strftime("%H:%M:%S")
        self.float_start_time = time.time()#time.asctime( time.localtime(time.time()) )
        print(f"start time is {self.start_time}")
        #self.start_time = start_time
        

    def release_table(self):
        #self.check_table()# this is being overridden when in assign table 
        self.occupied = False
        print("*******************************************")
        print(f"Table {self.table_number} is Now Available")
        print("*******************************************")
        now= datetime.datetime.now()
        self.end_time = now.strftime("%H:%M:%S") #time.asctime( time.localtime(time.time()) )
        self.float_end_time = time.time()#time.asctime( time.localtime(time.time()) )
        print(f" Table free at {self.end_time}")
        self.time_occupied()
        self.total_use_time += self.elapsed_time
        self.use_count += 1
        self.revenue_per_table()


    

            

    def time_occupied(self):
        int_elapsed_time = (self.float_end_time - self.float_start_time)/60
        self.elapsed_time = round(int_elapsed_time) 
   
        print(f" Table {self.table_number} has been in use since {self.start_time} for {self.elapsed_time} Minutes")
        
    def as_string(self):
        return "\nTable #: {0}\nStart time: {1}\nEnd time: {2}\nTotal time: {3} minutes\nTimes used {4}\n\n" .format(self.table_number,self.start_time,self.end_time,self.total_use_time, self.use_count)

    def use_counter(self):
        self.time_occupied()


    
def check_table():# this is being overridden when in assign table forgetting about it for now
    try:
        for index in range(0, len(pool_tables)):
        
            table = pool_tables[index]
       
        table_id= int(input("Please input number of Table from list "))
        table = (pool_tables[table_id -1])
        if table.occupied == True: 
            print("*********************************")
            print("!!The table is already occupied!!")
            print("*********************************")
            show_menu()
    except ValueError:
        print("Enter a number") 
    except IndexError:
        print("Number out of range there are only 12 pool tables") 
            
            

def show_menu():
    print("*******************************")
    print("*******************************")
    print("press 1 to view  table status")
    print("press 2 to assign table ")
    print("press 3 to release table ")
    print("press 4 to view in use time ")
    print("press q ")        
    print("*******************************")
    print("*******************************")
              
def select_table_assign():
    try:
        for index in range(0, len(pool_tables)):
        
            table = pool_tables[index]
       
        table_id= int(input("Please input number of Table from list "))
        table = (pool_tables[table_id -1])
        #add the check function in here 
        if table.occupied == True:
            print("*********************************")
            print("!!The table is already occupied!!")
            print("*********************************")
            
    

        else :
            table.assign_table()
    except ValueError:
        print("Enter a number") 
    except IndexError:
        print("There are only 12 pool tables")
        
   

def select_table_release():
    for index in range(0, len(pool_tables)):
        
        table = pool_tables[index]
    try:  
        table_id= int(input("Please input number of Table from list "))
        table = (pool_tables[table_id -1])
        if table.occupied == False:
            print("*******************************")

            print ("!!That table is already Open!!")
            print("*******************************")

        else :
            table.release_table()
   
    except ValueError:
        print("Enter a number") 
    except IndexError:
        print("There are only 12 pool tables")
        
        

def view_table_status():
    for table in pool_tables:
        if table.occupied == False:
            print(f"Table Number {table.table_number} is Free")
        elif table.occupied == True:
            print(f"Table Number {table.table_number} is Occupied")

def view_table_status_free():
    for table in pool_tables:
        if table.occupied == False:
            print(f"Table Number {table.table_number} is Free")
        
    
def view_table_status_occupied():
    for table in pool_tables:
        
        
        if table.occupied == True:
            print(f"Table Number {table.table_number} is Occupied")
                        
def write_all_out():
    for table in pool_tables:
        print(f' Table {table.table_number} has been used {table.use_count} times for a total of {table.total_use_time} minutes')#if table.occupied == False:
       
        with open (f"{today}.txt","a") as file_object:
            #writes the table out to text file 
            file_object.write(table.as_string())
        
          


def view_update_in_use_time():
    for table in pool_tables:
        if table.occupied == True :
            table.float_end_time = time.time()
            table.time_occupied()


def clear_all_tables_release():
    for table in pool_tables:

        if table.occupied == True:
            table.release_table()
            print("*******************************")
            print ("closing all tables")
            print("*******************************")

def write_to_json():
    pool_tables_as_dict.append(table.__dict__)
    with open(f"{today}.json", "w") as file_object:
        json.dump(pool_tables_as_dict,file_object, indent=2)


menu_entry = " "
print("*******************************")
print("Initializing Pool Tables")
print("*******************************")

a= int(input("input number of tables"))+1

for index in range (1,a):
    table = Pooltable(index)
    pool_tables.append(table)
    pool_tables_as_dict.append(table.__dict__)

try:
    with open(f"{today}.json","r") as file_object:
        loaded_tables = json.load(file_object)
        for i in range(len(pool_tables)):
            pool_tables[i].occupied = loaded_tables[i]['occupied']
            pool_tables[i].start_time = loaded_tables[i]['start_time']
            pool_tables[i].float_start_time = loaded_tables[i]['float_start_time']
except:
    write_to_json()
    

while menu_entry != "q":
    show_menu()
    menu_entry = input("Please enter choice   ").lower()
    print("*******************************************")
    
    if menu_entry == "1":
        view_table_status()


    elif menu_entry == "2":
       
        view_table_status_free()
        select_table_assign()
        write_to_json()
     

    elif menu_entry == "3":
        view_table_status_occupied()
        select_table_release()
        view_table_status()
        write_to_json()
       
    elif menu_entry == "4":
        view_update_in_use_time()
    
    


clear_all_tables_release()
view_update_in_use_time()
#table.as_string()  
write_to_json()
write_all_out()      


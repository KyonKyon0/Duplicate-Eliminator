#Read file

import pandas as pd

#Time Import
import time
from datetime import datetime

#Data visualization

import matplotlib.pyplot as plt


def clear_screen ():
    time.sleep(1)
    for i in range (99):
        print ("")


def time_stamp ():
    ini_time_stamp = datetime.now().strftime("DATE : %d - %m - %Y | TIME : (%H: %M : %S)")
    print (ini_time_stamp)
    

def creator_id ():
        information = [
        "PYTHON Duplicate_Eliminator.PY PROJECT",
        "CREATED BY : OSCAR TAMBUNAN",
    ]
        
        for show_creator_id in creator_id:
            print (show_creator_id)
    
    
def delete_duplicated ():
    global df_main_file
    df_main_file = df_main_file.drop_duplicates()
    print ("")
    print ("Deletting Duplicate/Multiple CSV ")
    time.sleep(3)
    print ("Duplicated Count (AFTER )  :" ,df_main_file.duplicated().sum())

    
def create_new_file ():
    file_time_stamp = datetime.now().strftime( "(%H%M%S)")
    new_file_name = (f"{file_time_stamp}harga_rumah_jakarta.csv")
    df_main_file.to_csv(new_file_name, index=False)

    print ("NEW CSV FILE CREATED : " , new_file_name)
    
    
def cnf_menu ():
    in_cnf_menu = [
        "-1- DOWNLOAD NEW FILE",
        "-2- SKIP DOWNLOAD NEW FILE"
    ]
    for i in  in_cnf_menu:
        print (i)
    

time_stamp()

    
#READ AND SHOW  TYPE : "CSV" AT DRIVE
df_main_file = pd.read_csv("harga_rumah_jakarta.csv")
print ("File open succesfully")

time.sleep(2)

#SHOW DF TYPE DATA
df_main_file.info()

print ("data size :")
print (df_main_file.shape)

df_main_file.head()

#SHOW duplicate df from CSV
print("Duplicated count (BEFORE) :", df_main_file.duplicated().sum(), end="")
time.sleep(3)
duplicate_counter = df_main_file.duplicated().sum()
df_main_file.isna().sum()

#RE- CHECK DUPLICATE DF AT CSV
while True :
    duplicate_counter = df_main_file.duplicated().sum()
    if duplicate_counter == 0:
        print (" Duplicate ") 
        break
    else :
        print (" Duplicates")
        delete_duplicated()
        

#Save new csv
while True :
    try:
        cnf_menu()
        cnf_input = input("INPUT YOUR CHOICE :")
        if cnf_input == "1":
            print ("DOWNLOADING NEW FILE")
            create_new_file()
            print ("DATE / TIME")
            time_stamp()
            break

        elif cnf_input == "2":
            print ("THE FILE WONT BE DOWNLOADED")
            break
    except ValueError:
        print ("Only Input Integer/Number")
        break













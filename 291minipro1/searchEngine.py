

import random
import cx_Oracle
import datetime

def searchEngine(curs, connection):
    print("SearchEngine...")
    option=0
    while (option != 'exit'):
        #print("SearchEngine...\n return: return to main menu \n exit: exit the program\n ")
        option = input("option? \n1-Driver's Info \n2-Violation Records \n3-Vehilce History \n exit: exit to main\n-")
        
        if option!=0:
            if option=='1':
                choice=input("1-Licence No \n2-Name \n-")
                if choice=='1':
                    licenceNo=input('now enter the licenceNO\n-')            
                    query="SELECT name, d.licence_no, addr, birthday, class, description, expiring_date FROM people p, drive_licence d, driving_condition dc, restriction r WHERE d.licence_no=r.licence_no AND r.r_id=dc.c_id AND p.sin=d.sin AND d.licence_no="+"\'"+licenceNo+"\'"
                    curs.execute(query)
                    rows = curs.fetchall()    
                    if len(rows)==0:
                        print("no info avaliable")
                    else:                        
                        for i in rows:
                            print("name:",i[0])
                            print("licence_no:",i[1])
                            print("addr:",i[2])
                            print("birthday:",i[3])
                            print("driving class:",i[4])
                            print("driving_condition:",i[5])
                            print("expiring_data:",i[6])            
                if choice=='2':
                    name=input('now enter the name\n-')
                    query="SELECT name, d.licence_no, addr, birthday, class, description, expiring_date FROM people p, drive_licence d, driving_condition dc, restriction r WHERE d.licence_no=r.licence_no AND r.r_id=dc.c_id AND p.sin=d.sin AND p.name="+"\'"+name+"\'"
                    curs.execute(query)
                    rows = curs.fetchall()            
                    if len(rows)==0:
                        print("no info avaliable")
                    else:              
                        for i in rows:
                            print("name:",i[0])
                            print("licence_no:",i[1])
                            print("addr:",i[2])
                            print("birthday:",i[3])
                            print("driving class:",i[4])
                            print("driving_condition:",i[5])
                            print("expiring_data:",i[6])                
            elif option=='2':
                choice=input("1-Licence No. \n2-SIN of a person\n")
                if choice=='1':
                    licence=input("please input the licence number\n")
                    query="SELECT name, d.licence_no, t.ticket_no, t.violator_no, t.vehicle_id, t.office_no, t.vtype, t.vdate, t.place, tt.fine, descriptions FROM people p, ticket t, ticket_type tt, drive_licence d WHERE p.sin=t.violator_no AND t.vtype=tt.vtype AND p.sin=d.sin AND d.licence_no="+"\'"+licence+"\'"
                    curs.execute(query)
                    rows = curs.fetchall()            
                    if len(rows)==0:
                        print("no info avaliable")
                    else:                        
                        for i in rows:            
                            print("Name:",i[0])
                            print("Licence No:",i[1])
                            print("Ticket No:",i[2])
                            print("Violator No:",i[3])
                            print("Vehicle ID:",i[4])
                            print("Office No:",i[5])
                            print("Violation Type:",i[6])
                            print("Violation Date:",i[7])
                            print("Violation Place:",i[8])
                            print("Fine:",i[9])
                            print("Description:",i[10])            
                if choice=='2':
                    sin=input("please input the sin\n")
                    query="SELECT name, t.ticket_no, t.violator_no, t.vehicle_id, t.office_no, t.vtype, t.vdate, t.place, tt.fine, descriptions FROM people p, ticket t, ticket_type tt WHERE p.sin = t.violator_no AND t.vtype = tt.vtype AND p.sin = "+"\'"+sin+"\'"
                    curs.execute(query)
                    rows = curs.fetchall()  
                    if len(rows)==0:
                        print("no info avaliable")
                    else:                        
                        for i in rows:            
                            print("Name:",i[0])
                            print("Ticket No:",i[1])
                            print("Violator No:",i[2])
                            print("Vehicle ID:",i[3])
                            print("Office No:",i[4])
                            print("Violation Type:",i[5])
                            print("Violation Date:",i[6])
                            print("Violation Place:",i[7])
                            print("Fine:",i[8])
                            print("Description:",i[9])           
        
            
            
            
            elif option=='3':
                serialnumber = input("Vehicle Serial Number\n")
                query="SELECT COUNT(transaction_id), AVG(price), COUNT(ticket_no) FROM auto_sale a, ticket t WHERE a.vehicle_id="+"\'"+serialnumber+"\'"
                curs.execute(query)
                rows = curs.fetchall()
                if len(rows)==0:
                    print("no info avaliable")
                else:                    
                    for i in rows:
                            print("Transaction number of times:",i[0])
                            print("Average Price:",i[1])
                            print("Number of Violation:",i[2])
            else:
                if(option !='exit'):
                    print('invalid input!\n \n \n')
        option = input("countinue?(yes/exit)\n")
    
    print('bye')


dt = "DROP TABLE "

drop_o = dt + "owner;"
drop_as = dt + "auto_sale;"
drop_r = dt + "restriction;"
drop_dc = dt + "driving_condition;"
drop_t = dt + "ticket;"
drop_tt = dt + "ticket_type;"
drop_v = dt + "vehicle;"
drop_vt = dt + "vehicle_type;"
drop_dl = dt + "drive_licence;"
drop_p = dt + "people;"

creat_p = "CREATE TABLE  people (sin CHAR(15), name VARCHAR(40), height number(5,2), weight number(5,2), eyecolor VARCHAR (10), haircolor VARCHAR(10), addr VARCHAR2(50), gender CHAR, birthday DATE, PRIMARY KEY (sin), CHECK ( gender IN ('m', 'f') ) );"

creat_dl = "CREATE TABLE drive_licence (licence_no CHAR(15), sin char(15), class VARCHAR(10), photo BLOB, issuing_date DATE, expiring_date DATE, PRIMARY KEY (licence_no), UNIQUE (sin), FOREIGN KEY (sin) REFERENCES people ON DELETE CASCADE );"

creat_dc = "CREATE TABLE driving_condition (c_id INTEGER, description VARCHAR(1024), PRIMARY KEY (c_id) );"

creat_r = " CREATE TABLE restriction(licence_no CHAR(15), r_id INTEGER, PRIMARY KEY (licence_no, r_id), FOREIGN KEY (licence_no) REFERENCES drive_licence, FOREIGN KEY (r_id) REFERENCES driving_condition );"

creat_vt = "CREATE TABLE vehicle_type (type_id integer, type CHAR(10), PRIMARY KEY (type_id) );"

creat_v =  "CREATE TABLE vehicle (serial_no CHAR(15), maker VARCHAR(20), model VARCHAR(20), year number(4,0), color VARCHAR(10), type_id integer,PRIMARY KEY (serial_no), FOREIGN KEY (type_id) REFERENCES vehicle_type );"

creat_o = "CREATE TABLE owner ( owner_id CHAR(15), vehicle_id CHAR(15), is_primary_owner CHAR(1), PRIMARY KEY (owner_id, vehicle_id), FOREIGN KEY (owner_id) REFERENCES people,FOREIGN KEY (vehicle_id) REFERENCES vehicle,CHECK ( is_primary_owner IN ('y', 'n')) );"

creat_as = "CREATE TABLE auto_sale ( transaction_id int, seller_id CHAR(15), buyer_id CHAR(15), vehicle_id CHAR(15), s_date date, price numeric(9,2), PRIMARY KEY (transaction_id), FOREIGN KEY (seller_id) REFERENCES people, FOREIGN KEY (buyer_id) REFERENCES people, FOREIGN KEY (vehicle_id) REFERENCES vehicle);"

creat_tt = "CREATE TABLE ticket_type ( vtype CHAR(10), fine number(5,2), PRIMARY KEY (vtype));"

creat_t = "CREATE TABLE ticket ( ticket_no int, violator_no CHAR(15), vehicle_id CHAR(15), office_no CHAR(15), vtype char(10), vdate date, place varchar(20), descriptions varchar(1024), PRIMARY KEY (ticket_no), FOREIGN KEY (vtype) REFERENCES ticket_type, FOREIGN KEY (violator_no) REFERENCES people ON DELETE CASCADE, FOREIGN KEY (vehicle_id)  REFERENCES vehicle, FOREIGN KEY (office_no) REFERENCES people ON DELETE CASCADE);"




def doTable():
	print("1")
	pass

doTable()


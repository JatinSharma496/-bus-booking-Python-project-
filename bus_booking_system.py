import sqlite3
from tkinter import messagebox

def connect_database():
    conn=sqlite3.connect("bus_booking_system.db")
    return conn

def create_table():
    conn=connect_database()
    cursor=conn.cursor()

    cursor.execute('''
    create table if not exists bus_operators(
        operator_id text primary key,
        operator_name text,
        operator_address text,
        operator_phone  text,
        operator_email text
    )
    ''')

    cursor.execute('''
    create table if not exists bus_details(
        bus_id text primary key,
        bus_type text,
        bus_capacity integer,
        bus_fare integer,
        operator_id text references bus_operators(operator_id) on delete cascade on update cascade,
        route_id text references route_details(route_id) on delete cascade on update cascade
    )
    ''')

    cursor.execute('''
    create table if not exists route_details(
        route_id text,
        station_name text,
         station_id text,
         primary key (route_id,station_name) 
    )
    ''')


    cursor.execute('''
    CREATE TABLE IF NOT EXISTS new_run (
        bus_id TEXT,
        running_date TEXT,
        seat_available INTEGER,
        PRIMARY KEY (bus_id, running_date),
        FOREIGN KEY (bus_id) REFERENCES bus_details(bus_id) ON DELETE CASCADE ON UPDATE CASCADE
    )
''')


  
    cursor.execute('''
    create table if not exists booking_details(
        bookin_reference_no text Primary key,
        start_station_id text ,
        end_station_id text ,
        booking_date text,
        travel_date text,
        name text,
        gender text,
        total_seat integer,
        mobile_no text,
        age text,
        bus_id text references bus_details(bus_id)     
    )
    ''')


    

    conn.commit()
    conn.close()

    
def add_booking_details(passenger_data):
    conn = connect_database()
    cursor = conn.cursor()

    cursor.execute('''
        INSERT INTO  booking_details (bookin_reference_no,start_station_id, end_station_id, booking_date, 
        travel_date,name,gender,total_seat,mobile_no ,age,bus_id)
        VALUES (?, ?, ?, ?,?,?,?,?,?,?,?)
    ''', passenger_data)

    conn.commit()
    conn.close()
    

def add_operator(operator_data):
    conn = connect_database()
    cursor = conn.cursor()

    cursor.execute('''
        INSERT INTO bus_operators (operator_id, operator_name, operator_address, operator_phone, operator_email)
        VALUES (?, ?, ?, ?, ?)
    ''', operator_data)

    conn.commit()
    conn.close()


def edit_operator(op_id,operator_data):
    conn = connect_database()
    cursor = conn.cursor()

    cursor.execute('''
        update bus_operators set operator_id=?, operator_name=?, operator_address=?, operator_phone=?, operator_email=?
        where operator_id=?
    ''',(*operator_data,op_id) )

    conn.commit()
    conn.close()


def add_bus(bus_data):
    conn = connect_database()
    cursor = conn.cursor()

    try:
        cursor.execute('select * from route_details where route_id = ?', (bus_data[5],))
        if not cursor.fetchone():
            messagebox.showerror("Error", "Route_id does not exist.")
            conn.rollback()
            return

        cursor.execute('SELECT * FROM bus_operators WHERE operator_id = ?', (bus_data[4],))
        if not cursor.fetchone():
            messagebox.showerror("Error", "Operator_id does not exist.")
            conn.rollback()
            return

        cursor.execute('''
            INSERT INTO bus_details (
                bus_id,
                bus_type,
                bus_capacity,
                bus_fare,
                operator_id,
                route_id
            )
            VALUES (?, ?, ?, ?, ?, ?)
        ''', bus_data)

        conn.commit()
        return 1
    except Exception as e:
        #messagebox.showerror("Error", f"Error adding bus: {e}")
        conn.rollback()
        return
    finally:
        conn.close()


def edit_bus(busid,bus_data):
    conn = connect_database()
    cursor = conn.cursor()

    cursor.execute('select * from route_details where route_id = ?',(bus_data[5],))
    if not cursor.fetchone():
        messagebox.showerror("Error","Route_id does not exist.")
        conn.rollback()
        return 

    cursor.execute('SELECT * FROM bus_operators WHERE operator_id = ?', (bus_data[4],))
    if not cursor.fetchone():
        messagebox.showerror("Error","Operator_id does not exist.")
        conn.rollback()
        return

    cursor.execute('''
        update bus_details set
         bus_id=?,
         bus_type=?,
          bus_capacity=?, 
          bus_fare=?, 
          operator_id=?,
          route_id=?
        where bus_id=?
    ''',(*bus_data,busid) )

    conn.commit()
    conn.close()

from tkinter import messagebox

def add_route(route_data):
    conn = connect_database()
    cursor = conn.cursor()

    try:
        cursor.execute('''
            INSERT INTO route_details (
               route_id, station_name, station_id)
            VALUES (?, ?, ?)
        ''', route_data)

        conn.commit()
        conn.close()
    except Exception as e:
        conn.rollback()
        conn.close()
        messagebox.showerror("Error", f"Failed to add route: {e}")
        return


def add_newrun(newrun_data):
    conn = connect_database()
    cursor = conn.cursor()

    try:
        # Check if the record already exists
        cursor.execute('SELECT * FROM new_run WHERE bus_id = ? AND running_date = ?', (newrun_data[0], newrun_data[1]))
        if cursor.fetchone():
            messagebox.showerror("Error", "Record with the same bus_id and running_date already exists.")
            return

        # Insert the new record
        cursor.execute('''
            INSERT INTO new_run (
               bus_id,
               running_date,
               seat_available
            )
            VALUES (?, ?, ?)
        ''', newrun_data)

        conn.commit()
    except Exception as e:
        messagebox.showerror("Error", f"Error adding new_run record: {e}")
        conn.rollback()
    finally:
        conn.close()
create_table()



def delete_route(route_id, station):
    conn = connect_database()
    cursor = conn.cursor()

    # Use a parameterized query for composite primary key
    cursor.execute('DELETE FROM route_details WHERE route_id = ? AND station_name = ?', (route_id, station))

    conn.commit()
    conn.close()



def delete_newrun(bus_id, running_date):
    conn = connect_database()
    cursor = conn.cursor()

    try:
        # Use parameterized query to avoid SQL injection
        cursor.execute('DELETE FROM new_run WHERE bus_id = ? AND running_date = ?', (bus_id, running_date))

        # Check if any rows were affected
        if cursor.rowcount == 0:
            messagebox.showerror("Error", "Record not found.")
        conn.commit()
    except Exception as e:
        messagebox.showerror("Error", f"Error deleting new_run record: {e}")
        conn.rollback()
    finally:
        conn.close()



def read_operators():
    conn = connect_database()
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM bus_operators')
    operators = cursor.fetchall()

    conn.close()

    return operators

print("\n operator  data:\n")
print(read_operators())


def read_bus():
    conn = connect_database()
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM bus_details')
    operators = cursor.fetchall()

    conn.close()

    return operators

print("\nBus data:\n")
print(read_bus())


def read_route():
    conn = connect_database()
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM route_details')
    
    operators = cursor.fetchall()

    conn.close()

    return operators

print("\nroute data:\n")
print(read_route())

def read_booking():
    conn = connect_database()
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM booking_details')
    
    operators = cursor.fetchall()

    conn.close()

    return operators

print("\nbooking data:\n")
print(read_booking())


def ticket(refer_no):
    conn = connect_database()
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM booking_details where bookin_reference_no=? ',(refer_no,))
    
    operators = cursor.fetchall()

    conn.close()

    return operators


def show_tickets_from_mobile(mobile_no):
    conn = connect_database()
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM booking_details where mobile_no =? ',(mobile_no,))
    
    operators = cursor.fetchall()

    conn.close()

    return operators
def read_newrun():
    conn = connect_database()
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM new_run')
    operators = cursor.fetchall()

    conn.close()

    return operators

print("\nnew run data:\n")
print(read_newrun())


def show_route(start_station_name, end_station_name):
    conn = connect_database()
    cursor = conn.cursor()

    # Use a self-join to find route_ids that have both start and end stations
    cur = cursor.execute('''
        SELECT r1.route_id
        FROM route_details r1
        JOIN route_details r2 ON r1.route_id = r2.route_id
        WHERE r1.station_name = ? AND r2.station_name = ?
    ''', (start_station_name, end_station_name))

    route = cur.fetchall()

    conn.close()
    return route



def show_bus(route):
    conn = connect_database()
    cursor = conn.cursor()

    
    cur = cursor.execute('''
        select bus_id from bus_details where route_id =?
    ''', (route))

    buses = cur.fetchall()

    conn.close()
    return buses

def show_bus_fare(bus_id):
    conn = connect_database()
    cursor = conn.cursor()

    
    cur = cursor.execute('''
        select bus_fare from bus_details where bus_id =?
    ''', (bus_id,))

    buses = cur.fetchone()

    conn.close()
    return buses

def show_run(bus_id,Journey_date):
    conn = connect_database()
    cursor = conn.cursor()

    
    cur = cursor.execute('''
        select bus_id from new_run where bus_id =? and running_date=?''',(bus_id,Journey_date))

    buses = cur.fetchall()

    conn.close()
    return buses


def show_operator(bus_id):
    conn = connect_database()
    cursor = conn.cursor()

    # Use a join operation to get the operator details associated with the bus_id
    cur = cursor.execute('''
        SELECT bo.operator_name
        FROM bus_details bd
        JOIN bus_operators bo ON bd.operator_id = bo.operator_id
        WHERE bd.bus_id = ?
    ''', (bus_id,))

    operator_name = cur.fetchone()

    conn.close()
    return operator_name


def show_bus_type(busid):
    conn = connect_database()
    cursor = conn.cursor()

    cur=cursor.execute('select bus_type from bus_details where bus_id=?',(busid,))
    bus_type=cur.fetchone()

   
    conn.close()
    return bus_type



def show_avail(bus_id, running_date):
    conn = connect_database()
    cursor = conn.cursor()

    try:
        # Use a parameterized query to avoid SQL injection
        cursor.execute('SELECT seat_available FROM new_run WHERE bus_id = ? AND running_date = ?', (bus_id, running_date))
        seat = cursor.fetchone()

        return seat[0] if seat else None
    except Exception as e:
        print(f"Error in show_avail: {e}")
        return None
    finally:
        conn.close()



def edit_avail(bus_id, total_seat, Journey_date):
    conn = connect_database()
    cursor = conn.cursor()

    try:
        # Use a parameterized query to avoid SQL injection
        cursor.execute('SELECT seat_available FROM new_run WHERE bus_id = ? AND running_date = ?', (bus_id, Journey_date))
        seat = cursor.fetchone()

        if seat:
            remaining_seats = int(seat[0]) - int(total_seat)

            # Update the available seats in the new_run table
            cursor.execute('UPDATE new_run SET seat_available=? WHERE bus_id=? AND running_date=?', (remaining_seats, bus_id, Journey_date))
            conn.commit()
        else:
            print("Record not found for the specified bus_id and running_date.")
    except Exception as e:
        print(f"Error in edit_avail: {e}")
        conn.rollback()
    finally:
        conn.close()

def show_cap(busid):
    conn = connect_database()
    cursor = conn.cursor()

    cur=cursor.execute('select  bus_capacity from bus_details where bus_id=?',(busid,))
    bus_type=cur.fetchone()

    conn.close()
    return bus_type


def show_fare(busid):
    conn = connect_database()
    cursor = conn.cursor()

    cur=cursor.execute('select bus_fare from bus_details where bus_id=?',(busid,))
    bus_fare=cur.fetchone()

    conn.commit()
    conn.close()
    return bus_fare

print(show_operator("1"))

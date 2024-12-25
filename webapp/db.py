"""Database queries and functions."""

import psycopg
import socket
from datetime import datetime
import random
# Determine whether running on/off campus
# Note: PGUSER and PGPASSWORD must be set
try:
    socket.gethostbyname("data.cs.jmu.edu")
    DSN = "host=data.cs.jmu.edu dbname=motel7 user=rebellcj password=113464038"
except:
    DSN = "host=localhost dbname=motel7"

# ---------------------------- functions for CHECK-IN ----------------------------
def checking_in(reservation_id):
    reservation_id = str(reservation_id)
    with psycopg.connect(DSN) as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM checking_in(%s)",
                        [reservation_id])
            return cur.fetchall()
        
def checking_into_room(room_number, hotel_id, reservation_id):
    with psycopg.connect(DSN) as conn:
        with conn.cursor() as cur:

            # Get destination
            sql = """UPDATE reservation
                  SET room_number = %s
                  where reservation_id = %s"""
            cur.execute(sql, (room_number, reservation_id))

            sql = """UPDATE room
                  SET occupied = True
                  WHERE room_number = %s and hotel_id = %s"""
            cur.execute(sql, (room_number, hotel_id))

# ---------------------------- functions for CHECK OUT ----------------------------
def checking_out(reservation_id):
    reservation_id = str(reservation_id)
    if reservation_id != "":
        with psycopg.connect(DSN) as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT * FROM checking_out(%s)",
                            [reservation_id])
                result1 = cur.fetchall()
                cur.execute("SELECT * FROM season_price(%s)",
                            [reservation_id])
                result2 = cur.fetchall()
                
                cur.execute("SELECT * FROM dow_finder(%s)",
                            [reservation_id])
                result3 = cur.fetchall()
                cur.execute("SELECT * FROM additional_charge(%s)",
                            [reservation_id])
                result4 = cur.fetchall()
                if result2[0][0] != None and result1[0][0] != None:
                    return [(reservation_id, str(round(result1[0][0])), str(result2[0][0]), str(result3[0][0]), str(result4[0][0]), str(round(result1[0][0]) * result2[0][0] + result3[0][0] + result4[0][0]))]
                if result1[0][0] != None:
                    return [(reservation_id, str(round(result1[0][0])), str(0), str(result3[0][0]), str(result4[0][0]), str(round(result1[0][0]) + result3[0][0] + result4[0][0]))]
  
def checkout_success(id, total):
    id = str(id)
    total = str(total)
    with psycopg.connect(DSN) as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT * FROM room_change(%s, %s)",
                            [id, total])
                return
            
def season_price(reservation_id):
    reservation_id = str(reservation_id)
    with psycopg.connect(DSN) as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM season_price(%s)",
                        [reservation_id])
            return cur.fetchall()
        
def hotel_movies(reservation_id):
    reservation_id = str(reservation_id)
    with psycopg.connect(DSN) as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM movie_list(%s)",
                        [reservation_id])
            return cur.fetchall()

def checking_out_movie(reservation_id, title):
    reservation_id = str(reservation_id)
    title = str(title)
    with psycopg.connect(DSN) as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM additional_insert(%s, %s)",
                        (title, reservation_id))
            return cur.fetchall()

# ---------------------------- functions for the RESERVATION ----------------------------

# function to print all the reservations that meet the criteria
def reservation(hotel_id, guest_id, check_in_date, check_out_date):
    hotel_id = str(hotel_id)
    guest_id = str(guest_id)
    check_in_date = str(check_in_date)
    check_out_date = str(check_out_date)
    with psycopg.connect(DSN) as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM reservation_search(%s, %s, %s, %s)",
                    [hotel_id, guest_id, check_in_date, check_out_date])
            return cur.fetchall()

# function to filter out available reservations with the param specifications, calls the reservation.sql query
def fetch_reservation_data(hotel_id, guest_id, check_in_date, check_out_date):
    # Connection and query logic (placeholder)
    with psycopg.connect(DSN) as conn:
        with conn.cursor() as cur:
            cur.execute(" SELECT room_type, average_nightly_price FROM reservation_search(%s, %s, %s, %s)", 
                        [hotel_id, guest_id, check_in_date, check_out_date])
            return cur.fetchall()
        
# get the room_type_id from its string and hotel_id (needed to insert a reservation into the table)      
def fetch_room_type_id(room_type_str, hotel_id):
    with psycopg.connect(DSN) as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT room_type_id FROM room_type WHERE hotel_id = %s AND room_type = %s", 
                        [hotel_id, room_type_str])
            return cur.fetchall()
    
# function to generate a reservation_id to be used in booking, makes sure no reservation 
# currently exists with said reservation_id
def create_reservation_id(hotel_id):
    reservation_id = random.randint(1, 5000)
    with psycopg.connect(DSN) as conn:
        with conn.cursor() as cur:
            # make sure reservation id does not exist
            cur.execute("SELECT * FROM reservation WHERE reservation_id = %s AND hotel_id = %s", 
                    [reservation_id, hotel_id])
            # keep trying till generate a reservation_id that doesn't exist yet
            if cur.fetchall() != "":
                reservation_id = random.randint(1, 5000)
            cur.execute("SELECT * FROM reservation WHERE reservation_id = %s AND hotel_id = %s", 
                    [reservation_id, hotel_id])
        return reservation_id

# "book" a reservation (i.e. insert reservation into the database)
def book_reservation(hotel_id, beg_date, end_date, guest_id, room_type_str, est_price, num_occupants):
    with psycopg.connect(DSN) as conn:
        with conn.cursor() as cur:
        # convert or fetch any necessary data to match format needed for reservation table
            reservation_id = create_reservation_id(hotel_id)
            room_number = 0 # placeholder till check-in
            room_type_id = fetch_room_type_id(room_type_str, hotel_id)[0][0]
            print(room_type_id)
            check_in = datetime.strptime(beg_date, "%Y-%m-%d").date()
            check_out = datetime.strptime(end_date, "%Y-%m-%d").date()
            print(check_in)
            num_days = (check_out.day - check_in.day) + 1
            print("num days: ", num_days)
            est_price = 157.91 * num_days  # nightly price x number of nights
            print(est_price)
            # create a reservation for the room_type selected with the info above
            sql = "INSERT INTO reservation VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s)"
            args = [reservation_id, room_number, hotel_id, beg_date, end_date, room_type_id, num_occupants, est_price, guest_id]
            cur.execute(sql, args)
            
            # allow the user to add occupants after creation (update reservation info)
            return reservation_id

if __name__ == "__main__":
    print(checking_in(2))
"""Example web application for postgres_air."""

from datetime import date
from flask import Flask, request, render_template, redirect, flash
from psycopg import DatabaseError
import db

app = Flask(__name__)
app.secret_key = "dev"

@app.route("/")
def index():
    return render_template('main.html', title='Home')

@app.route("/checking_in")
def checking_in():
    reservation_id = request.args.get("reservation_id", 1)

    if request.args:
        data = db.checking_in(reservation_id)
    else:
        data = None
    return render_template('checking_in.html', title='Check In', data=data, reservation_id=reservation_id, reservation_id_hidden=reservation_id)

# ---------------------------- for check-out ----------------------------
@app.route("/checking_out")
def checking_out():
    reservation_id = request.args.get("reservation_id", 1)
    if request.args:
        data = db.checking_out(reservation_id)
    else:
        data = None
        
    print(data)
    
    return render_template('checking_out.html', title='Check Out', data=data, reservation_id=reservation_id)

@app.route("/hotel_movies")
def hotel_movies():
    reservation_id = request.args.get("reservation_id", "")
    if request.args:
        data = db.hotel_movies(reservation_id)
        for ind, m in enumerate(data):
            data[ind] = m[1:]
    else:
        data = None
    print(data)
    return render_template('hotel_movies.html', title='Hotel Movies', data=data, reservation_id = reservation_id)

@app.route("/movie_reserve")
def movie_reserve():
    reservation_id_hidden = request.args.get("reservation_id_hidden", "")
    movie_title = request.args.get("title", "")
    if reservation_id_hidden and movie_title:
        db.checking_out_movie(reservation_id_hidden, movie_title)
    return render_template("movie_suc.html", title='Check Out Movie', reservation_id=reservation_id_hidden)


@app.route("/room_reserve")
def room_reserve():
    # Make sure a flight was selected
    room_number = request.args.get("room_number", "")
    if not room_number:
        return redirect("/room_reserve")
    # Get inputs from this page's form
    hotel_id = request.args.get("hotel_id", "")
    reservation_id = request.args.get("reservation_id_hidden", "")
    for i in range(10):
        print(hotel_id, reservation_id)
    if hotel_id and reservation_id:
        try:
            db.checking_into_room(room_number, hotel_id, reservation_id)
            # flash(f"Successfully booked {name} ({ref})")
        except DatabaseError as error:
            flash(error)
    return render_template("checking_in_success.html", title='Check In Success', reservation_id=reservation_id)

@app.route("/export_data/<id>")
def export_data(id):
    total = request.args.get('total')
    print(total)
    db.checkout_success(id, total)
    return render_template('success.html', title='Success', reservation_id=id)

# ---------------------------- for reservation ----------------------------
@app.route("/reservation")
def reservation():
    # get form inputs with default values
    default_date = date.today().strftime('%Y-%m-%d')  # Sets today's date as default
    hotel_id = request.args.get("hotel_id", 1)
    guest_id = request.args.get("guest_id", 2)
    check_in_date = request.args.get("check_in_date", default_date)
    check_out_date = request.args.get("check_out_date", default_date)
    rounded_data = []
    if request.args:
        data = db.fetch_reservation_data(hotel_id, guest_id, check_in_date, check_out_date)
        rounded_data = [(room_type, round(average_nightly_price, 2)) for room_type, average_nightly_price in data]
        # data = db.reservation(hotel_id, guest_id, check_in_date, check_out_date)
    else:
        data = None
    print(data)
    return render_template("reservation.html", title='Reservation', data=rounded_data, hotel_id=hotel_id, guest_id=guest_id, check_in_date=check_in_date, check_out_date=check_out_date)

@app.route("/export_reservation")
def export_res():
    # make sure a reservation was selected
    room_type = request.args.get("room_type", "")
    if not room_type:
        return redirect("/reservation")
    # Get inputs from this page's form 
    hotel_id = request.args.get("hotel_hidden", "")
    base_price = request.args.get("average_nightly_cost", "")
    check_in_date = request.args.get("check_in_hidden", "")
    check_out_date = request.args.get("check_out_hidden", "")
    guest_id = request.args.get("guest_hidden", "")
    num_occupants = request.args.get("num_occupants", "")
    print(room_type)
    print(base_price)
    print(check_in_date)
    print(check_out_date)
    print(guest_id)
    print(num_occupants)

    if room_type and base_price and hotel_id and check_in_date and check_out_date and num_occupants:
        try:
            reservation_id = db.book_reservation(
                hotel_id, check_in_date, check_out_date, guest_id, room_type, base_price, num_occupants
            )
            return render_template('reservation_confirm.html', title="successful_booking", hotel_id=hotel_id, check_in_date=check_in_date, check_out_date=check_out_date, 
        guest_id=guest_id, room_type=room_type, num_occupants=num_occupants, base_price=base_price, reservation_id=reservation_id)
            # db.book_reservation(hotel_id, check_in_date, check_out_date, guest_id, room_type, base_price, num_occupants)
        except DatabaseError as error:
            app.logger.error(f"Database error occurred: {error}")
            flash(str(error))
        return redirect("/reservation")

    



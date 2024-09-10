"""Generate fake data for the hotel database."""
# Generate fake data for motel7 database


import datetime
from faker import Faker
import random

fake = Faker()

# Function that make 20 hotels 
def make_hotels():
    hotels = []
    for id in range(1, 21):
        h = []
        h.append(id)
        h.append(fake.street_address() + " " + fake.country() + ", " + fake.city())
        h.append(fake.color_name() + str(id) + " Hotel")
        hotels.append(h)
    return hotels

# Function to connect 1-4 phone numbers for each hotel created above
def make_hotel_phones(hotels):
    hotel_phones = []
    for h in hotels:
        # a hotel has between 1 and 4 phone numbers
        phones = random.randint(1, 4)
        # phones+1 because the end of the range is not inclusive
        for i in range(1, phones+1):
            hp = []
            hp.append(h[0])  # hotel id
            hp.append(i)
            hp.append(fake.msisdn()[:-3])
            # make a random choice from a list
            hp.append(random.choice(["Front Desk", "Reservations", "Room Service", "Security"]))
            hotel_phones.append(hp)
    return hotel_phones

# Functions to generate employees for a hotel
def employee(hotels):
    employees = []
    for id in hotels:
        num_employed = random.randint(50, 150)
        for i in range(num_employed):
            employee_id = fake.unique.random_number(digits=4)
            employee_name = fake.unique.name()
            phone_number = fake.msisdn()
            trimmed = phone_number[:-3]
            salary = random.randint(20000, 80000)
            employees.append((employee_id, id[0], employee_name, trimmed, salary))
    return employees

# list that holds all the possible room_types a hotel could possibly have
room_array = [("Single", 150, 2), ("Double", 250, 4), ("Triple", 300, 5), ("Suite", 500, 4), ("Penthouse", 1500, 6)]

# Function randomly generate room_types per hotel
def make_room_types(hotels):
    room_types = []
    room_array = [("Single", 150, 2, 125), ("Double", 250, 4, 150), ("Triple", 300, 5, 175), ("Suite", 500, 4, 300), ("Penthouse", 1500, 6, 500)]
    room_type_cur_id = 1
    for h in hotels:
        room_array_copy = room_array[:]
        for i in range(1, 4):
            rt = []
            rt.append(h[0]) # Append hotel ID
            rt.append(room_type_cur_id) # room type ID
            room_type_cur_id += 1 #increment index
            type_name = random.choice(room_array_copy) # Randomly pick name of type, then remove from set to avoid repeats
            room_array_copy.remove(type_name)
            rt.append(type_name[0])
            size = type_name[1] 
            rt.append(str(size) + " square feet") # size 
            rt.append(type_name[2]) # capacity
            rt.append(type_name[3])
            room_types.append(rt)
    return room_types

# Function to generate features assoicated with a specific room type 
def room_features(room_types):
    room_features = []
    for room_type in room_types:
        if room_type[2] == "Single":
            room_features.append((room_type[1], "TV, Desk, Mini-Fridge, Standard Bathroom, Couch, Queen Sized Bed, Microwave"))
        elif room_type[2] == "Double":
            room_features.append((room_type[1], "TV, Desk, Mini-Fridge, Standard Bathroom, Couch, Two Queen Beds, Small Dining Table"))
        elif room_type[2] == "Triple":
            room_features.append((room_type[1], "TV, Desk, Mini-Fridge, Standard Bathroom, Couch, Three Queen Beds, Medium Dining Table"))
        elif room_type[2] == "Suite":
            room_features.append((room_type[1], "TV, Desk, Mini-Fridge, Standard Bathroom, Couch, Kitchenette, Medium Dining Table, Separate Bedroom(s), Small Balcony"))
        elif room_type[2] == "Penthouse":
            room_features.append((room_type[1], "TV, Desk, Mini-Fridge, Standard Bathroom, Couch, Direct Elevator Access, Jacuzzi Tub, Two Bedrooms (one with king size bed, one with two queens), Private(roof-top) Terrace, Washer and Dryer"))

    return room_features

# Function that generate rooms for a hotel
def make_rooms(hotels, room_types):
    rooms = []
    for h in hotels:
        floor = 1
        for rt in room_types:
            for i in range(25):
                if h[0] == rt[0]:
                    room = []
                    room.append(str(floor) + str(i).zfill(2)) # room_number
                    room.append(rt[1]) # Room_type
                    room.append(h[0]) # Hotel_id
                    room.append(floor) # floor number
                    room.append(random.choice([True, False])) #is_cleaned
                    room.append(random.choice([True, False])) #occupied
                    rooms.append(room) # add to room array 
            if h[0] == rt[0]:
                floor += 1
        floor = 1
    return rooms

# Function that generates ammenities for each hotel
def hotel_ammenity(hotels):
    amenities = []
    for h in hotels:
        amenity_list = ["Pool", "Spa", "Gym", "Restaurant", "Bar", "Free Wi-Fi", "Parking", "Concierge", "Room Service"]
        num_amenities = random.randint(2, len(amenity_list))
        chosen_amenities = set() 
        while len(chosen_amenities) < num_amenities:
            amenity = random.choice(amenity_list)
            if amenity not in chosen_amenities:
                chosen_amenities.add(amenity)
                amenities.append((h[0], amenity)) 
    return amenities

# Function that generate seasons 
def make_seasons():
    seasons = []
    season_names = ["Summer Season", "Winter Season", "Ski Season", "Christmas Season", "Fall Season", "Spring Season", "Graduation Season", "Football Season"]
    for season_name in season_names:
        season = []
        season.append(season_name)
        season.append(fake.date_this_year())
        season.append(fake.date_this_year())
        season.append(str(1) + "." + str(random.randint(5, 20)).zfill(2))
        seasons.append(season)
    return seasons

# Function to generate seasons associated with a specific hotel
def make_hotel_seasons(hotels):
    hotel_seasons = []
    # SEASON NAMES MUST MATCH SEASON NAMES IN MAKE_SEASONS IN ODER TO WORK PROPERLY
    season_names = ["Summer Season", "Winter Season", "Ski Season", "Christmas Season", "Fall Season", "Spring Season", "Graduation Season", "Football Season"]
    for h in hotels:
        season_set = set(season_names)
        for i in range(3):
            hotel_season = []
            chosen_name = random.choice(list(season_set))
            season_set.remove(chosen_name)
            hotel_season.append(h[0])
            hotel_season.append(chosen_name)
            hotel_seasons.append(hotel_season)
    return hotel_seasons

#array of tuples to hold guest_statuses and their discount values 
guest_statuses = [("Standard", 10), ("Military", 15), ("Gold", 20), ("Platinum", 25)]

# Function that generates random guests 
def make_guests(guest_statuses):
    guests = []
    guest_statuses = [("Standard", 10), ("Military", 15), ("Gold", 20), ("Platinum", 25)]
    identification_types = ["DriverLicense", "Passport", "SSN"]
    for i in range(500):
        guest = []
        guest.append(i) #guest_id
        guest.append(random.choice(identification_types)) #identifcation_type
        # generate appropriate identification_number based on identification_type selected
        if guest[1] == "Passport":
            guest.append(fake.passport_number()) 
        elif guest[1] == "SSN":
            guest.append(fake.ssn())
        else:
            guest.append(fake.vin())
        guest.append(fake.street_address() + " " + fake.city()) #address
        home_phone = fake.msisdn() 
        guest.append(home_phone[:-3]) #home_phone_number
        mobile_phone = fake.msisdn()
        guest.append(mobile_phone[:-3]) #mobile_phone_number
        guest.append(random.choice(guest_statuses)[0]) #guest_status_str
        guest.append(fake.name())
        guests.append(guest)
    return guests

# Function to generate DOW Multipler for weekily price flucuation of room prices
def dow_multiplier(hotels):
    dows = []
    for h in hotels:
        weekend_addition = random.randint(50, 120)
        dows.append([h[0], "Monday", 1, 0]) # Monday
        dows.append([h[0], "Tuesday", 2, 0]) # Tuesday
        dows.append([h[0], "Wednesday", 3, 0]) # Wednesday
        dows.append([h[0], "Thursday", 4, 0]) # Thursday
        dows.append([h[0], "Friday", 5, weekend_addition]) # Friday
        dows.append([h[0], "Saturday", 6, weekend_addition]) # Saturday
        dows.append([h[0], "Sunday", 7, weekend_addition]) # Sunday
    return dows

# Function to generate reservations
def generate_reservations(rooms, guests):
    reservations = []
    reservation_id = 1
    for room in rooms:
        if (random.choices([True, False], weights= [0.1, 0.9])): 
            this_reservations_guest = random.choice(guests) #pick a guest at random
            reservation = []
            reservation.append(reservation_id) #reservation_id
            reservation_id += 1
            reservation.append(room[0]) #room_number
            reservation.append(room[2]) #hotel_id
            check_in_date = fake.date_time_between_dates(datetime.datetime(2022, 1, 1), datetime.datetime(2024, 4, 1)).date()
            check_out_date = fake.date_time_between_dates(check_in_date, datetime.datetime(2024, 4, 8)).date()
            reservation.append(check_in_date)
            reservation.append(check_out_date)
            reservation.append(room[1]) # room_type_id 
            reservation.append(0) #num_of_occupants
            reservation.append(0) #total_cost
            reservation.append(this_reservations_guest[0]) #guest_id
            reservations.append(reservation) #add to list 
    return reservations



rooms_cap = [("Single", 2), ("Double", 4), ("Triple", 5), ("Suite", 4), ("Penthouse", 6)]

# Function to generate occupants for a reservation based on room_type capacity
def generate_occupants(reservations):
    data = []
    for res in reservations:
        for r_t in room_types:
            # checking hotel_id
            if res[2] == r_t[0]:
                type_str = r_t[2]
                for obj in rooms_cap:
                    if type_str == obj[0]:
                        num_occupants = random.randint(1, obj[1])
                        res[6] = num_occupants
                        for _ in range(num_occupants):
                            name = fake.name()
                            data.append((res[0], name))   
 
    return data

# Function to generate a bill for a reservation
# bill_id, reservation_id, price, paid, guest_id
def make_bill(reservations, guests):
    bills = []
    for res in reservations:
        for g in guests:
            if res[8]==g[0]:
                bill = []
                bill.append(fake.random_number(digits=10)) #bill_id
                bill.append(res[0]) # reservation_id
                bill.append(res[7]) #bill amount 
                bill.append(random.choice([True, False]))
                bill.append(g[0]) #guest_id
                bills.append(bill) # add to bill array
    return bills

#Function to generate a billing_history for a guest 
# guest_id, bill_id, bill_price
def generate_billing_history(bills, guests):
    billing_history = []
    for b in bills:
        for g in guests:
        # add all bills for a guest 
            if b[4]==g[0]:
                past_bill = []
                past_bill.append(g[0]) # guest_id
                past_bill.append(b[0]) #bill_id
                past_bill.append(b[3]) # bill_price
                billing_history.append(past_bill)
    return billing_history

# Function to generate reviews
def generate_reviews(reservations):
    reviews = []
    past_reservations = [res for res in reservations if res[3] < datetime.datetime(2024, 4, 1).date()]
    for reservation in past_reservations:
        guest_id = fake.random_int(min=0, max=499)
        reservation_date = reservation[3]
        display_name = fake.name()
        review_text = fake.paragraph(nb_sentences=3)
        score = fake.random_int(min=1, max=10)
        review = (guest_id, reservation_date, display_name, review_text, score)
        reviews.append(review)
    return reviews
# list of additional charges a guest can incur during their stay, with their name and price assoicated with it
additional_charges = [("room service", 25.00), ("rented movie", 5.00), ("spa", 50.00), ("valet", 10.00), ("city tour", 100.00), ("mini-fridge used", 20.00)]
# make additional charges for a guest on a reservation
def generate_additional_charges(reservations):
    add_charges = []
    for res in reservations:
        for _ in range(0, 5):
            new_charge = random.choice(additional_charges)
            charge = (new_charge[0], new_charge[1], res[0])
            add_charges.append(charge)
            res[7] += new_charge[1]
    return add_charges


# populate employees that can't be used 
# prevent repeats for manager and other employee assignments
added_employees = set() 
# assign one manager per hotel, from prexisiting employees data
def generate_managers(employees, hotels):
    managers = []
    for h in hotels:
        choice = random.choice(employees)
        if choice not in added_employees:
            for i in range(1):   
                added_employees.add(choice[0])
                managers.append((choice[0], h[0])) #employee_id and hotel_id
    return managers

def generate_cleaners(employees, hotels):
    cleaners = []
    for h in hotels:
        assigned_cleaners = 0
        for emply in employees:
            if emply[0] not in added_employees and assigned_cleaners < 4:
                cleaners.append((emply[0], h[0])) #employee_id
                added_employees.add(emply[0])
                assigned_cleaners += 1
        
    return cleaners

def assign_rooms_to_cleaners(cleaners, rooms, hotels):
    cleaning_assignments = []
    for clnr in cleaners:
        hotel_id = clnr[1]
        room_count = 0
        print(f"Cleaner {clnr[0]} works at hotel {hotel_id}")

        for room in rooms:
                if room_count < 5:
                    if room[2] == hotel_id and not room[4]:
                        print(f"Assigning room {room[0]} to cleaner {clnr[0]}")
                        cleaning_assignments.append((room[0], room[1], room[2], clnr[0]))
                        room_count += 1
                if room_count >= 5:
                    break
    return cleaning_assignments

def generate_bellhop(employees, hotels):
    bellhops = []
    for h in hotels:
        num_bellhop = 0
        for emply in employees:
            if emply[0] not in added_employees and num_bellhop < 3:
                bellhops.append((emply[0], h[0]))
                added_employees.add(emply[0])
                num_bellhop += 1
    return bellhops

def generate_desk_clerk(employees, hotels):
    desk_clerks = []
    for h in hotels:
        num_dskclrk = 0
        for emply in employees:
            if emply[0] not in added_employees and num_dskclrk < 4:
                desk_clerks.append((emply[0], h[0]))
                added_employees.add(emply[0])
                num_dskclrk += 1
    return desk_clerks



        

# MAIN FUNCTION!! outputs to files
if __name__ == "__main__":
    # Output everything tab-separated

    f = open("hotels.txt", "w")
    hotels = make_hotels()
    for h in hotels:
        for ind, attr in enumerate(h):
            f.write(str(attr))
            if ind < len(h) - 1:
                f.write("|")
            # print(attr, end="\t")
        f.write("\n")
        # print()
    f.close()


    f = open("phone_numbers.txt", "w")
    hotel_phones = make_hotel_phones(hotels)
    for hp in hotel_phones:
        for ind, attr in enumerate(hp):
            f.write(str(attr))
            if ind < len(hp) - 1:
                f.write("|")
            # print(attr, end="\t")
        f.write("\n")
        # print()
    f.close()

    f = open("room_types.txt", "w")
    room_types = make_room_types(hotels)
    for rt in room_types:
        for ind, attr in enumerate(rt):
            f.write(str(attr))
            if ind < len(rt) - 1:
                f.write("|")
        f.write("\n")
    f.close()

    f = open("rooms.txt", "w")
    rooms = make_rooms(hotels, room_types)
    for room in rooms:
        for ind, attr in enumerate(room):
            f.write(str(attr))
            if ind < len(room) - 1:
                f.write("|")
        f.write("\n")
    f.close()

    f = open("seasons.txt", "w")
    seasons = make_seasons()
    for season in seasons:
        for ind, attr in enumerate(season):
            f.write(str(attr))
            if ind < len(season) - 1:
                f.write("|")
        f.write("\n")
    f.close()

    f = open("hotel_seasons.txt", "w")
    hotel_seasons = make_hotel_seasons(hotels)
    for hotel_season in hotel_seasons:
        for ind, attr in enumerate(hotel_season):
            f.write(str(attr))
            if ind < len(hotel_season) - 1:
                f.write("|")
        f.write("\n")
    f.close()

    f = open("guests.txt", "w")
    guests = make_guests([])
    for guest in guests:
        for ind, attr in enumerate(guest):
            f.write(str(attr))
            if ind < len(guest) - 1:
                f.write("|")
        f.write("\n")
    f.close()

    f = open("room_features.txt", "w")
    room_array = ["Single", "Double", "Triple", "Suite", "Penthouse"]  # Corrected "Penthouse" typo
    r = room_features(room_types)
    for i in r:
        for ind, attr in enumerate(i):
            f.write(str(attr))
            if ind < len(i) - 1:
                f.write("|")
        f.write("\n")
    f.close()

    f = open("hotel_ammenity.txt", "w")
    ammenity = hotel_ammenity(hotels)
    for i in ammenity:
        for ind, attr in enumerate(i):
            f.write(str(attr))
            if ind < len(i) - 1:
                f.write("|")
        f.write("\n")
    f.close()

    f = open("weekily_prices.txt", "w")
    dow = dow_multiplier(hotels)
    for i in dow:
        for ind, attr in enumerate(i):
            f.write(str(attr))
            if ind < len(i) - 1:
                f.write("|")
        f.write("\n")
    f.close()

    f = open("employee_data.txt", "w")
    employee_data = employee(hotels)
    for h in employee_data:
        for ind, attr in enumerate(h):
            f.write(str(attr))
            if ind < len(h) - 1:
                f.write("|")
        f.write("\n")
    f.close() 

    f = open("managers.txt", "w")
    manager_data = generate_managers(employee_data, hotels)
    for mg in manager_data:
        for ind, attr in enumerate(mg):
            f.write(str(attr))
            if ind < len(mg) - 1:
                f.write("|")
        f.write("\n")
    f.close()


    f = open("cleaners.txt", "w")
    cleaners_data = generate_cleaners(employee_data, hotels)
    for clnr in cleaners_data:
        for ind, attr in enumerate(clnr):
            f.write(str(attr))
            if ind < len(clnr) - 1:
                f.write("|")
        f.write("\n")
    f.close()

    f = open("assigned_rooms.txt", "w")
    assigned_rooms = assign_rooms_to_cleaners(cleaners_data, rooms, hotels)
    for assgn in assigned_rooms:
        for ind, attr in enumerate(assgn):
            f.write(str(attr))
            if ind <len(assgn) - 1:
                f.write("|")
        f.write("\n")
    f.close()

    f = open("bellhop.txt", "w")
    bellhops_data = generate_bellhop(employee_data, hotels)
    for bh in bellhops_data:
        for ind, attr in enumerate(bh):
            f.write(str(attr))
            if ind <len(bh) - 1:
                f.write("|")
        f.write("\n")
    f.close()

    f = open("desk_clerk.txt", "w")
    desk_clerk_data = generate_desk_clerk(employee_data, hotels)
    for dskclr in desk_clerk_data:
        for ind, attr in enumerate(dskclr):
            f.write(str(attr))
            if ind <len(dskclr) - 1:
                f.write("|")
        f.write("\n")
    f.close()

    reservations = generate_reservations(rooms, guests)


    f = open("occupants.txt", "w")
    occupants_array = generate_occupants(reservations)
    if occupants_array:
        for i in occupants_array:
            f.write("|".join(map(str, i)) + "\n")
    else:
        print("No occupants generated.")
    f.close() 

    f = open("reservations.txt", "w")
    for res in reservations:
        for ind, attr in enumerate(res):
            f.write(str(attr))
            if ind < len(res) - 1:
                f.write("|")
        f.write("\n")
    f.close() 

    f = open("occupants.txt", "w")
    occupants_array = generate_occupants(reservations)
    for i in occupants_array:
        for ind, attr in enumerate(i):
            f.write(str(attr))
            if ind < len(i) - 1:
                f.write("|")
        f.write("\n")
    f.close() 

    f = open("reviews.txt", "w")
    reviews = generate_reviews(reservations)
    for rev in reviews:
        for ind, attr in enumerate(rev):
            f.write(str(attr))
            if ind < len(rev) - 1:
                f.write("|")
        f.write("\n")
    f.close()

    f = open("additional_charges.txt", "w")
    additional_charges = generate_additional_charges(reservations)
    for charge in additional_charges:
        for ind, attr in enumerate(charge):
            f.write(str(attr))
            if ind < len(charge) - 1:
                f.write("|")
        f.write("\n")
    f.close()

    f = open("bills.txt", "w")
    bills = make_bill(reservations, guests)
    for b in bills:
        for ind, attr in enumerate(b):
            f.write(str(attr))
            if ind < len(b) - 1:
                f.write("|")
        f.write("\n")
    f.close()

    f = open("billing_history.txt", "w")
    history = generate_billing_history(bills, guests)
    for guest_history in history:
        for ind, attr, in enumerate(guest_history):
            f.write(str(attr))
            if ind < len(guest_history) - 1:
                f.write("|")
        f.write("\n")
    f.close()

    

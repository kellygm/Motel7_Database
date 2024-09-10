--------------------------------------------------------------------------------
-- Group: Motel7
-- Assignment: GP2
-- File name: create.sql
-- Group Members: Thomas C, Gillian K, Colin R, and Sam V
--------------------------------------------------------------------------------

--------------------------------------------------------------------------------
-- Drop Tables 
--------------------------------------------------------------------------------
DROP TABLE IF EXISTS Occupant cascade;
DROP TABLE IF EXISTS Additional_Charges cascade;
DROP TABLE IF EXISTS Billing_History cascade;
DROP TABLE IF EXISTS Bill cascade;
DROP TABLE IF EXISTS Review cascade;
DROP TABLE IF EXISTS DOW_Multiplier cascade;
DROP TABLE IF EXISTS Room_Service cascade;
DROP TABLE IF EXISTS Reservation cascade;
DROP TABLE IF EXISTS Guest cascade;
DROP TABLE IF EXISTS Guest_Status cascade;
DROP TABLE IF EXISTS Room_Features cascade;
DROP TABLE IF EXISTS Hotel_Amenities cascade;
DROP TABLE IF EXISTS Room_Type cascade;
DROP TABLE IF EXISTS Hotel_Season cascade;
DROP TABLE IF EXISTS Season cascade;
DROP TABLE IF EXISTS Assigned_Rooms cascade;
DROP TABLE IF EXISTS Desk_Clerk cascade;
DROP TABLE IF EXISTS Cleaner cascade;
DROP TABLE IF EXISTS Bellhop cascade;
DROP TABLE IF EXISTS Manager cascade;
DROP TABLE IF EXISTS Employee cascade;
DROP TABLE IF EXISTS Room cascade;
DROP TABLE IF EXISTS Hotel cascade;
DROP TABLE IF EXISTS Hotel_phone cascade;

-- additions after GP2
-- Bellhop, Manager, Room_Features, Guest_Status, Billing_History, Additional_Charges
-- DOW_Multiplier, Assigned_Rooms

--------------------------------------------------------------------------------
-- Create Tables
--------------------------------------------------------------------------------

-- the different types of seasons
CREATE TABLE SEASON 
(
    season_name text NOT NULL,
    start_date date NOT NULL,
    end_date date NOT NULL,
    price_multiplier decimal NOT NULL
);

ALTER TABLE SEASON OWNER TO motel7;

-- encapsulation of a hotel
CREATE TABLE HOTEL(
	hotel_id integer Unique NOT NULL,
    address text UNIQUE NOT NULL,
    hotel_name text UNIQUE NOT NULL
--     hotel_ammenities text[]
);

ALTER TABLE HOTEL OWNER TO motel7;


-- Specific season for a specific hotel
CREATE TABLE HOTEL_SEASON(
	hotel_id integer NOT NULL,
	season_name text NOT NULL
);

ALTER TABLE HOTEL_SEASON OWNER TO motel7;

CREATE TABLE HOTEL_PHONE(
	hotel_id integer NOT NULL,
	phone_id integer NOT NULL,
	phone_number text NOT NULL,
	description text NOT NULL
);

ALTER TABLE HOTEL_PHONE OWNER TO motel7;

-- individual room in a hotel
CREATE TABLE ROOM(
    room_number integer,
    room_type text,
    hotel_id integer,
    floor_number integer,
    is_clean boolean,
	occupied boolean
);

ALTER TABLE ROOM OWNER TO motel7;

-- different features based on room type
CREATE TABLE ROOM_FEATURES(
	room_type_id integer not null, -- references room_type features apply to (make foreign key in alter)
	feature_name text not null
);

ALTER TABLE ROOM_FEATURES OWNER TO motel7;

CREATE TABLE HOTEL_AMENITIES(
	hotel_id integer not null,
	amenity_name text not null
);

ALTER TABLE HOTEL_AMENITIES OWNER TO motel7;

-- Price differenation based on day of the week 
CREATE TABLE DOW_MULTIPLIER(
	hotel_id integer NOT NULL,
	dow_name text NOT NULL, -- don't allow repeat names 
	dow_dayweek integer NOT NULL,
	dow_additional_price integer NOT NULL
);

ALTER TABLE DOW_MULTIPLIER OWNER TO motel7;

-- type of room available in a hotel
CREATE TABLE ROOM_TYPE(
	hotel_id integer NOT NULL,
	room_type_id integer unique NOT NULL, -- to map to room features
    room_type text,
    room_size text,
    capacity integer,
    price integer
);

ALTER TABLE ROOM_TYPE OWNER TO motel7;

-- list representation of other things a guest may be charged for during their stay
CREATE TABLE ADDITIONAL_CHARGES(
	name_of_charge text NOT NULL,
	add_price decimal NOT NULL,
	reservation_id integer NOT NULL -- reference to reservation to add charges to
);


ALTER TABLE ADDITIONAL_CHARGES OWNER TO motel7;

-- encapsulation of employees of a hotel
CREATE TABLE EMPLOYEE(
	employee_id integer UNIQUE NOT NULL,
	hotel_id integer NOT NULL,
    employee_name text UNIQUE NOT NULL,
    phone_number text,
    salary bigint NOT NULL
);

ALTER TABLE EMPLOYEE OWNER TO motel7;

-- a type of employee
CREATE TABLE DESK_CLERK(
    employee_id bigint NOT NULL
);

ALTER TABLE DESK_CLERK OWNER TO motel7;

-- a type of employee
CREATE TABLE CLEANER(
    employee_id bigint NOT NULL
--     assigned_rooms bigint[]
);

ALTER TABLE CLEANER OWNER TO motel7;

-- table of assigned rooms for a cleaner
CREATE TABLE ASSIGNED_ROOMS(
	room_number integer NOT NULL,
	room_type text NOT NULL,
	hotel_id integer NOT NULL,
	employee_id bigint NOT NULL
);

ALTER TABLE ASSIGNED_ROOMS OWNER TO motel7;

-- a type of employee
CREATE TABLE BELLHOP(
    employee_id bigint NOT NULL
);

ALTER TABLE BELLHOP OWNER TO motel7;

-- a type of employee that manages other employees at a specific hotel
CREATE TABLE MANAGER(
    employee_id bigint NOT NULL,
	hotel_id integer NOT NULL -- reference the hotel manager works
);

ALTER TABLE MANAGER OWNER TO motel7;

-- someone who is occupying a room/rooms assigned to a specific guest
CREATE TABLE OCCUPANT(
	reservation_id integer not NULL,
	occupant_name varchar(50) NOT NULL
);

ALTER TABLE OCCUPANT OWNER TO motel7;

-- -- additional fee  
-- CREATE TABLE ROOM_SERVICE(
-- 	reservation_id integer unique NOT NULL,
-- 	price decimal
-- );

-- ALTER TABLE ROOM_SERVICE OWNER TO motel7;

-- cost determined based on reservation and guest 
CREATE TABLE BILL(
	bill_id integer UNIQUE NOT NULL,
	reservation_id integer UNIQUE NOT NULL,
	price decimal NOT NULL,
	paid boolean NOT NULL,
	guest_id INTEGER NOT NULL
);

ALTER TABLE BILL OWNER TO motel7;

-- a reservation for a specific hotel associated with a guest 
CREATE TABLE RESERVATION(
	reservation_id integer UNIQUE NOT NULL,
	room_number integer NOT NULL,
	hotel_id integer NOT NULL,
	check_in_date DATE NOT NULL,
	check_out_date DATE NOT NULL,
    room_type text NOT NULL,
	num_of_occupants integer NOT NULL,
	total_cost integer NOT NULL,
	guest_id integer NOT NULL
);

ALTER TABLE RESERVATION OWNER TO motel7;

-- collection of guest_status and discount associated with each type
CREATE TABLE GUEST_STATUS (
	guest_status_str VARCHAR(20) NOT NULL UNIQUE,
	discount integer NOT NULL
);

ALTER TABLE GUEST_STATUS OWNER TO motel7;

-- encapsulation of a guest at a hotel
CREATE TABLE GUEST(
	guest_id integer UNIQUE NOT NULL,
    identification_type text NOT NULL,
    identification_number text NOT NULL,
    address text NOT NULL,
	home_phone_num text,
    mobile_phone_num text NOT NULL,
	guest_status text NOT NULL,
	guest_name text NOT NULL
);

ALTER TABLE GUEST OWNER TO motel7;

-- collection of all bills associated with a specific guest 
CREATE TABLE BILLING_HISTORY(
	guest_id integer NOT NULL,
	bill_id integer NOT NULL,
	bill_price decimal NOT NULL
);

ALTER TABLE BILLING_HISTORY OWNER TO motel7;

-- encapsualtion of a review that a guest may leave for a hotel
CREATE TABLE REVIEW(
	guest_id integer NOT NULL,
    reservation_date DATE NOT NULL,
	display_name varchar(64),
	review_text varchar(500),
	score integer NOT NULL check(score between 1 AND 10)
);

ALTER TABLE REVIEW OWNER TO motel7;

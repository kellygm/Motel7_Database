--------------------------------------------------------------------------------
-- Group: Motel7
-- Assignment: GP2
-- File name: alter.sql
-- Group Members: Thomas C, Gillian K, Colin R, and Sam V
--------------------------------------------------------------------------------
ALTER TABLE HOTEL 
	ADD PRIMARY KEY(hotel_id);
	
ALTER TABLE GUEST 
	ADD PRIMARY KEY(guest_id),
	ADD FOREIGN KEY(guest_status) REFERENCES GUEST_STATUS(guest_status_str); 
	
ALTER TABLE RESERVATION 
	ADD PRIMARY KEY(reservation_id),
	ADD FOREIGN KEY(guest_id) REFERENCES GUEST(guest_id),
	ADD FOREIGN KEY(hotel_id) REFERENCES HOTEL(hotel_id);
  
ALTER TABLE EMPLOYEE 
	ADD PRIMARY KEY(employee_id),
	ADD FOREIGN KEY(hotel_id) REFERENCES HOTEL(hotel_id);

ALTER TABLE DESK_CLERK
	ADD FOREIGN KEY(employee_id) REFERENCES EMPLOYEE(employee_id);
	
-- new
ALTER TABLE MANAGER
	ADD FOREIGN KEY(employee_id) REFERENCES EMPLOYEE(employee_id),
	ADD FOREIGN KEY(hotel_id) REFERENCES HOTEL(hotel_id);
	
ALTER TABLE ROOM_FEATURES
	ADD FOREIGN KEY (room_type_id) REFERENCES ROOM_TYPE(room_type_id);

ALTER TABLE HOTEL_AMENITIES
	ADD FOREIGN KEY(hotel_id) REFERENCES HOTEL(hotel_id);

-- new
ALTER TABLE BELLHOP
	ADD FOREIGN KEY(employee_id) REFERENCES EMPLOYEE(employee_id);
 
ALTER TABLE CLEANER 
	ADD FOREIGN KEY(employee_id) REFERENCES EMPLOYEE(employee_id);

-- Weak entities
ALTER TABLE ROOM
	ADD FOREIGN KEY(hotel_id) REFERENCES HOTEL(hotel_id),
	ADD PRIMARY KEY(room_number, room_type, hotel_id);
	
-- new
ALTER TABLE ASSIGNED_ROOMS
	ADD FOREIGN KEY(employee_id) REFERENCES EMPLOYEE(employee_id),
	ADD FOREIGN KEY(room_number, room_type, hotel_id) REFERENCES ROOM(room_number, room_type, hotel_id);

ALTER TABLE SEASON  
	ADD PRIMARY KEY(season_name);

ALTER TABLE HOTEL_SEASON
	ADD FOREIGN KEY(season_name) REFERENCES SEASON(season_name),
	ADD FOREIGN KEY(hotel_id) REFERENCES HOTEL(hotel_id);

ALTER TABLE OCCUPANT 
	ADD FOREIGN KEY(reservation_id) REFERENCES RESERVATION(reservation_id);

ALTER TABLE BILL
	ADD FOREIGN KEY(guest_id) REFERENCES GUEST(guest_id),
	ADD FOREIGN KEY(reservation_id) REFERENCES RESERVATION(reservation_id);

-- new
ALTER TABLE ADDITIONAL_CHARGES
	ADD FOREIGN KEY(reservation_id) REFERENCES RESERVATION(reservation_id);

-- new
ALTER TABLE BILLING_HISTORY
	ADD FOREIGN KEY(guest_id) REFERENCES GUEST(guest_id),
	ADD FOREIGN KEY (bill_id) REFERENCES BILL(bill_id);

ALTER TABLE DOW_MULTIPLIER
	ADD FOREIGN KEY(hotel_id) REFERENCES HOTEL(hotel_id);
	

ALTER TABLE REVIEW
	ADD FOREIGN KEY(guest_id) REFERENCES GUEST(guest_id);  

ALTER TABLE ROOM_TYPE
	ADD FOREIGN KEY(hotel_id) REFERENCES HOTEL(hotel_id);
	
ALTER TABLE HOTEL_PHONE
	ADD FOREIGN KEY(hotel_id) REFERENCES HOTEL(hotel_id)

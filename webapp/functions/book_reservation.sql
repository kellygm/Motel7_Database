-- Makes a reservation for the selected room_type from table 
DROP FUNCTION IF EXISTS book_reservation(integer, date, date, integer, text, decimal);

CREATE FUNCTION book_reservation(hotel_id integer, beg_date date, end_date date, guest_id integer, room_type_id text, estimated_price decimal)
RETURNS integer AS $$

INSERT INTO reservation
-- need to generate 
VALUES("[reservation_id]", "[room_number]", hotel_id, beg_date, end_date, room_type_id, "[num_occupants]", estimated_price, guest_id)

-- return the reservation_id (needed to assign occupants)
$$ LANGUAGE SQL VOLATILE;

ALTER FUNCTION book_reservation(integer, date, date, integer, text, decimal) OWNER TO motel7;
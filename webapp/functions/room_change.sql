DROP FUNCTION IF EXISTS room_change(hotel_id integer, total decimal);

CREATE FUNCTION room_change(reservation_id integer, total decimal)
RETURNS VOID AS $$

	UPDATE room
    SET occupied = false,
        is_clean = false
    WHERE room.hotel_id = (
        SELECT hotel.hotel_id
        FROM hotel
        JOIN reservation ON reservation.hotel_id = hotel.hotel_id
        WHERE reservation.reservation_id = $1 and reservation.room_number = room.room_number
    );
	insert into BILL (bill_id, reservation_id, price, paid, guest_id)
	VALUES($1, $1, $2, true, (select guest.guest_id from guest join reservation on reservation.guest_id = guest.guest_id
						 where reservation.reservation_id = $1))
	
	
$$ Language SQL VOLATILE strict;

ALTER FUNCTION room_change(reservation_id integer, total decimal) OWNER TO motel7;
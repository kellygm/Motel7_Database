--room
--isoccupied = false
--iscleaned = false

--generate a bill

CREATE OR REPLACE FUNCTION checking_out(reservation_id integer)
RETURNS DECIMAL AS $$
DECLARE
    result DECIMAL;
BEGIN
    SELECT (reservation.check_out_date - reservation.check_in_date) * room_type.price * 
           (100 - guest_status.discount) / 100.0
    INTO result
    FROM reservation
    JOIN guest ON guest.guest_id = reservation.guest_id
    JOIN guest_status on guest.guest_status = guest_status.guest_status_str
    JOIN room_type ON CAST(reservation.room_type AS INT) = room_type.room_type_id
    WHERE reservation.reservation_id = $1
    AND NOT EXISTS (SELECT * from bill where bill_id = $1);

    RETURN result;
END;
$$ LANGUAGE plpgsql STRICT;


ALTER FUNCTION checking_out(reservation_id integer) OWNER TO motel7;
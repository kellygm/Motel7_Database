DROP FUNCTION IF EXISTS dow_finder(hotel_id integer);

CREATE FUNCTION dow_finder(reservation_id integer)
RETURNS decimal AS $$

	SELECT dow_additional_price
	FROM dow_multiplier
	JOIN hotel ON hotel.hotel_id = dow_multiplier.hotel_id
	JOIN reservation ON reservation.hotel_id = hotel.hotel_id
	WHERE reservation.reservation_id = $1 
	AND EXTRACT(DOW FROM reservation.check_in_date) = (dow_multiplier.dow_dayweek - 1);

$$ Language SQL Stable strict;

ALTER FUNCTION dow_finder(reservation_id integer) OWNER TO motel7;
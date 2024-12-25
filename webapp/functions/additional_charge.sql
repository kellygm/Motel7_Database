DROP FUNCTION IF EXISTS additional_charge(hotel_id integer);

CREATE FUNCTION additional_charge(reservation_id integer)
RETURNS decimal AS $$

	select sum(add_price)
	from additional_charges 
	join reservation on reservation.reservation_id = additional_charges.reservation_id
	where reservation.reservation_id = $1;
	$$ Language SQL Stable strict;

ALTER FUNCTION additional_charge(reservation_id integer) OWNER TO motel7;
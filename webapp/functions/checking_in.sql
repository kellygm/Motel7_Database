DROP FUNCTION IF EXISTS checking_in(reservation_id integer);

CREATE FUNCTION checking_in(reservation_id integer)
RETURNS SETOF room AS $$

	select *
	from room
	where hotel_id in (select hotel_id from reservation where reservation_id = $1) 
        and room_type in (select room_type from reservation where reservation_id = $1)
		and is_clean and not occupied
        
$$ LANGUAGE SQL STABLE STRICT;

ALTER FUNCTION checking_in(reservation_id integer) OWNER TO motel7;
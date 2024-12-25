CREATE FUNCTION season_price(reservation_id integer)
RETURNS decimal AS $$

	select price_multiplier
	from season
	join hotel_season on hotel_season.season_name = season.season_name
	join hotel on hotel.hotel_id = hotel_season.hotel_id
	join reservation on reservation.hotel_id = hotel.hotel_id
	where reservation.reservation_id = $1 and extract(month from reservation.check_in_date) between extract(month from season.start_date) and extract(month from season.end_date);

$$ Language SQL Stable strict;

ALTER FUNCTION season_price(reservation_id integer) OWNER TO motel7;
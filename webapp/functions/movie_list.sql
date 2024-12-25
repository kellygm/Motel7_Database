DROP FUNCTION IF EXISTS movie_list(hotel_id integer);

CREATE FUNCTION movie_list(reservation_id integer)
RETURNS setof hotel_movies AS $$

	select hotel_movies.*
	from hotel_movies
	join hotel on hotel.hotel_id = hotel_movies.hotel_id
	join reservation on reservation.hotel_id = hotel.hotel_id
	where reservation.reservation_id = $1
	
$$ LANGUAGE SQL STABLE STRICT;

ALTER FUNCTION movie_list(reservation_id integer) OWNER TO motel7;
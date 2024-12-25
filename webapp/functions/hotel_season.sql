DROP FUNCTION IF EXISTS hotel_season(hotel_id integer);

CREATE FUNCTION hotel_season(hotel_id integer)
RETURNS SETOF room AS $$

	select *
	from hotel_season
    where hotel_id  in (select hotel_id from hotel where hotel_id = $1) 
$$ LANGUAGE SQL STABLE STRICT;

ALTER FUNCTION hotel_season(hotel_id integer) OWNER TO motel7;
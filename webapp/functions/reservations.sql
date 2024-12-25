-- List all available room_types for a specific stay (start date to end date)
-- 
-- Select all room_types avaiable at hotel
-- filter out only rooms that are unoccupied and cleaned 
-- within the range of beg_date to end_date
-- calculate AVERAGE cost per night for each room_type available (cost-per-night / # nights)
-- take into account current season and DOW to adjust cost 
-- apply special discount based on guest_status
-- List all available room_types for a specific stay (start date to end date)
DROP FUNCTION IF EXISTS reservation_search(a_hotel_id integer, a_guest_id integer, beg_date date, end_date date);

CREATE FUNCTION reservation_search(a_hotel_id integer, a_guest_id integer, beg_date date, end_date date)
RETURNS TABLE(room_type text, average_nightly_price decimal) AS $$
	SELECT
		rt.room_type,
		SUM( 
			( (rt.price + dow.dow_additional_price + s.price_multiplier) / ( end_date - beg_date ) ) / (g_stat.discount * 0.1)  
		) AS avg_nightly_price
	FROM
		room r
		JOIN room_type rt ON r.hotel_id = rt.hotel_id -- all room_types available for this hotel
		JOIN guest g ON g.guest_id = a_guest_id 
		JOIN guest_status g_stat ON g_stat.guest_status_str = g.guest_status -- get the guest's discount 
		-- Get hotel season price multiplier
		JOIN hotel_season h_season ON h_season.hotel_id = r.hotel_id
		JOIN season s ON h_season.season_name = s.season_name
		JOIN dow_multiplier dow ON dow.hotel_id = r.hotel_id AND CAST(dow.dow_dayweek AS int) = EXTRACT(DOW FROM beg_date)
		-- JOIN dow_multiplier dow ON dow.hotel_id = r.hotel_id AND dow.dow_dayweek = EXTRACT(DOW FROM beg_date)
	WHERE 
		r.hotel_id = a_hotel_id
		AND r.is_clean = TRUE
		AND r.occupied = FALSE
		AND NOT EXISTS (
			SELECT 1 FROM reservation
			WHERE room_number = r.room_number
			AND hotel_id = r.hotel_id
			AND check_in_date BETWEEN beg_date AND end_date
			AND check_out_date BETWEEN beg_date AND end_date
-- 			AND (check_in_date < beg_date AND check_out_date > end_date)
		)
	GROUP BY
		rt.room_type;
$$ LANGUAGE SQL STABLE;
ALTER FUNCTION reservation_search(hotel_id integer, guest_id integer, beg_date date, end_date date) OWNER TO motel7;
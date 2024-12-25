DROP FUNCTION IF EXISTS additional_insert(movie text, reservation_id integer);

CREATE FUNCTION additional_insert(movie text, reservation_id integer)
RETURNS VOID AS $$

    INSERT INTO additional_charges (name_of_charge, add_price, reservation_id)
    VALUES('Rented Movie', (SELECT hotel_movies.price FROM hotel_movies
                            JOIN hotel ON hotel.hotel_id = hotel_movies.hotel_id
                            JOIN reservation ON reservation.hotel_id = hotel.hotel_id
                            WHERE reservation.reservation_id = reservation_id
                            AND hotel_movies.title = movie), reservation_id)
    
$$ LANGUAGE SQL VOLATILE STRICT;

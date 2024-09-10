
\copy hotel FROM hotels.txt (DELIMITER '|')
\.

\copy phone_numbers FROM phone_numbers.txt (DELIMITER '|')
\.

\copy room_type FROM room_types.txt (DELIMITER '|')
\.

\copy room FROM rooms.txt (DELIMITER '|')
\.

\copy season FROM seasons.txt (DELIMITER '|')
\.

\copy hotel_season FROM hotel_seasons.txt (DELIMITER '|')
\.

\copy guest FROM guests.txt (DELIMITER '|')
\.

--\copy billing_history FROM billing_history.txt (DELIMITER '|') -- Come back too
--\.

--\copy bill FROM bills.txt (DELIMITER '|') -- Come back too
--\.

\copy DOW_multiplier FROM weekily_prices.txt (DELIMITER '|')
\.

\copy employee FROM employee_data.txt (DELIMITER '|')
\.

\copy hotel_amenities FROM hotel_ammenity.txt (DELIMITER '|')
\.

\copy occupant FROM occupants.txt (DELIMITER '|')
\.

\copy reservation FROM reservations.txt (DELIMITER '|')
\.

\copy review FROM reviews.txt (DELIMITER '|')
\.

\copy room_features FROM room_features.txt (DELIMITER '|')
\.

\copy additional_charges from additional_charges.txt (DELIMITER '|')
\.


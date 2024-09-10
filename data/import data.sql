\copy hotel FROM hotels.txt (DELIMITER '|')
\.

\copy phone_numbers FROM phone_numbers.txt (DELIMITER '|')
\.

\copy room_type FROM room_types.txt (DELIMITER '|')
\.

\copy room FROM rooms.txt (DELIMITER '|')
\.
--Broken season import do not use
--\copy season FROM seasons.txt (DELIMITER '|')
--\.

\copy hotel_season FROM \hotel_seasons.txt (DELIMITER '|')
\.

\copy guest FROM \guests.txt (DELIMITER '|')
\.

\copy review FROM \reviews.txt (DELIMITER '|')
\.

\copy reservation FROM \reservations.txt (DELIMITER '|')
\.
-- helper function that is called to allow the person booking the reservation
-- to add an occupant to a reservation 

DROP FUNCTION IF EXISTS assign_occupants(integer, text, integer);
CREATE FUNCTION assign_occupants(reservation_id integer, occupant_name text, num_people integer)
RETURNS integer AS $$

-- create an occupant
INSERT INTO occupant()
VALUES(reservation_id, occupant_name)
-- update the reservation attr num_occupants accordingly

-- return the COUNT() of occupants with passed reservation_id
ALTER FUNCTION assign_occupants(reservation_id integer, occupant_name text, num_people integer)

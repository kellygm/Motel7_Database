# Database

# GP2 Submission

## File Contents 

* create.sql -- drops and creates all tables
* alter.sql -- adds all primary and foreign keys
* eer_model.png -- EER diagram from [draw.io](https://www.drawio.com/)
* rel_model.pgerd -- relational ERD (pgAdmin)

## Building the database 

Define environment variables:

```
sh
export PGHOST=data.cs.jmu.edu
export PGDATABASE=motel7
export PGUSER=jmu_username
export PGPASSWORD=student_number
```
Run the following commands:

```
sh
psql < create.sql
psql < alter.sql
```

## Changes to EER model
While mapping EER to relational, we made the following changes:
  *  decided that a reservation for a single room_type and that the room number is determined upon check-in
  *  a guest may have multiple reservations if booking more than one room
  *  added a gust_id to the BILL table to link all reservations needing to be paid by the guest (to accomodate for the changes to reservation's behavior)

## Relational model notes
  * decided that the 'review_text' for a review could be 'NULL' in case a guest just wants to leave a rating (1-10)
  * added start and end dates for 'hotel_season' to specify when a specific starts for a certain hotel
  *  decided that the 'date' for a review will be the check-out date (instead of creatin a date range from check-in to check-out date)
  *  added 'hotel_id' column to employee table (needed as relationship between employee and hotel they work at)

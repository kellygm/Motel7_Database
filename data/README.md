#Data

#GP3 Submission

# Data Creation

We used a combination of Python along with utilizing the Faker package to generate our data. Each table in our database has at least one function associated with generating random data for it. Each function outputted a list of string objects, each of which had attribtues that aligned with a relevant column of the table they are generating the data for. Information was added to individual string objects using the "append()" method and comments are placed to the side of each one to specify what information is being appended (i.e. reservation_id, price, etc.) to show its relation to a column. We used appropriate and realisitc data values for all of our inputs and confirmed that all files generated used the same format structure and field and line delimiters. The main function is where all of the writing to the various text files happens. We decided to make our text files inclusive to all values in the lists to force uniqueness in the randomization. The text files can be filtered or split to only display data that meets a desired criteria (i.e. get the billing history for a single guest by filtering for their guest_id in the billing_history.txt).

# Text Files
* billing_history.txt -- shows the billing history for every exisiting guest the hotel
* bills.txt -- shows a single bill associated with a reservation
* employees_data.txt -- this file contains the information for each employee that is working at a specific motel7
* guest.txt -- a list of all guests and their account information that have or are currently staying at one of the hotels in the motel7 chain
* hotel_ammenity.txt -- lists the ammenities of each hotel
* hotel_seasons.txt -- This file contains the data for the connecting table between hotel and season to model the many to many relationship
* hotels.txt -- this file showcases all the hotels and their associated attributes in the motel7 chain
* occupants.txt -- provides a list of occupants and where they are staying
* phone_numbers.txt -- lists all the phone numbers associated with any of the hotels in the motel7 chain
* reservations.txt -- shows all reservations for every hotel in the motel7 chain 
* reviews.txt -- shows all reviews left by guests and when their most recent stay at one of the motel7 hotels was
* room_features.txt -- lists the features associated with each room type
* room_types -- lists all the different room types that could be available at one of the motel7 chains
* rooms.txt -- lists the specific rooms and their room types for a specific hotel
* seasons.txt -- lists all the seasons that may impact price and availability across the motel7 chain
* weekily_prices.txt -- shows the price multipler per room type for every day of the week, labeled 1-7 (i.e. 1 is Monday)


# Py Files
```
generate.py -- encapsulation of generating all the data and outputting it to the various text files
```


# SQL Files
```
load.sql -- This file contains all the psql commands necesarry to import the data from the text files into the data base
```


# Changes made to Relational Model from GP2
While reviewing our work from GP2, we made the following changes before we began GP3:
  * added a table 'Room_Features' to represent a list of special features associated with a specific room type
  * added the table 'Guest_Status' to house the different statuses a guest can hold, and the discount associated with them
  * added the table 'Billing_History' to keep a record of all past stays at a hotel for a specific guest
  * added the table 'DOW_Multiplier' which determines any up-charges placed on each room type based on the day of the week
  * added the table 'Assigned_Rooms' to represent a list of rooms that a cleaner employee is assigned to clean
  * added the table 'Additional_Charges' which keeps track of any services that a guest could be charged for during their stay
  * added the table 'Hotel_Ammenities' to represent a lsit of ammenities a specific hotel has to offer
  * added more employees types 'Bellhop' and 'Manager'. 'Bellhop' takes guests bags to their room, and a 'Manager' manages the employees at a specific hotel

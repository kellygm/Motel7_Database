from faker import Faker

def generate_fake_data(num_hotels, num_movies_per_hotel):
    fake = Faker()
    data = []

    for hotel_id in range(1, num_hotels + 1):
        movie_titles = set()  # To ensure unique movie titles per hotel
        for _ in range(num_movies_per_hotel):
            while True:
                title = fake.random_element(["The Shawshank Redemption", "Inception", "Pulp Fiction",
                                             "The Dark Knight", "Forrest Gump", "Fight Club",
                                             "The Matrix", "Gladiator", "Braveheart",
                                             "The Lord of the Rings: Fellowship of the Ring",
                                             "The Lion King", "The Avengers", "Titanic",
                                             "The Social Network", "The Revenant"])
                if title not in movie_titles:
                    movie_titles.add(title)
                    break

            rating = fake.pydecimal(left_digits=1, right_digits=1, positive=True, min_value=1, max_value=5)
            runtime = fake.random_int(min=60, max=180)  # Assuming runtime in minutes
            price = fake.pydecimal(left_digits=2, right_digits=2, positive=True)

            data.append(f"{hotel_id}|{title}|{rating}|{runtime}|{price}")

    return data

if __name__ == "__main__":
    num_hotels_to_generate = 20
    num_movies_per_hotel = 5
    fake_data = generate_fake_data(num_hotels_to_generate, num_movies_per_hotel)

    # Save data to a tab-delimited text file
    with open("hotel_movies_data.txt", "w") as file:
        for record in fake_data:
            file.write(record + "\n")

    print(f"{num_hotels_to_generate} hotels with {num_movies_per_hotel} movies each saved to 'hotel_movies_data.txt'.")



# DROP TABLE IF EXISTS Hotel_Movies cascade;

# CREATE TABLE Hotel_Movies 
# (
# 	hotel_id integer NOT NULL,
#     title text NOT NULL,
#     rating decimal NOT NULL,
#     runtime integer NOT NULL,
#     price decimal NOT NULL
# );
# ALTER TABLE Hotel_Movies OWNER TO motel7;

# ALTER TABLE Hotel_Movies
# 	ADD FOREIGN KEY(hotel_id) REFERENCES HOTEL(hotel_id);

class MoviesSystem:
    def __init__(self, name, id, category, avail_seats, price):
        self.name = name
        self.id = id
        self.category = category
        self.avail_seats = avail_seats
        self.price = price

    def dis(self):
        print(self.name, self.id, self.category, self.avail_seats, self.price)


def view_all_movies(movies):
    if not movies:
        print(" No movies available.")
        return
    print("\nAvailable Movies ")
    for movie in movies:
        movie.dis()


def add_movie(movies):
    movie_id = int(input("Enter Movie ID: "))
    name = input("Enter Movie Name: ")
    category = input("Enter Category: ")
    seats = int(input("Enter Available Seats: "))
    price = float(input("Enter Ticket Price: "))
    movie = MoviesSystem(name, movie_id, category, seats, price)
    movies.append(movie)
    print("Movie added successfully!")


def search_movie(movies):
    movie_id = int(input("Enter Movie ID to search: "))
    for movie in movies:
        if movie.id == movie_id:
            print("Movie found!")
            print("ID:", movie.id)
            print("Name:", movie.name)
            return
    print("Movie not found.")


def book_ticket(movies, movie_id, seats_to_book):
    for movie in movies:
        if movie.id == movie_id:
            if movie.avail_seats >= seats_to_book:
                movie.avail_seats -= seats_to_book
                total_price = seats_to_book * movie.price
                print(f" Success! Booked {seats_to_book} ticket(s) for '{movie.name}'. Total: ${total_price:.2f}")
            else:
                print(f" Error: Only {movie.avail_seats} seats available.")
            return
    print(" Error: Movie ID not found.")


def cancel_ticket(movies):
    movie_id = int(input("Enter Movie ID: "))
    tickets = int(input("Enter number of tickets to cancel: "))
    for movie in movies:
        if movie.id == movie_id:
            movie.avail_seats += tickets
            print("Ticket cancelled successfully!")
            return
    print("Movie not found.")


def save_data(movies):
    with open("movies.txt", "w") as f:
        for movie in movies:
            line = f"{movie.id},{movie.name},{movie.category},{movie.avail_seats},{movie.price}\n"
            f.write(line)
    print("Data saved to", "movies.txt")


def main():
    m1 = MoviesSystem("Harry poter", 125, "Drama", 50, 200)
    m2 = MoviesSystem("Avatar", 245, "Action", 100, 50)
    movies_list = [m1, m2]

    while True:
        print("\n1. View All Movies")
        print("2. Add Movie")
        print("3. Search Movie")
        print("4. Book Ticket")
        print("5. Cancel Ticket")
        print("6. Save Data")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            view_all_movies(movies_list)
        elif choice == "2":
            add_movie(movies_list)
        elif choice == "3":
            search_movie(movies_list)
        elif choice == "4":
            movie_id = int(input("Enter Movie ID: "))
            seats = int(input("Enter number of seats to book: "))
            book_ticket(movies_list, movie_id, seats)
        elif choice == "5":
            cancel_ticket(movies_list)
        elif choice == "6":
            save_data(movies_list)
        elif choice == "7":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")


main()
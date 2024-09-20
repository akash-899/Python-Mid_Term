from datetime import datetime 

class Star_Cinema:
    _hall_list = []

    @classmethod
    def entry_hall(cls,hall):
        cls._hall_list.append(hall)

class Hall(Star_Cinema):
    def __init__(self,rows,cols,hall_no) -> None:
        super().__init__()
        self.__seats = {}
        self.__show_list = []
        self._rows = rows
        self._cols = cols
        self.__hall_no = hall_no

        Star_Cinema._hall_list.append(self)


    def entry_show(self,show_id,movie_name,time,date):
        show_info = (show_id,movie_name,time,date)
        self.__show_list.append(show_info)

        seat_allocation =[["Free" for _ in range(self._cols)] for _ in range(self._rows)]
        self.__seats[show_id] = seat_allocation

    
    def book_seats(self,show_id):
        if show_id not in self.__seats:
            print(f"Error: Show Id {show_id} does not exist!")
            return
        
        seat_map = self.__seats[show_id]

        try:
            num_tickets = int(input("Enter number of tickets: "))
        except ValueError:
            print("Invalid input. Please Enter a valid input")
            return
        
        for i in range(num_tickets):
            try:
                row = int(input("Enter Seat Row: "))
                col = int(input("Enter Seat Col: "))
            except ValueError:
                print("Invalid input. Please enter valid numbers for row and column.")
                continue

            if row < 0 or row >= self._rows or col < 0 or col >= self._cols:
                print(f"Seat ({row},{col}) is out of seat limit!")
                continue

            if seat_map[row][col] == "Free":
                seat_map[row][col] = "Booked"
                print(f"Seat ({row},{col}) successfully booked!")

            else:
                print(f"Error: Seat ({row},{col}) is already booked!)")

            

    def view_show_list(self):

        if not self.__show_list:
            print("No Show Running")
            return
        
        print(f"Shows Running in Hall {self.__hall_no}: ")

        for show_id,movie_name,time,date in self.__show_list:
            print(f"Show ID: {show_id}, Movie: {movie_name}, Time: {time}, Date: {date}")


    
    def view_available_seats(self,show_id):
        if show_id not in self.__seats:
            print(f"Error: Show ID {show_id} does not exist !")
            return
        

        seat_map = self.__seats[show_id]

        print(f"\nAvailable seats for Show ID {show_id} in Hall {self.__hall_no}: \n\t")

        available_seats = []

        for row in range(self._rows):
            for col in range(self._cols):
                if seat_map[row][col] == "Free":
                    available_seats.append((row,col))

        
        if not available_seats:
            print("No available seats !")

        else:
            for row,col in available_seats:
                print(f"Seat ({row},{col}) is available!")

    
    def view_shows_today(self):
        today = datetime.now().date()
        shows_today = [(show_id, movie_name, time) for show_id, movie_name, time, date in self.__show_list if date == today]

        if shows_today:
            print(f"Shows scheduled for today in Hall {self.__hall_no}:")
            for show_id, movie_name, time in shows_today:
                print(f"Show ID: {show_id}, Movie: {movie_name}, Time: {time}")
        else:
            print("No shows scheduled for today.")




class CinemaCounter:

    def __init__(self,hall) -> None:
        self.hall = hall

    def view_running_shows(self):
        self.hall.view_show_list()

    def view_seats(self,show_id):
        self.hall.view_available_seats(show_id)

    def book_tickets(self,show_id):
        self.hall.book_seats(show_id)

    def view_shows_today(self):
        self.hall.view_shows_today()


hall1 = Hall(10, 20, "H1")
today = datetime.now().date()
hall1.entry_show(1, "House of The Dragon", "18:00", today)
hall1.entry_show(2, "Game Of Thrones", "20:30", today)
hall1.entry_show(3, "Lord of Rings", "15:00", today)


counter = CinemaCounter(hall1)


while True:
    print("\nWelcome to Star Cinema!")
    print("1. View All Shows Today")
    print("2. View Available Seats")
    print("3. Book Tickets")
    print("4. Exit")

    ch = int(input("Enter Option: "))

    if ch == 1 :
        counter.view_shows_today()

    elif ch == 2:
        show_id = int(input("Enter Id: "))
        counter.view_seats(show_id)
    
    elif ch == 3:
        show_id = int(input("Enter Id: "))
        counter.book_tickets(show_id)

    elif ch == 4:
        print("Thank you for visiting Star Cinema!")
        break












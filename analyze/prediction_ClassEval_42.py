class Hotel:
    def __init__(self, name, rooms):
        self.name = name
        self.available_rooms = rooms
        self.booked_rooms = {}

    def book_room(self, room_type, room_number, name):
        if not self.is_room_type_available(room_type):
            return False

        if self.is_room_available(room_type, room_number):
            self.add_booking(room_type, room_number, name)
            return "Success!"
        elif self.available_rooms[room_type] != 0:
            return self.available_rooms[room_type]
        else:
            return False

    def is_room_type_available(self, room_type):
        return room_type in self.available_rooms

    def is_room_available(self, room_type, room_number):
        return room_number <= self.available_rooms[room_type]

    def add_booking(self, room_type, room_number, name):
        if room_type not in self.booked_rooms:
            self.booked_rooms[room_type] = {}
        self.booked_rooms[room_type][name] = room_number
        self.available_rooms[room_type] -= room_number

    def check_in(self, room_type, room_number, name):
        if not self.is_room_booked(room_type, name):
            return False
        if self.is_correct_room_number(room_type, name, room_number):
            self.remove_booking(room_type, name)
        else:
            self.decrease_booked_room_number(room_type, name, room_number)

    def is_room_booked(self, room_type, name):
        return room_type in self.booked_rooms and name in self.booked_rooms[room_type]

    def is_correct_room_number(self, room_type, name, room_number):
        return room_number == self.booked_rooms[room_type][name]

    def remove_booking(self, room_type, name):
        self.booked_rooms[room_type].pop(name)

    def decrease_booked_room_number(self, room_type, name, room_number):
        self.booked_rooms[room_type][name] -= room_number

    def check_out(self, room_type, room_number):
        if room_type in self.available_rooms:
            self.available_rooms[room_type] += room_number
        else:
            self.available_rooms[room_type] = room_number

    def get_available_rooms(self, room_type):
        return self.available_rooms[room_type]
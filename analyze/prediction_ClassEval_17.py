from datetime import datetime, timedelta

class CalendarUtil:
    def __init__(self):
        self.events = []

    def add_event(self, event):
        self.events.append(event)

    def remove_event(self, event):
        if event in self.events:
            self.events.remove(event)

    def get_events(self, date):
        return [event for event in self.events if event['date'].date() == date.date()]

    def is_available(self, start_time, end_time):
        return all(not (start_time < event['end_time'] and end_time > event['start_time']) for event in self.events)

    def get_available_slots(self, date):
        available_slots = []
        start_time = self._start_of_day(date)
        end_time = self._end_of_day(date)

        while start_time < end_time:
            slot_end_time = start_time + timedelta(minutes=60)
            if self.is_available(start_time, slot_end_time):
                available_slots.append((start_time, slot_end_time))
            start_time += timedelta(minutes=60)

        return available_slots

    def get_upcoming_events(self, num_events):
        now = datetime.now()
        upcoming_events = [event for event in self.events if event['start_time'] >= now]
        return upcoming_events[:num_events]

    def _start_of_day(self, date):
        return datetime(date.year, date.month, date.day, 0, 0)

    def _end_of_day(self, date):
        return datetime(date.year, date.month, date.day, 23, 59)
class Event:
    def __init__(self, name, date):
        self.name = name
        self.date = date
        self.participants = []

    def add_participants(self, new_participant):
        count = len(self.participants)
        self.participants.append(new_participant)
        count+=1
        print(count)

    def count_participants(self):
        count = len(self.participants)
        print(count)

events = {}

def add_event(name, date, participants)
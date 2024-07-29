class Event:
    def __init__(self, name, date, participants):
        self.name = name
        self.date = date
        participantslist = []
        participantslist.append(participants)
        self.participants = participantslist

    def add_participants(self, new_participant):
        count = len(self.participants)
        self.participants.append(new_participant)
        count+=1
        print(self.participants, count)

    def count_participants(self):
        count = len(self.participants)
        print(count)

events = {}

def add_event(name, date, participants):
    events[name]= Event(name, date, participants)
    print(f"Event {name} on date {date} has been added to Events with participants {participants}")

def new_guest(name, guest):
    if name in events:
        events[name].add_participants(guest)

add_event("Juice Party", "12/25/24", "Anne")
add_event("Brownie Party", "12/26/24", "Jeff")
new_guest("Juice Party", "Frank")


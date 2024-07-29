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

    def count_participants(self):
        count = len(self.participants)
        print(count)

events = {}

def add_event(name, date, participants):
    events[name]= Event(name, date, participants)
    print(f"Event {name} on date {date} has been added to Events with participants {participants}")


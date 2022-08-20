class Event:
    def __init__(self, event_date, event_type, machine_name, user):
        self.date = event_date
        self.type = event_type
        self.machine = machine_name
        self.user = user
        
events =[
    Event("2020-01-27 11:45:56", "login", "myworkstation.local", "jordan"),
    Event("2020-02-26 12:45:56", "login", "webserver.local", "lane"),
    Event("2020-03-25 13:45:56", "login", "webserver.local", "jordan"),
    Event("2020-04-31 15:45:56", "login", "mailserver.local", "chris"),
    Event("2020-05-21 17:45:56", "login", "myworkstation.local", "jordan"),
    Event("2020-06-11 18:45:56", "login", "mailserver.local", "jane")
]

def get_event_date(event):
    return event.date

def current_users(events):
    events.sort(key=get_event_date)
    machines = {}
    for event in events:
        if event.machine not in machines:
            machines[event.machine] = set()
        if event.type == "login":
            machines[event.machine].add(event.user)
        elif event.type == "logout":
            machines[event.machine].remove(event.user)
    return machines

def generate_report(machines):
    for machine, users in machines.items():
        if len(users) > 0:
            user_list = ", ".join(users)
            print("{}: {}".format(machine,user_list))
            
users = current_users(events)
print(users)

generate_report(users)
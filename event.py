class Event(object):
    event_time
    event_type
    last_event
    next_event
    def __init__(self, event_time, event_type, last_event, next_event):
        self.event_time = event_time
        self.event_type = event_type
        self.last_event = last_event
        self.next_event = next_event

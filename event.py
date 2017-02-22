class Event(object):
    def __init__(self, event_time, packet, event_type, prev_event, next_event):
        self.event_time = event_time
        self.packet = packet
        self.event_type = event_type
        self.prev_event = prev_event
        self.next_event = next_event

import queue
from .event import Event

# MAXBUFFER = int(input("Please enter the MAXBUFFER size for the packets queue: "))
# service_rate = int(input("Please enter the service rate: "))
# arrival_rate = int(input("Please enter the arrival rate: "))

# initialize
event_type = {"a":"arrival","d":"departure"}
MAXBUFFER = 20
event_id = 0
service_rate = 1
arrival_rate = 1
time = 0
packets_queue_length = 0
packets_queue = queue.Queue()
global_event_list = queue.PriorityQueue()

# create new event and insert into GEL
event_time = time
event = Event(event_time,event_type["a"],event_id)
event_id += 1
global_event_list.put(event_time, event)

for i in 100000:
    # 1. get the first event from the GEL;
    first_event = global_event_list.get()
    if first_event.event_type == event_type["a"]:
        #process-arrival-event
    else:
        #process-service-completion

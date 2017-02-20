import queue
import event
import random
from math import log

# initialize
# MAXBUFFER = int(input("Please enter the MAXBUFFER size for the packets queue: "))
# rate = int(input("Please enter the service rate: "))
event_type = {"a":"arrival","d":"departure"}
MAXBUFFER = 20
event_id = 0
time = 0
packets_queue_length = 0
packets_queue = queue.Queue()
global_event_list = queue.PriorityQueue()
rate = 1

def generate_arrival_rate():
    u = random.random()
    return ((-1/rate)*log(1-u));
def generate_offset_time():
    u = random.random()
    return ((-1/rate)*log(1-u));

# statistics
server_busy_time = 0
queue_length_sum = 0
packets_count = 0
packets_drop = 0

# create new event and insert into GEL
event_time = time + generate_offset_time()
event = Event(event_time,event_type["a"],event_id)
event_id += 1
global_event_list.put(event_time, event)

for i in 100000:
    # 1. get the first event from the GEL;
    first_event = global_event_list.get()
    # the first event is arrival event
    if first_event.event_type == event_type["a"]:
        # schedule the next arrival event
        time = event_time
        event_time = time + generate_offset_time()
        event = Event(event_time,event_type["a"],event_id)
        event_id += 1
        global_event_list.put(event_time, event)
        # process-arrival-event
        if packets_queue_length == 0:
            # Get the service time of the packet.
            # Create a departure event at time which is equal to the current time plus the service time of the packet.
            # Insert Event
        else:
            if packets_queue_length - 1 < MAXBUFFER:
                #  Put the packet into the queue
            else:
                # Queue is full
                # drop the packet; record a packet drop.
                # Since this is a new arrival event, we increment the length.
                # Update statistics which maintain the mean queue-length and the server busy time
    # the first event is departure event
    else:
        # process-service-completion
        time = event_time
        # Update statistics which maintain the mean queue-length and the server busy time
        # Since this is a packet departure, we decrement the length.
        if packets_queue_length > 0:
            # Dequeue the first packet from the buffer;
            # Create a new departure event for a time which is the current time plus the time to transmit the packet.
            # Insert the event at the right place in the GEL.

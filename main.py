import event
import packet
import GEL

import random
import queue
from math import log

# initialize
# MAXBUFFER = int(input("Please enter the MAXBUFFER size for the packets queue: "))
# rate = int(input("Please enter the service rate: "))
MAXBUFFER = 20
rate = 1
current_time = 0
packets_queue_length = 0
packets_queue = queue.Queue(MAXBUFFER)
global_event_list = None

def generate_arrival_rate():
    u = random.random()
    return ((-1/rate)*log(1-u));
def generate_service_rate():
    u = random.random()
    return ((-1/rate)*log(1-u));

# statistics
server_busy_time = 0
packets_queue_length_sum = 0
packets_count = 0
packets_drop = 0

global_event_list = GEL.scheduleNextArrival(global_event_list, generate_service_rate(), generate_arrival_rate(), current_time)

for i in range(100000):
    # 1. get the first event from the GEL;
    first_event = GEL.popGEL(global_event_list)
    current_time = first_event.event_time
    # the first event is arrival event
    if first_event.event_type == "arrival":
        # schedule the next arrival event
        global_event_list = GEL.scheduleNextArrival(global_event_list, generate_arrival_rate(), generate_service_rate(), current_time)
        # process-arrival-event
        # Queue is empty
        if packets_queue.empty():
            # Get the service time of the packet.
            service_time = current_time + generate_service_rate()
            # Create a departure event at time which is equal to the current time plus the service time of the packet.
            # Insert Event
            global_event_list = GEL.scheduleNextDeparture(global_event_list, first_event.packet, service_time, current_time)
        # Queue is full
        elif packets_queue.full():
            # drop the packet; record a packet drop.
            packets_drop += 1
            # Since this is a new arrival event, we increment the length.
            packets_queue_length += 1
            # Update statistics which maintain the mean queue-length and the server busy time
            # TODO: server busy time
            packets_queue_length_sum += packets_queue_length
            packets_count += 1
        else:
            #  Put the packet into the queue
            packets_queue.put(first_event.packet)
            # Since this is a new arrival event, we increment the length.
            packets_queue_length += 1
            # Update statistics which maintain the mean queue-length and the
            # TODO: server busy time
            packets_queue_length_sum += packets_queue_length
            packets_count += 1
    # the first event is departure event
    else:
        # process-service-completion
        # Update statistics which maintain the mean queue-length and the server busy time
        # Since this is a packet departure, we decrement the length.
        packets_queue_length -= 1
        if not packets_queue.empty():
            # Dequeue the first packet from the buffer;
            packet = packets_queue.get()
            global_event_list = GEL.scheduleNextDeparture(global_event_list, packet, packet.transmit_time, current_time)
            # Create a new departure event for a time which is the current time plus the time to transmit the packet.
            # Insert the event at the right place in the GEL.

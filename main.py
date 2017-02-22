import event
import packet
import GEL

import random
import queue
from math import log

# initialize
# MAXBUFFER = int(input("Please enter the MAXBUFFER size for the packets queue: "))
# service_rate = int(input("Please enter the service rate: "))
# arrival_rate = int(input("Please enter the arrival rate: "))
MAXBUFFER = 1
service_rate = 1
arrival_rate = 3
current_time = 0
active_packets_length = 0
packets_queue = queue.Queue(MAXBUFFER)
global_event_list = None

def generate_arrival_time():
    u = random.random()
    return ((-1/arrival_rate)*log(1-u));
def generate_service_time():
    u = random.random()
    return ((-1/service_rate)*log(1-u));

# statistics
server_busy_time_start = 0
server_busy_time_end = 0
server_busy_time = 0
packets_queue_length_sum = 0
packets_count = 0
packets_drop = 0

global_event_list = GEL.scheduleNextArrival(global_event_list, generate_service_time(), generate_arrival_time(), current_time)

for i in range(100000):
    # 1. get the first event from the GEL;
    (first_event, global_event_list) = GEL.popGEL(global_event_list)
    current_time = first_event.event_time
    # the first event is arrival event
    if first_event.event_type == "arrival":
        # schedule the next arrival event
        global_event_list = GEL.scheduleNextArrival(global_event_list, generate_arrival_time(), generate_service_time(), current_time)
        # process-arrival-event
        # Queue is empty
        if active_packets_length == 0:
            # Get the service time of the packet.
            service_time = first_event.packet.service_time
            # Create a departure event at time which is equal to the current time plus the service time of the packet.
            # Insert Event
            global_event_list = GEL.scheduleNextDeparture(global_event_list, first_event.packet, service_time, current_time)
            packets_queue_length_sum += active_packets_length
            packets_count += 1
            active_packets_length += 1
        elif active_packets_length - 1 < MAXBUFFER:
            #  Put the packet into the queue
            packets_queue.put(first_event.packet)
            # Since this is a new arrival event, we increment the length.
            # packets_queue_length += 1
            # Update statistics which maintain the mean queue-length and the
            packets_queue_length_sum += active_packets_length
            packets_count += 1
            active_packets_length += 1
        # Queue is full
        else:
            # drop the packet; record a packet drop.
            packets_drop += 1
            # Since this is a new arrival event, we increment the length.
            # Update statistics which maintain the mean queue-length and the server busy time
            server_busy_time_start = current_time
            packets_queue_length_sum += active_packets_length
            packets_count += 1
    # the first event is departure event
    else:
        # process-service-completion
        # Update statistics which maintain the mean queue-length and the server busy time
        # Since this is a packet departure, we decrement the length.
        if server_busy_time_start > 0:
            server_busy_time += (current_time - server_busy_time_start)
            server_busy_time_start = 0
        active_packets_length -= 1
        if active_packets_length > 0:
            packet = packets_queue.get()
            # Dequeue the first packet from the buffer;
            # Create a new departure event for a time which is the current time plus the time to transmit the packet.
            # Insert the event at the right place in the GEL.
            global_event_list = GEL.scheduleNextDeparture(global_event_list, packet, packet.service_time, current_time)

print("server utilization:")
print(server_busy_time/current_time)
print("mean queue length:")
print(packets_queue_length_sum/packets_count)
print(packets_drop)

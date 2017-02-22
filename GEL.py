import packet
import event

def insertGEL(global_event_list, new_event):
    if global_event_list == None:
        global_event_list = new_event
    else:
        event = global_event_list
        next_event = event.next_event
        while next_event != None || new_event.event_time > next_event.event_time:
            event = event.next_event
            next_event = event.next_event
        event.next_event = new_event
        new_event.prev_event = event
        new_event.next_event = next_event
        if next_event != None:
            next_event.prev_event = new_event


def popGEL(global_event_list):
    first_event = global_event_list
    first_event.next_event.prev_event = None
    global_event_list = first_event.next_event
    return first_event

def scheduleNextArrival(global_event_list, arrival_time, service_time, current_time):
    new_packet = Packet(service_time)
    new_event = Event(current_time + arrival_time, new_packet, event_type["a"], None, None)
    insertGEL(global_event_list,new_event)

def scheduleNextDeparture(global_event_list, packet, service_time, current_time):
    new_event = Event(current_time + service_time, packet, event_type["d"], None, None)
    insertGEL(global_event_list,new_event)

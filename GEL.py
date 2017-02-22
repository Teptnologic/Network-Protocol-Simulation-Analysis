import packet
import event

def insertGEL(global_event_list, new_event):
    if global_event_list == None:
        global_event_list = new_event
    else:
        event = global_event_list
        next_event = event.next_event
        while next_event != None and new_event.event_time > next_event.event_time:
            event = event.next_event
            next_event = event.next_event
        event.next_event = new_event
        new_event.prev_event = event
        new_event.next_event = next_event
        if next_event != None:
            next_event.prev_event = new_event
    return global_event_list


def popGEL(global_event_list):
    first_event = global_event_list
    if first_event.next_event != None:
        first_event.next_event.prev_event = None
    global_event_list = first_event.next_event
    return first_event

event_type = {"a":"arrival","d":"departure"}

def scheduleNextArrival(global_event_list, arrival_time, service_time, current_time):
    new_packet = packet.Packet(service_time)
    new_event = event.Event(current_time + arrival_time, new_packet, event_type["a"], None, None)
    global_event_list = insertGEL(global_event_list,new_event)
    print("insert arrival event")
    return global_event_list

def scheduleNextDeparture(global_event_list, packet, service_time, current_time):
    new_event = event.Event(current_time + service_time, packet, event_type["d"], None, None)
    global_event_list = insertGEL(global_event_list,new_event)
    print("insert departure event")
    return global_event_list

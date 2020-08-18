#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    # Your code here
    route = []
    source = " "
    destination = " "
    for source, destination in tickets:
        if tickets[source] == None:
            tickets[source].items()
    print(tickets[source])
        # elif:
        #     tickets[destination +1]
        # else route.append(tickets[destination] == None)
    
    return route

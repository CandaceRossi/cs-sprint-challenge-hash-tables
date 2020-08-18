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
    solution = {}
    # l = len(tickets)
    route = [None] * length
    # source = " "
    # destination = " "
    for ticket in range(length):
        print(route[ticket])
        if tickets[ticket].source == "NONE":
            print(tickets[ticket].source)
            route[0] = tickets[ticket].destination

        solution[tickets[ticket].source] = tickets[ticket].destination

    for ticket in range(length):
        if route[ticket-1]:
            print(route[ticket-1])
            route[ticket] = solution[route[ticket-1]]
    return route

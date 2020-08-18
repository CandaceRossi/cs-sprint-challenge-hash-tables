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
    l = len(tickets)
    route = []
    source = " "
    destination = " "
    for ticket in tickets:
        if ticket not in solution:
            solution[ticket] = []

        if ticket.source == None:
            route.append(ticket)
        if ticket.source == None:
            route.append(ticket)

    for i in range(l - 1):
        current_ticket = tickets[i]
        route[current_ticket].append(tickets[i].destination)
    #     if ticket.destination == None:
    #         route.append(ticket.items())
    #     else:
    #         route.append(ticket.items())
    # for i in range(l - 1):
    #     current_ticket = ticket[i]
    #     solution[current_ticket].append(ticket[i])
    # for source, destination in tickets:
    #     if tickets[source] == None:
    #         route.append(tickets[source].items())
    #     if
    # print(ticket[source])
    # elif:
    #     tickets[destination +1]
    # else route.append(tickets[destination] == None)

    return route

class Event:
    def __init__(self, id, x, y, prices):
        self.id = id
        self.x = x
        self.y = y
        self.prices = prices

    def buyTicket(self):
        if self.isTicketAvailable:
            self.prices.pop(0)

    def isTicketAvailable(self):
        return self.prices != []


class Buyer:
    def __init__(self, id, x, y):
        self.id = id
        self.x = x
        self.y = y


def manhattan_distance(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)

sizeOfWorld = int(input())

resultList = list()
numberOfEvents = int(input())
listOfEvents = list()

for i in range(numberOfEvents):
    eventLine = input().split()

    eventId = int(eventLine[0])
    eventX = int(eventLine[1])
    eventY = int(eventLine[2])
    eventPrices = [int(i) for i in eventLine[3:]]
    eventPrices.sort()

    listOfEvents.append(Event(eventId, eventX, eventY, eventPrices))

listOfEvents.sort(key=lambda event: event.id)

numberOfBuyers = int(input())
listOfBuyers = list()
for i in range(numberOfBuyers):
    buyerLine = input().split()
    buyerX = int(buyerLine[0])
    buyerY = int(buyerLine[1])
    listOfBuyers.append(Buyer(i, buyerX, buyerY))

for buyer in listOfBuyers:
    minDistance = float('inf')
    for event in listOfEvents:
        if event.isTicketAvailable:
            minDistance = min(minDistance,
                              manhattan_distance(buyer.x, buyer.y, event.x, event.y))
        else:
            listOfEvents.remove(event)

    closestEvents = list()
    for event in listOfEvents:
        if manhattan_distance(buyer.x, buyer.y, event.x, event.y) == minDistance \
                and event.isTicketAvailable():
            closestEvents.append(event)

    minPrice = float('inf')
    for event in closestEvents:
        minPrice = min(minPrice, event.prices[0])

    for event in closestEvents:
        if event.prices[0] == minPrice:
            event.buyTicket()
            resultList.append('' + str(event.id) + ' ' + str(minPrice))
            if event.prices:
                listOfEvents.remove(event)
                closestEvents.remove(event)
            break

for result in resultList:
    print(result)

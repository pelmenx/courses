# show how many roads have we add(minimum) to make flight from starting_airport to others ones.
# Number of connected flight doesn't matter

def find_loop(airports, routes, increment=1):

    airports_used = {}
    for airport in airports:
        for item in airports:
            airports_used[item] = 0
        starting_air = airport
        routes_copy = routes.copy()
        for i in range(0, len(routes_copy)):
            if routes_copy[i][0] == starting_air:
                cycle(routes_copy, airport, airports_used, starting_air, increment)
        if airport == airports[len(airports) - 1]:
            raise Exception


def cycle(routes_copy, airport, airports_used, starting_air, increment, roads_group=[], airports_group=[]):
    for i in range(0, len(routes_copy)):
        if routes_copy[i][0] == starting_air:
            airports_used[airport] = 1
            starting_air = routes_copy[i][1]
            roads_group.append(routes_copy[i])
            for j in range(0, 2):
                if routes_copy[i][j] not in airports_group:
                    airports_group.append(routes_copy[i][j])
            routes_copy[i] = ["AAA", "AAA"]
            if airports_used[starting_air] == 1:
                modified_roads(roads_group, airports_group, increment)
            cycle(routes_copy, airport, airports_used, starting_air, increment)
    airports_group.clear()
    roads_group.clear()
    return 0


def modified_roads(roads_group, airports_group, increment):
    for road in roads_group:
        for route in routes:
            if road == route:
                routes.remove(road)

    for air in airports_group:
        for i in range(0, len(routes)):
            for j in range(0, 2):
                if routes[i][j] == air:
                    routes[i][j] = ("group" + str(increment))
    for air in airports_group:
        for i in range(0, len(airports)):
            if airports[i] == air:
                if "group" + str(increment) not in airports:
                    airports[i] = ("group" + str(increment))
                else:
                    airports[i] = "delete"
    for i in range(0, airports.count("delete")):
        airports.remove("delete")
    increment += 1
    find_loop(airports, routes, increment)


def find_new_routes(new_routes=[]):
    counter = 0
    for airport in airports:
        i = 0
        if airport != starting_airport:
            for route in routes:
                if airport == route[1]:
                    i += 1
            if i == 0:
                counter += 1
                new_routes.append([starting_airport, airport])
    return counter, new_routes


# list of airports
airports = ["BGI", "CDG", "DEL", "DOH", "DSM", "EWR",
            "EYW", "HND", "ICN", "JFK", "LGA", "LHR",
            "ORD", "SAN", "SFO", "SIN", "TLV", "BUD"]
# One way flihts
routes = [["DSM", "ORD"],
          ["ORD", "BGI"],
          ["BGI", 'LGA'],
          ["SIN", "CDG"],
          ["CDG", "SIN"],
          ["CDG", "BUD"],
          ["DEL", "DOH"],
          ["DEL", "CDG"],
          ["TLV", "DEL"],
          ["EWR", "HND"],
          ["HND", "ICN"],
          ["HND", "JFK"],
          ["ICN", "JFK"],
          ["JFK", "LGA"],
          ["EYW", "LHR"],
          ["LHR", "SFO"],
          ["SFO", "SAN"],
          ["SFO", "DSM"],
          ["SAN", "EYW"]
          ]
starting_airport = "LGA"


try:
    find_loop(airports, routes)
except Exception:
    print(find_new_routes())

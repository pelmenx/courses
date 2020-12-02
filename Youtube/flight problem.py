def find_loop(airpots, routes):

    airpots_count = {}
    for airport in airpots:
        for route in routes:
            if airport == route[0]:
                if airport not in airpots_count:
                    airpots_count[airport] = 1
                else:
                    airpots_count[airport] += 1
        if airport not in airpots_count:
            airpots_count[airport] = 1

    airpots_used = {}
    for airport in airpots:
        for item in airpots:
            airpots_used[item] = 0
        print("next")
        print("current airport -", airport)
        starting_air = airport
        routes_copy = routes.copy()
        for i in range(0, len(routes_copy)):
            if routes_copy[i][0] == starting_air:
                cycle(routes_copy, airport, airpots_used, starting_air)

    return 0


def cycle(routes_copy, airport, airpots_used, starting_air, roads_group=[]):
    print("CYCLE")
    for i in range(0, len(routes_copy)):
        if routes_copy[i][0] == starting_air:
            airpots_used[airport] = 1
            starting_air = routes_copy[i][1]
            print("airport -", airport, "|", "ruote -", routes_copy[i], "|", "starting_air -", starting_air)
            print(routes_copy)
            print(airpots_used)
            roads_group.append(routes_copy[i])
            routes_copy[i] = ["AAA", "AAA"]
            print(routes_copy)
            if airpots_used[starting_air] == 1:
                print("-", roads_group)
                print("BREAK")
                return 0
            cycle(routes_copy, airport, airpots_used, starting_air)
    roads_group.clear()
    print("no more roads")
    return 0


def modified_roads():

    return 0


# list of airports
airpots = ["BGI", "CDG", "DEL", "DOH", "DSM", "EWR",
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

find_loop(airpots, routes)

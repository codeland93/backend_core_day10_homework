our_routes = {"LAX", "JFK", "CDG", "DXB"}
competitor_routes = {"JFK", "CDG", "LHR", "BKK"}

# Destinations that both airlines fly to

intersect = our_routes.intersection(competitor_routes)
print(intersect)

# Destinations unique to your airline

print(our_routes.difference(competitor_routes))

# Whether there are any destinations that neither airline shares      

print(our_routes.symmetric_difference(competitor_routes))
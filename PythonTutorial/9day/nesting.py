
places_visited = {
  "France": "Paris",
  "Russia": "Moscow",
  "Germany": "Munich",
}

travel_log = {
  "France": ["Paris", "Lille", "Dijon"],
  "Russia": ["Moscow", "St. Petersburg", "Rostov"],
  "Germany": "Munich"
}

# exercise asks to change the Russia key to be a dictionary, use the same cities but add a value to each key

# print(travel_log)

travel_log["France"] = {"cities_visited": ["Paris", "Lille", "Dijon"]}

travel_log["Russia"] = {
  "cities_visited": ["Moscow", "St. Petersburg", "Rostov"]
}

# how things can be nested, with lists in dictionaries in lists

travel_log2 = [
  {
    "country": "France",
    "cities_visited": ["Paris", "Lille", "Dijon"],
    "times_visited": 12
  },
  {
    "country": "Russia",
    "cities_visited": ["Moscow", "St. Petersburg", "Rostov"],
    "times_visited": 1
  }
  ]

print(travel_log)

#travel_log = {
 #   "France": ["Dijon", "Lillie", "Paris"]
 #   "Germany": ["stuttgart", "Berlin"]
#}

#print(travel_log["France"])

#nested_list = ["a", "b", ["c", "d"]]

#print(nested_list[2][0])


travel_log = {
    "France": {
        "num times vistied": 8,
        "cities visited": ["Dijon", "Lillie", "Paris"]
    },
    "Germany": ["stuttgart", "Berlin"]
}

print(travel_log["France"]["cities visited"][1])
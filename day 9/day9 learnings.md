# dictionaries & nesting
## dictionaries
dictionairies allow for definition making.
to create dictionary: {key: value} -> programming_dictionary = {"bug": "an error in a program, "another":"with its definition"}
for ease of interpretation:
programming dictionary = {
    "bug": "definition",
    "another": "with its definition"
}

to retrieve item you identify the one by the key:
programming_dictionary["bug"]

adding new entry:
programming_dictionary["loop"] = "definition of loop"

empty dict:
empty_dictionary = {}

wipe existing dict:
programming_dictionary = {}

edit an item:
programming_dictionary["bug"] = "new definition"

for thing in programming_dictionary:
    thing will be keys

## nesting
putting one inside the other
{
    key: [list],
    key2: {dict}
}

travel_log = {
    "France": ["paris", "lille"]
}

nested dict
travel_log = {
    "France": {"cities visited": "Paris", "cities to visit": ["lille", "dijon"]}
}

nesting a dictionary in a list
[{
    key:[list],
    key2:{dict}
}
{
    key: value,
    key2: value2
}]

travel_log = [
    {
        "country": "france", 
        "cities_visited": ["Paris", "Lille", "Dijon"], 
        "total_visits": 12
    },
    {
        "country": "germany", 
        "cities_visited": ["Berlin", "Stuttgart"], 
        "total_visits": 5
    }
]
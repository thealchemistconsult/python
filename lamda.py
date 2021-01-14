people = [
    {"name": "Kofi", "house": "KumaHouse"},
    {"name": "Kwasi", "house": "AccraHouse"},
    {"name": "Kwame", "house": "AkyemHouse"}
]

people.sort(key=lambda person: person["name"])


print(people)
from entities import Other, PrivatePerson, PublicPerson

try:
    from entities import Organization
except ImportError:
    from entities import organization as Organization


# Devskiller INFO: This file is simple db mock, please skip this file doing code review

def get_objects_list():
    return [
        PrivatePerson("John", "Doe", "Paris"),
        PublicPerson("Donald", "Trump", "New York"),
        Organization("Devskiller", "Warsaw"),
        Other("Kevin"),
    ]


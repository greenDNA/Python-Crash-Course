"""
1.py
def city_country(city, country):
    return "{}, {}".format(city.title(), country.title())
"""

def city_country(city, country, population=''):
    if population:
        return "{}, {} - population {}".format(city.title(), country.title(), population)
    else:
        return "{}, {}".format(city.title(), country.title())

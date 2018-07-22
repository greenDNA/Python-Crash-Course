def make_car(manufacturer, model, **other):
    vehicle= {}
    vehicle['manufacturer'] = manufacturer
    vehicle['model'] = model
    for key, value in other.items():
        vehicle[key] = value
    return vehicle
car = make_car('Toyota', 'Mustang', color='green', doors='coupe')
print(car)

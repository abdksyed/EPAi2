import itertools
import datetime
from collections import namedtuple, defaultdict


def ticket_gen():
    with open('nyc_parking_tickets_extract-1.csv') as f:
        def date_type(x): return datetime.datetime.strptime(
            x, "%m/%d/%Y").date()
        data_type = [int, str, str, str, date_type, int, str, str, str]
        Parking = namedtuple('Parking', [x.replace(
            " ", "") for x in next(f).strip().split(',')])
        for row in f:
            yield Parking(*(type(field) for type, field in zip(data_type, row.strip().split(','))))


def violations_per_carmake(parking_ticket_generator):
    vechicle_makes = defaultdict(int)

    for ticket in ticket_gen():
        if ticket.VehicleMake:
            vechicle_makes[ticket.VehicleMake] += 1

    yield from sorted(vechicle_makes.items(), key=lambda x: x[1], reverse=True)

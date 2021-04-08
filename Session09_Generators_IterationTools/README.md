# Session 9 - Generators and Iteration Tools

### [Class Notebooks - Generators and Iteration Tools](https://github.com/abdksyed/EPAi2/blob/main/Session09_Generators_IterationTools/notebooks/)

Click on **Open in Colab** for hands-on.

### [Assignment Notebook](https://colab.research.google.com/drive/1WbPacPBdMcyjVBPtRUYVJYqUChjzzmiD?usp=sharing)

### Topic Covered:

* #### Yielding and Generator Functions
* #### Making an iterable from a Generator
* #### Generator Expressions and Performance
* #### Yield From
* #### Aggregators
* #### Slicing
* #### Selecting and Filtering
* #### Infinite Iterators
* #### Chaining and Teeing
* #### Mapping and Reduction
* #### Zipping


## Objective A - Create Lazy Iterators to generate Ticket Data from csv.
Create a lazy iterator that will return a named tuple of the data in each row. The data types should be appropriate - i.e. if the column is a date, you should be storing dates in the named tuple, if the field is an integer, then it should be stored as an integer, etc.

```python
def ticket_gen():
    with open('nyc_parking_tickets_extract-1.csv') as f:
        def date_type(x): return datetime.datetime.strptime(
            x, "%m/%d/%Y").date()
        data_type = [int, str, str, str, date_type, int, str, str, str]
        Parking = namedtuple('Parking', [x.replace(
            " ", "") for x in next(f).strip().split(',')])
        for row in f:
            yield Parking(*(type(field) for type, field in zip(data_type, row.strip().split(','))))
```

## Objective B - Calculate the number of violations by car make.

```python
def violations_per_carmake(parking_ticket_generator):
    vechicle_makes = defaultdict(int)

    for ticket in ticket_gen():
        if ticket.VehicleMake:
            vechicle_makes[ticket.VehicleMake] += 1

    yield from sorted(vechicle_makes.items(), key=lambda x: x[1], reverse=True)
```
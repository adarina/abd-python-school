import datetime
import random


def random_date():
    """
    This function will return a random datetime between two datetime
    objects.
    """
    start = datetime.date(year=1950, month=1, day=1)
    end = datetime.date(year=1990, month=12, day=31)
    delta = end - start
    int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
    random_second = random.randrange(int_delta)
    return start + datetime.timedelta(seconds=random_second)


# def random_weight():
#     return random.randint(50, 120) + random.random()


# def random_pulse():
#     return random.randint(60, 110)


# def random_pressure():
#     return "bottom:" + str(random.randint(40, 80)) + ",top:" + str(random.randint(70, 160))


# def random_ekg():
#     return ",".join([str(random.random()) for _ in range(100)])


# def random_value_for_type(mtype):
#     mapping = {
#         'weight': random_weight,
#         'avg_pulse': random_pulse,
#         'avg_pressure': random_pressure,
#         'EKG': random_ekg
#     }
#     return mapping[mtype]()
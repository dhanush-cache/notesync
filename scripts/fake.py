import random
import re
import string
from datetime import datetime

from faker import Faker

fake = Faker()


def name():
    return " ".join(
        fake.words(
            nb=random.randint(2, 4),
            part_of_speech="noun",
            unique=True,
        )
    )


def sentence():
    words_count = random.randint(10, 20)
    return fake.sentence(words_count)


def to_slug(name):
    return name.lower().replace(" ", "-")


def code():
    letters = "".join(random.choices(string.ascii_letters, k=2))
    digits = "".join(random.choices(string.digits, k=5))
    return f"{letters}-{digits}"


def first_name():
    return fake.first_name()


def last_name():
    return fake.last_name()


def email(fname, lname):
    fname = fname.lower()
    lname = lname.lower()
    username = random.choice(
        [
            fname + str(random.randint(1, 1000)),
            lname + str(random.randint(1, 1000)),
            fname + lname + str(random.randint(1, 1000)),
            fname + lname,
        ]
    )
    return re.sub(r"^.*@", username + "@", fake.email(safe=False))


def url():
    return fake.url()


def date():
    year, month, day = map(int, fake.date().split("-"))
    return datetime(year, month, day)


def score():
    return random.randint(1, 5)

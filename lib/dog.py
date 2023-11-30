#!/usr/bin/env python3

APPROVED_BREEDS = [
    "Mastiff",
    "Chihuahua",
    "Corgi",
    "Shar Pei",
    "Beagle",
    "French Bulldog",
    "Pug",
    "Pointer",
]


class Dog:
    def __init__(self, name="", breed="") -> None:
        self.name = name
        self.breed = breed

    def get_name(self):
        return self.name

    def set_name(self, name):
        try:
            # Validate and set the name
            if isinstance(name, str) and 1 <= len(name) <= 25:
                self.name = name
            else:
                raise ValueError("Name must be a string between 1 and 25 characters.")
        except ValueError as e:
            print(str(e))

    def get_breed(self):
        return self.breed

    def set_breed(self, breed):
        try:
            # Validate and set the breed
            if breed not in APPROVED_BREEDS:
                raise ValueError("Breed must be in the list of approved breeds.")
            else:
                self.breed = breed
        except ValueError as e:
            print(str(e))


APPROVED_JOBS = ["Sales", "ITC"]


class Person:
    def __init__(self, name="", job=""):  # Allow empty name and job by default
        self.name = name
        self.job = job

    def get_name(self):
        return self.name

    def set_name(self, name):
        try:
            # Validate and set the name
            if isinstance(name, str) and 1 <= len(name) <= 25:
                self.name = name
            else:
                raise ValueError("Name must be a string between 1 and 25 characters.")
        except ValueError as e:
            print(str(e))

    def get_job(self):
        return self.job

    def set_job(self, job):
        try:
            # Validate and set the job
            if job not in APPROVED_JOBS:
                raise ValueError("Job must be in the list of approved jobs.")
            else:
                self.job = job
        except ValueError as e:
            print(str(e))


guido = Person(name="Guido")  # Correct
guido = Person("guido van rossum")  # Correct

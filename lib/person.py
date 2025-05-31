#!/usr/bin/env python3
APPROVED_JOBS = [
    "Admin", "Customer Service", "Human Resources", "ITC", "Production", "Legal",
    "Finance", "Sales", "General Management", "Research & Development", "Marketing", "Purchasing"
]

class Person:
    def __init__(self, name="Unknown", job="Unknown"):
        self._name = None  # Initialize attributes
        self._job = None
        self.name = name  # Use property setter
        if self._name is not None:  # Only validate job if name is valid
            self.job = job  # Use property setter

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if isinstance(value, str) and 1 <= len(value) <= 25:
            self._name = value.title()  # Convert to title case before saving
        else:
            print("Name must be string between 1 and 25 characters.")

    @property
    def job(self):
        return self._job

    @job.setter
    def job(self, value):
        if value in APPROVED_JOBS:  # Reference the global variable
            self._job = value
        else:
            print("Job must be in list of approved jobs.")

    pass
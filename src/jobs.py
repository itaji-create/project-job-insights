from functools import lru_cache
import csv


@lru_cache
def read(path):
    with open(path) as file:
        jobs_reader = csv.DictReader(file)
        jobs_data = [row for row in jobs_reader]
        return jobs_data

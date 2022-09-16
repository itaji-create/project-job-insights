from functools import lru_cache
import csv


@lru_cache
def read(path):
    with open(path) as file:
        jobs = csv.DictReader(file)
        jobs_data = [row for row in jobs]
        return jobs_data

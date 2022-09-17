from src.jobs import read


def get_unique_job_types(path):
    jobs_data = read(path)

    types_list = []

    for row in jobs_data:
        type = row["job_type"]
        if type not in types_list:
            types_list.append(type)

    return types_list


def filter_by_job_type(jobs, job_type):
    list_jobs = [job for job in jobs if job["job_type"] == job_type]

    return list_jobs


def get_unique_industries(path):
    jobs_data = read(path)

    industry_list = []

    for row in jobs_data:
        industry = row["industry"]
        if industry not in industry_list:
            if len(industry) > 1:
                industry_list.append(industry)
    return industry_list


def filter_by_industry(jobs, industry):
    list_industries = [job for job in jobs if job["industry"] == industry]

    return list_industries


def get_max_salary(path):
    jobs_data = read(path)
    max_salaries = []
    for row in jobs_data:
        max_salary = row["max_salary"]
        if max_salary not in max_salaries and len(max_salary) > 0:
            if str(max_salary).isdigit():
                max_salaries.append(int(max_salary))
    max_salaries.sort()
    return max_salaries[-1]


def get_min_salary(path):
    jobs_data = read(path)
    min_salaries = []
    for row in jobs_data:
        min_salary = row["min_salary"]
        if min_salary not in min_salaries and len(min_salary) > 0:
            if str(min_salary).isdigit():
                min_salaries.append(int(min_salary))
    min_salaries.sort()
    return min_salaries[0]


def matches_salary_range(job, salary):

    if "min_salary" not in job or "max_salary" not in job:
        raise ValueError
    min_salary = job["min_salary"]
    max_salary = job["max_salary"]
    if type(min_salary) is not int or type(max_salary) is not int:
        raise ValueError
    if min_salary > max_salary:
        raise ValueError

    return min_salary <= salary <= max_salary


def filter_by_salary_range(jobs, salary):
    filtered_jobs = []
    for job in jobs:
        if str(salary).isdigit() and job["min_salary"] < job["max_salary"]:
            if matches_salary_range(job, salary):
                filtered_jobs.append(job)

    return filtered_jobs

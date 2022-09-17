from src.jobs import read


def get_unique_job_types(path):
    """Checks all different job types and returns a list of them

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    list
        List of unique job types
    """
    jobs_data = read(path)

    types_list = []

    for row in jobs_data:
        type = row["job_type"]
        if type not in types_list:
            types_list.append(type)

    return types_list


def filter_by_job_type(jobs, job_type):
    """Filters a list of jobs by job_type

    Parameters
    ----------
    jobs : list
        List of jobs to be filtered
    job_type : str
        Job type for the list filter

    Returns
    -------
    list
        List of jobs with provided job_type
    """
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
    """Filters a list of jobs by industry

    Parameters
    ----------
    jobs : list
        List of jobs to be filtered
    industry : str
        Industry for the list filter

    Returns
    -------
    list
        List of jobs with provided industry
    """
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
    """Checks if a given salary is in the salary range of a given job

    Parameters
    ----------
    job : dict
        The job with `min_salary` and `max_salary` keys
    salary : int
        The salary to check if matches with salary range of the job

    Returns
    -------
    bool
        True if the salary is in the salary range of the job, False otherwise

    Raises
    ------
    ValueError
        If `job["min_salary"]` or `job["max_salary"]` doesn't exists
        If `job["min_salary"]` or `job["max_salary"]` aren't valid integers
        If `job["min_salary"]` is greather than `job["max_salary"]`
        If `salary` isn't a valid integer
    """
    pass


def filter_by_salary_range(jobs, salary):
    """Filters a list of jobs by salary range

    Parameters
    ----------
    jobs : list
        The jobs to be filtered
    salary : int
        The salary to be used as filter

    Returns
    -------
    list
        Jobs whose salary range contains `salary`
    """
    return []

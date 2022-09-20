from src.counter import count_ocurrences


def test_count_ocurrences():
    result = count_ocurrences("src/jobs.csv", "job")

    assert type(result) == int

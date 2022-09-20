from src.counter import count_ocurrences


def test_counter():
    result = count_ocurrences("src/jobs.csv", "job")

    assert type(result) == int
    assert result == 3454

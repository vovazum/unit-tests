import pytest
from string_slices import string_slices

@pytest.mark.parametrize(
    "input_string, expected_output",
    [
        ("%%Приказ об увольнении&#", "Приказ об увольнении"),
        ("%%Лучший студент на курсе!&#", "Лучший студент на курсе!"),
        ("%%Hello World!&#", "Hello World!")
    ]
)
def test_string_slices(input_string, expected_output):
    assert string_slices(input_string) == expected_output
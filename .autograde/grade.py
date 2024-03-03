import pytest

fn_name = "treecoords"


class ImportDetailsError(Exception):
    pass


try:
    import uppgift

    fn = getattr(uppgift, fn_name)

    if not callable(fn):
        raise ImportDetailsError(f"Function {fn_name} is not callable")

    # Check if the function takes exactly two arguments
    if not fn.__code__.co_argcount == 2:
        raise ImportDetailsError(f"Function {fn_name} must take exactly two arguments")

    def test_exempel_1():
        assert fn({"a": 1, "b": 2}) == ((("a",), 1), (("b",), 2))

    def test_exempel_2():
        assert fn({"x": {"y": 3}, "z": 4}) == ((("x", "y"), 3), (("z",), 4))

    def test_exempel_3():
        assert fn({"root": {"left": 5, "right": {"left": 6, "right": 7}}}) == (
            (("root", "left"), 5),
            (("root", "right", "left"), 6),
            (("root", "right", "right"), 7),
        )

    def test_exempel_4():
        assert fn({"1": {"2": {"3": {}}, "4": {"5": 8, "6": 9}}}) == (
            (("1", "4", "5"), 8),
            (("1", "4", "6"), 9),
        )

    def test_exempel_5():
        assert fn({"a": {"b": {"c": 10, "d": 11}, "e": {"f": 12}}, "g": 13}) == (
            (("a", "b", "c"), 10),
            (("a", "b", "d"), 11),
            (("a", "e", "f"), 12),
            (("g",), 13),
        )

except ImportDetailsError as e:
    pytest.fail(str(e))

except ImportError:
    pytest.fail(f"Function {fn_name} has not been implemented")

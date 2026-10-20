from scope import use_local_object, use_global_object, object


def test_global():
    assert object == "This is the global object."
    assert "object" in globals()
    assert id(use_global_object()) == id(object)


def test_local():
    assert use_local_object() == "This is the local object."

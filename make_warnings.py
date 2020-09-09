import warnings
import pytest

def fxn():
    warnings.warn("deprecated", DeprecationWarning)

def not_warn():
    pass

def warn_message():
    # warnings.warn("I'm a warning message", UserWarning)
    warnings.warn("user", UserWarning)
    warnings.warn("runtime", RuntimeWarning)

def test_hello(recwarn):
    warnings.warn("hello", UserWarning)
    assert len(recwarn) == 1
    w = recwarn.pop(UserWarning)
    assert issubclass(w.category, UserWarning)
    assert str(w.message) == "hello"
    assert w.filename
    assert w.lineno
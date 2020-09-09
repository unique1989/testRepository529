import pytest
import make_warnings

class TestWarns():
    def test_depre(self):
        with pytest.warns(DeprecationWarning):
            make_warnings.fxn()

    def test_not_warn(self):
        with pytest.warns(DeprecationWarning):
            make_warnings.not_warn()

    def test_warn_match(self):
        with pytest.warns(UserWarning, match=r'^I.*e'):
            make_warnings.warn_message()

        with pytest.warns(UserWarning, match=r'.*u.*') as record:
            make_warnings.warn_message()

        assert len(record) == 2
        assert str(record[0].message) == "user"
        assert str(record[1].message) == "runtime"
   
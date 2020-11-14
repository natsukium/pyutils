import pkg_resources
import pytest
import pyutils


def test_version() -> None:
    expect = pkg_resources.get_distribution('pyutils').version
    actual = pyutils.__version__
    assert expect == actual


if __name__ == '__main__':
    pytest.main([__file__, '-v'])

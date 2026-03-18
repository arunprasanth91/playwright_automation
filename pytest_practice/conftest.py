# global file for fixture - should always have filename as conftest
import pytest


@pytest.fixture
def prerequisite1(scope = "function"):
    # when scope = function it will run before/after every function
    # when scope = module it will run only once for the complete file.
    # scope = class also works like module but use when test file defined as a class.
    # scope = session it will run only once per execution/run.

    print('runs before everything else.')
    yield # will pause fixture here and resume after tests are completed. acts as a tear down method as well.
    print('runs after everything else.')
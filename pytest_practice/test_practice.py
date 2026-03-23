import pytest

# file name should start with test.

@pytest.fixture
def prerequisite(scope = "function"):
    # when scope = function it will run before/after every function
    # when scope = module it will run only once for the complete file.
    # scope = class also works like module but use when test file defined as a class.
    # scope = session

    print('runs before everything else.')
    # we can also return from fixture can be directly accessed by the fixture ref passed as arguemnt to test methods
    return "Done with Prerequisite setup!"

# start with test keyword

def test_first(prerequisite): # fixture name should be passed as argument to run before/after.
    print('hello world')
    assert prerequisite == 'Done with Prerequisite setup!'

def test_second(prerequisite1): print('hello world22222')
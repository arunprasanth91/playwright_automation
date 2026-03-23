1. pytest - to all the test files 
2. pytest -v -s -> -v stands for verbose and -s stands for printing logs to console.
3. pytest test_filename::test_method_name - To run a particular test method from a test module.
4. @pytest.fixture - can be used to execute before/after a test method. 
    fixture can return an object, that can be used in the test method by passing the fixture method name as argument to test method and the argument will 
    hold the value of what is returned from the fixture.
5. @pytest.fixture(scope=function/module/class/session)
    scope = function - runs before/after every test method
    scope = module - runs once before/after for a test module
    scope = class - runs once before/after for a test class
    scope = session - runs once before/after for a test execution/run.

6. @pytest.mark.skip - to skip a test 
7. @pytest.mark.smoke/regression - tagging a test method 
   To run tagged test method - pytest -m smoke/regression
8. 




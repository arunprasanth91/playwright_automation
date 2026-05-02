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
8. @pytest.mark.parameterize(list/dict/tuple)  - to parameterize with diff datasets. 



Parallelization - Parallelization in Playwright Python is managed via worker processes. 
By default, the Playwright Pytest plugin does not run tests in parallel. You must explicitly enable it using the pytest-xdist plugin. 

# Run tests using 3 parallel workers
pytest -n 3

rerun failed test with delay 
pytest --reruns 5 --reruns-delay 1


Sharding - Sharding is the process of splitting a large test suite into smaller subsets (shards) to run them on different machines simultaneously,
typically within a CI/CD pipeline. 

# Run only the first part of a suite split into 3 shards
pytest --shard=1/3
# Run the second part
pytest --shard=2/3
# Run the third part
pytest --shard=3/3

Key Differences
Feature 	    Parallelization (Workers)	            Sharding
Scope	        Single Machine	                        Multiple Machines/Nodes
Scaling	        Vertical (Uses CPU cores)	            Horizontal (Uses multiple runners)
Setup	        pytest-xdist plugin	                    Command-line --shard flag
Primary Use	    Local development & CI efficiency	    Large enterprise-scale test suites

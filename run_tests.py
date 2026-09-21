import unittest
import sys

def main():
    print("=======================================")
    print(" Running Contact Management Test Suite ")
    print("=======================================\n")
    
    # Discover and load all tests from the 'tests' directory
    loader = unittest.TestLoader()
    suite = loader.discover('tests')

    # Run the tests and capture the results silently
    runner = unittest.TextTestRunner(verbosity=0)
    result = runner.run(suite)

    print("\n---------------------------------------")
    print("              TEST SUMMARY             ")
    print("---------------------------------------")
    
    total_tests = result.testsRun
    failed_tests = len(result.failures)
    errored_tests = len(result.errors)
    passed_tests = total_tests - (failed_tests + errored_tests)

    print(f"Total Tests Run : {total_tests}")
    print(f"Passed          : {passed_tests}")
    print(f"Failed          : {failed_tests}")
    print(f"Errors          : {errored_tests}")
    print("---------------------------------------")

    if result.wasSuccessful():
        print("[SUCCESS] ALL TESTS PASSED SUCCESSFULLY!")
        sys.exit(0)
    else:
        print("[FAILED] SOME TESTS FAILED.")
        
        if result.failures:
            print("\n--- Failures ---")
            for failure in result.failures:
                print(f"Test: {failure[0]}")
                print(failure[1])
                
        if result.errors:
            print("\n--- Errors ---")
            for error in result.errors:
                print(f"Test: {error[0]}")
                print(error[1])
        sys.exit(1)

if __name__ == '__main__':
    main()

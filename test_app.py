from app import add

def test_add_function():
    print("Running test...")
    assert add(2, 3) == 6
    print("Test passed!")

# This makes the script run the test function
if __name__ == "__main__":
    test_add_function()

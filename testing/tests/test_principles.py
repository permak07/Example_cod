import sys
sys.path.append("../src")
#TODO make it with pip install -e
from src.math_demo import (add, 
                           add_with_bug)
def test_addition():
    assert add(2,2)==4
    print("Test basic addition")

def test_addition_with_bug():
    assert add_with_bug(2,2)==4
    print("Test bug addition_with_bug")
    assert add_with_bug(6,7)==13 #fail

if __name__=="__main__":
    test_addition()
    test_addition_with_bug()
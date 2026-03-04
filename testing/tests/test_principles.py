import sys
sys.path.append("../src")
#TODO make it with pip install -c
from math_demo import add
def test_addition():
    assert add(2,2)==4
    print("Test basic addition")

if __name__=="__main__":
    test_addition()
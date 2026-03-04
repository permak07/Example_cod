# import sys
# sys.path.append("../src")
# #TODO make it with pip install -e
from src.math_demo import (add, 
                           add_with_bug,
                           calculate_tax_with_bug,
                           calculate_tax
                           )
def test_addition():
    assert add(2,2)==4
    print("Test basic addition")

def test_addition_with_bug():
    assert add_with_bug(2,2)==4
    print("Test bug addition_with_bug")
    #assert add_with_bug(6,7)==13 #fail

def test_addition_duplicated():
    assert add(2,3)==3+2
    print("test_additoin_duplicated")

# bad test
def test_addition_overcomplicatid():
    for i in range(0,2**32):
        for j in range(0,2**32):
            assert add(i,j)==sum(i,j)
            assert add(-i,j)==sum(-i,j)
            assert add(i,-j)==sum(i,-j)
            assert add(-i,-j)==sum(-i,-j)

def test_addition_reasonable():
    assert add(2,2)==4
    assert add(0,0)==0
    assert add(6,7)==13
    assert add(-6,-7)==-13
    assert add(6,-7)==-1
    assert add(7,0)==7
    assert add(-7,0)==-7
    print("Test_addition_reasonable")

def test_additon_communication():
    assert add(7,-6)==1
    assert add(-6,7)==1
    print("test_addition_communication")

def test_calculate_pesticised():
    assert calculate_tax_with_bug(1000)==150
    assert calculate_tax_with_bug(100)==15
    assert calculate_tax_with_bug(10)==1.5
    assert calculate_tax_with_bug(1)==0.15
    assert calculate_tax_with_bug(245)==36.75
    assert calculate_tax_with_bug(-200)==-30
    assert calculate_tax_with_bug(0)==0
    print("test_calculate_pesticised")
    # Неточность
    #assert calculate_tax_with_bug(24.5)==3.67 #3.675

def test_calculate():
    assert calculate_tax_with_bug(1000)==150
    assert calculate_tax_with_bug(100)==15
    assert calculate_tax_with_bug(10)==1.5
    assert calculate_tax_with_bug(1)==0.15
    assert calculate_tax_with_bug(245)==36.75
    assert calculate_tax_with_bug(-200)==-30
    assert calculate_tax_with_bug(0)==0
    assert calculate_tax_with_bug(24.5)==3.67 #3.675
    print("test_calculate")


if __name__=="__main__":
    test_addition()
    test_addition_with_bug()
    test_addition_duplicated()
    #test_addition_overcomplicatid()
    test_addition_reasonable()
    test_additon_communication()
    test_calculate_pesticised()
    test_calculate()
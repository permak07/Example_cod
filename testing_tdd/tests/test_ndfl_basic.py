from ndfl import calculate_ndfl_lax

#| **До 2,4 млн руб.** | 13% | 13% от дохода |
#| **2,4 – 5 млн руб.** | 15% | 312 000 + 15% с суммы превышения |
#| **5 – 20 млн руб.** | 18% | 702 000 + 18% с суммы превышения |
#| **20 – 50 млн руб.** | 20% | 3 402 000 + 20% с суммы превышения |
#| **Свыше 50 млн руб.** | 22% | 9 402 000 + 22% с суммы превышения |
def test_ndfl():
    assert test_ndfl()==None

def test_ndfl():
    assert calculate_ndfl_lax()==None
    
def test_ndfl_tier1():
    assert calculate_ndfl_lax(500_000)==65_000

def test_ndfl_tier2():
    assert calculate_ndfl_lax(4_000_000)==512_000

def test_ndfl_tier3():
    assert calculate_ndfl_lax(10_000_000)==1_602_000

# def test_ndfl_tier4():
#     assert calculate_ndfl_lax(500_000)==65_000

#TODO make last two tiers
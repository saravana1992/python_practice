
from fizz import fizzBuzz


def test_for_fizz():
    assert fizzBuzz(3) == [1,2, "Fooz"], "Returns multiple of 3"

def test_for_buzzzz():
    assert fizzBuzz(5) == [1,2, "Fooz", 4, "Buzz"], "Returns multiple of 5"
    
def test_for_FizzBuzz():
    assert fizzBuzz(15) == [1,2, "Fooz", 4, "Buzz","Fooz" ,7,8, "Fooz" , "Buzz" ,11, "Fooz" ,13,14, "FoozBuzz"], "Returns multiple of 15"

    

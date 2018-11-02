from fizzbuzz import FizzBuzz

def test_number():
    fb = FizzBuzz.play(1)
    assert fb == 1

def test_fizz():
    fb = FizzBuzz.play(3)
    assert fb == 'Fizz'

def test_buzz():
    fb = FizzBuzz.play(5)
    assert fb == 'Buzz'

def test_fizzbuzz():
    fb = FizzBuzz.play(15)
    assert fb == 'FizzBuzz'

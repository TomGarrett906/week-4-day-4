from unittest import TestCase, main
from count_calls import fib

class CountCalls(TestCase):

  def test_calls_10(self):    
    self.assertNotEqual(fib(10), 123456)
    print(f"fib(10) {fib.count}")

  def test_calls_200(self):    
    self.assertEqual(fib(200), 280571172992510140037611932413038677189525)
    

if __name__ == '__main__':
  main()
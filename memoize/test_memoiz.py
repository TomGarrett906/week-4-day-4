from unittest import TestCase, main
from memoize import fib

class TestMemoiz(TestCase):

  def test_fib_10(self):    
    self.assertNotEqual(fib(10), 123456)

  def test_fib_200(self):    
    self.assertEqual(fib(200), 280571172992510140037611932413038677189525)
    

if __name__ == '__main__':
  main()
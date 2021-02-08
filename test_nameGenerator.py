import unittest
import nameGenerator

class TestAve(unittest.TestCase):
  def test1(self):
    self.assertEqual(nameGenerator.nameGen("Jane", "Doe"),"Jane Doe")
  def test2(self):
    self.assertEqual(nameGenerator.nameGen("10", "20"),"10 20")
  def test3(self):
    self.assertEqual(nameGenerator.nameGen("", ""),"")
    

if __name__ == '__main__':
  unittest.main()
import unittest
from unittest.mock import patch
from employee import Employee

class TestEmployee(unittest.TestCase):
  
  def setUp(self):
    self.emp_1 = Employee("Jason", "Whisnant", 55000)
    self.emp_2 = Employee("Jason", "Coder", 85000)
  
  def tearDown(self):
    pass
  
  def test_email(self):
    self.assertEqual(self.emp_1.email, "Jason.Whisnant@email.com")
    self.assertEqual(self.emp_2.email, "Jason.Coder@email.com")
    
    self.emp_1.first = "Jacob"
    self.emp_2.last = "Whisnant"
    
    self.assertEqual(self.emp_1.email, "Jacob.Whisnant@email.com")
    self.assertEqual(self.emp_2.email, "Jason.Whisnant@email.com")
    
  def test_fullname(self):
    self.assertEqual(self.emp_1.fullname, "Jason Whisnant")
    self.assertEqual(self.emp_2.fullname, "Jason Coder")
    
    self.emp_1.first = "Jacob"
    self.emp_2.last = "Whisnant"
    
    self.assertEqual(self.emp_1.fullname, "Jacob Whisnant")
    self.assertEqual(self.emp_2.fullname, "Jason Whisnant")
  
  def test_apply_raise(self):
    self.emp_1.apply_raise()
    self.emp_2.apply_raise()
    
    self.assertEqual(self.emp_1.pay, 57750)
    self.assertEqual(self.emp_2.pay, 89250)
  
  
if __name__ == '__main__':
  unittest.main()
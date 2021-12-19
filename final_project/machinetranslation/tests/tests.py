import unittest
from translator import englishToFrench, frenchToEnglish

class TestTranslator(unittest.TestCase):
  def test_englishToFrench(self):
    self.assertEqual(englishToFrench('Hello'),'Bonjour')
    self.assertEqual(englishToFrench(), '')
    self.assertNotEqual(englishToFrench('School'), 'Bonjour')


  def test_frenchToEnglish(self):
    self.assertEqual(frenchToEnglish('Bonjour'),'Hello')
    self.assertEqual(frenchToEnglish(), '')
    self.assertNotEqual(frenchToEnglish('Loger'), 'Fan')

if __name__ =='__main__':
  unittest.main()
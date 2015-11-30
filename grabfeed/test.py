import unittest
from grabber import return_rss

class TestGrabber(unittest.TestCase):

  def test_wordpress(self):
      link = "http://techcrunch.com"
      self.assertEqual(return_rss(link), 'http://techcrunch.com/feed/')

if __name__ == '__main__':
    unittest.main()
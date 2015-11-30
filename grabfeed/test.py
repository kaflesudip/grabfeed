import unittest
from grabber import return_rss


class TestGrabber(unittest.TestCase):

    def test_wordpress(self):
        link = "http://techcrunch.com"
        self.assertEqual(return_rss(link), 'http://techcrunch.com/feed/')

    def test_blogger(self):
        link = "http://google.blogspot.com/"
        self.assertEqual(
            return_rss(link),
            'http://google.blogspot.com/feeds/posts/default?alt=rss'
        )

    def test_svtle(self):
        link = 'http://blog.svbtle.com/'
        self.assertEqual(
            return_rss(link),
            'http://blog.svbtle.com/feed'
        )

    def test_ghost(self):
        link = 'https://blog.ghost.org/'
        self.assertEqual(
            return_rss(link),
            'https://blog.ghost.org/rss/'
        )

if __name__ == '__main__':
    unittest.main()

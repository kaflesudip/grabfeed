import unittest
from grabber import return_rss, return_atom


class TestRSS(unittest.TestCase):

    def test_error_on_invalid_url(self):
        link = "http://example"
        self.assertRaises(Exception, return_rss, link)

    def test_error_on_url_without_feed(self):
        link = "http://example.com"
        self.assertRaises(Exception, return_rss, link)

    def test_wordpress(self):
        link = "https://techcrunch.com"
        self.assertEqual(return_rss(link), 'https://techcrunch.com/feed/')

    def test_blogger(self):
        link = "https://google.blogspot.com/"
        self.assertEqual(
            return_rss(link),
            'https://google.blogspot.com/feeds/posts/default?alt=rss'
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

    def test_medium(self):
        link = 'https://medium.com/stories-from-nlocate'
        self.assertEqual(
            return_rss(link),
            'https://medium.com/feed/stories-from-nlocate'
        )

    def test_tumblr(self):
        link = "https://staff.tumblr.com/"
        self.assertEqual(
            return_rss(link),
            'https://staff.tumblr.com/rss'
        )


class TestAtom(unittest.TestCase):

    def test_error_on_url_without_feed(self):
        link = "http://example.com"
        self.assertRaises(Exception, return_atom, link)

    def test_blogger(self):
        link = "https://google.blogspot.com/"
        self.assertEqual(
            return_atom(link),
            'https://google.blogspot.com/feeds/posts/default'
        )


if __name__ == '__main__':
    unittest.main()

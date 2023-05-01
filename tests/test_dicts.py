import unittest
from utils import dicts


class TestArrs(unittest.TestCase):

    def test_get_val(self):
        self.assertEqual(dicts.get_val({'vcs': 'mercurial'}, 'vcs', "test"), 'mercurial')
        self.assertEqual(dicts.get_val({}, 'vcs', "test"), 'test')
        self.assertEqual(dicts.get_val({}, 'vcs'), 'git')

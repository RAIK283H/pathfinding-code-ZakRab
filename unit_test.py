import math
import unittest
import global_game_data
from pathing import get_bfs_path, get_dfs_path
import graph_data
import pyglet
class TestPathFinding(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('test'.upper(), 'TEST')

    def test_isupper(self):
        self.assertTrue('TEST'.isupper())
        self.assertFalse('Test'.isupper())

    def test_floating_point_estimation(self):
        first_value = 0
        for x in range(1000):
            first_value += 1/100
        second_value = 10
        almost_pi = 3.1
        pi = math.pi
        self.assertNotEqual(first_value,second_value)
        self.assertAlmostEqual(first=first_value,second=second_value,delta=1e-9)
        self.assertNotEqual(almost_pi, pi)
        self.assertAlmostEqual(first=almost_pi, second=pi, delta=1e-1)

class TestBFS(unittest.TestCase):
    def test_bfs1(self):
        path = get_bfs_path()
        self.assertEqual(path, [0,1,2])
        pass

    def test_dfs1(self):
        path = get_bfs_path()
        self.assertEqual(path, [0,1,2])
        pass
    
    def test_bfs2(self):
        global_game_data.current_graph_index = 1
        path = get_bfs_path()
        self.assertEqual(path, [0,1,2,3])
        pass

    def test_dfs2(self):
        global_game_data.current_graph_index = 1
        path = get_dfs_path()
        self.assertEqual(path, [0,1,2,3])
        pass
if __name__ == '__main__':
    pyglet.app.run()
    unittest.main()

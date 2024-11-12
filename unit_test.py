import math
import unittest
import global_game_data
from pathing import get_bfs_path, get_dfs_path, get_dijkstra_path
import graph_data
import pyglet
from permutations import jst_permutations, valid_cycles
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
class TestPermute(unittest.TestCase):
    def test_permute1(self):
        permutations = jst_permutations(1)
        self.assertEqual(permutations, [[0]])
        pass

    def test_permute2(self):
        permutations = jst_permutations(2)
        self.assertEqual(permutations, [[0,1],[1,0]])
        pass
    
    def test_permute3(self):
        permutations = jst_permutations(3)
        self.assertEqual(permutations, [[0,1,2],[0,2,1],[2,0,1],[2,1,0],[1,2,0],[1,0,2]])
        pass
class TestCycle(unittest.TestCase):
    def test_cycle0(self):
        graph_data.graph_data[0] = [
            [(0, 0), [1, 2]],     
            [(100, 0), [0, 2, 3]],
            [(50, 100), [0, 1, 3, 4]],
            [(150, 100), [1, 2, 4]],
            [(100, 200), [2, 3]]   
        ]
        cycles = valid_cycles(0)
        print(cycles)
        paths = [
            [0, 1, 3, 4, 2],
            [0, 2, 4, 3, 1],
            [2, 0, 1, 3, 4],
            [4, 2, 0, 1, 3],
            [3, 4, 2, 0, 1],
            [2, 4, 3, 1, 0],
            [1, 3, 4, 2, 0],
            [3, 1, 0, 2, 4],
            [4, 3, 1, 0, 2],
            [1, 0, 2, 4, 3]
        ]
        self.assertEqual(cycles, paths)
        pass

    def test_cycle1(self):
        graph_data.graph_data[0] = [
        [(0, 0), [1]],
        [(200, -200), [2]],
        [(200, -400), [0]]
        ]
        cycles = valid_cycles(0)
        self.assertEqual(cycles, [[0, 1, 2], [2, 0, 1], [1, 2, 0]])
        pass


    def test_cycle2(self):
        graph_data.graph_data[0] = [
        [(0, 0), []],
        [(200, -200), []],
        [(200, -400), []]
        ]
        print(graph_data.graph_data[0])
        cycles = valid_cycles(0)
        self.assertEqual(cycles,  -1)
        pass
    
    def test_cycle3(self):
        graph_data.graph_data[0] = [
        [(0, 0), [2]],
        [(200, -200), [0]],
        [(200, -400), [1]]
        ]
        cycles = valid_cycles(0)
        self.assertEqual(cycles, [[0, 2, 1], [2, 1, 0], [1, 0, 2]])
        pass

class TestDijkstra(unittest.TestCase):
    def test_dijkstra1(self):
        global_game_data.current_graph_index = 0
        graph_data.graph_data[0] = [
        [(0, 0), [1]],
        [(200, -200), [2]],
        [(200, -400), []]
        ]
        path = get_dijkstra_path()
        self.assertEqual(path, [0, 1, 2])
        pass

    def test_dijkstra2(self):
        global_game_data.current_graph_index = 0
        graph_data.graph_data[0] = [
        [(0, 0), []],
        [(200, -200), []],
        [(200, -400), []]
        ]
        path = get_dijkstra_path()
        self.assertEqual(path, [])
        pass

    def test_dijkstra3(self):
        global_game_data.current_graph_index = 1
        path = get_dijkstra_path()
        self.assertEqual(path, [0, 1, 2, 3])
        pass

if __name__ == '__main__':
    pyglet.app.run()
    unittest.main()

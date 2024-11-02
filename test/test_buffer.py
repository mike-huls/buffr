# import unittest
# from typing import List, Any
#
# from buffr.buffers import Buffr
#
#
#
#
# class TestLRUCache(unittest.TestCase):
#
#
#
#     def test_returns_items_in_order(self):
#         result = []
#         def flush_func(items: List[Any]):
#             for i in items:
#                 result.append(i)
#
#         buffr = Buffr(max_capacity=100, time_interval=1, flush_func=flush_func)
#         for i in range(3):
#             buffr.add(i)
#         buffr.flush()
#
#         self.assertEqual(first=[0, 1, 2], second=result, msg="should be a list thats ordered lifo")
#
#     def test_lifo_works(self):
#         result = []
#         def flush_func(items: List[Any]):
#             for i in items:
#                 result.append(i)
#
#         buffr = Buffr(max_capacity=100, time_interval=1, flush_func=flush_func, fifo=False)
#         for i in range(3):
#             buffr.add(i)
#         buffr.flush()
#
#         self.assertEqual(first=[2, 1, 0], second=result, msg="should be a list thats ordered lifo")
#
#
# if __name__ == '__main__':
#     unittest.main()


import unittest
from typing import List, Any

from buffr.buffers import Buffr







def test_returns_items_in_order():
    result = []
    def flush_func(items: List[Any]):
        for i in items:
            result.append(i)

    buffr = Buffr(max_capacity=100, time_interval=1, flush_func=flush_func)
    for i in range(3):
        buffr.add(i)
    buffr.flush()

    assert [0, 1, 2] == result #should be a list thats ordered lifo

def test_lifo_works():
    result = []
    def flush_func(items: List[Any]):
        for i in items:
            result.append(i)

    buffr = Buffr(max_capacity=100, time_interval=1, flush_func=flush_func, fifo=False)
    for i in range(3):
        buffr.add(i)
    buffr.flush()

    assert [2, 1, 0] == result #should be a list thats ordered lifo

"""
python -m  coverage run -m pytest
coverage html
start chrome %cd%/htmlcov/index.html
"""
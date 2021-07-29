# -*- coding: UTF-8 -*-
import pytest
import sys
import os
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(os.path.split(rootPath)[0])

class Test_abc:



    @pytest.mark.parametrize("a",[3,8])
    def test_d1(self,a):
        print(f'\ntest_d1在执行{a}')

    @pytest.mark.parametrize("a", [(3, 8),(5,6)])
    def test_d21(self, a):
        print(f'test_d2在执行{a}')
    def test_a(self):
        a = 3+2
        print(a)
    def test_b(self):
        a = 3+2
        print(a)
    # def test_c(self):
    #     assert 0
    # def test_d(self):
    #     assert 0
    #
    # def test_e(self):
    #     assert 0
    #
    # def test_u(self):
    #     assert 0
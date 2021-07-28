# -*- coding: UTF-8 -*-
import pytest
import os
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
    def test_c(self):
        a = 3+2
        print(a)
    def test_d(self):
        a = 3+2
        print(a)

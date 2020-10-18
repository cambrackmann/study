
import pytest

def test_create_new_test():
    ret = set()
    ret.add('banana')
    ret.add('apple')
    assert 'apple' in ret
    assert 'pear' not in ret

def test_cams_test():
    me = 60
    you = 9
    assert me + you == 69

def test_array_test():
    ret = []
    ret += [1,2,5,69,420]
    assert ret[4] == 420

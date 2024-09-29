import pytest
import subprocess

def test_zero():
    f = 'zero.txt'
    res = subprocess.run(['wc', '--bytes', f], capture_output=True, text=True)
    print(res)
    expected = int(res.stdout.split()[0])
    
    ccwc = subprocess.run(['../src/ccwc/ccwc', '-c', f], capture_output=True, text=True)
    actual = int(ccwc.stdout.split()[0])

    assert expected == 0, 'wc should return 0!'
    assert actual == expected, f'Should be zero, got {actual}'


if __name__ == '__main__':
    pytest.main()
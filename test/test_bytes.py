import pytest
import subprocess

def run_on(filename):
    res = subprocess.run(['wc', '--bytes', filename], capture_output=True, text=True)
    print(res)
    expected = int(res.stdout.split()[0])
    
    ccwc = subprocess.run(['../src/ccwc/ccwc', '-c', filename], capture_output=True, text=True)
    actual = int(ccwc.stdout.split()[0])

    return (expected, actual)


def test_zero():
    expected, actual = run_on('zero.txt')
    assert expected == 0, 'wc should return 0!'
    assert actual == expected, f'Should be {expected}, got {actual}'


def test_bytes():
    expected, actual = run_on('test.txt')
    assert expected == 342190, 'wc should return 342190!'
    assert actual == expected, f'Should be {expected}, got {actual}'


if __name__ == '__main__':
    pytest.main()
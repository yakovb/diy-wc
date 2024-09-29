import pytest
import subprocess

def count_bytes_on(filename):
    res = subprocess.run(['wc', '--bytes', filename], capture_output=True, text=True)
    expected = int(res.stdout.split()[0])
    
    ccwc = subprocess.run(['../src/ccwc/ccwc', '-c', filename], capture_output=True, text=True)
    print(ccwc)
    actual = int(ccwc.stdout.split()[0])

    return (expected, actual)


def count_lines_on(filename):
    res = subprocess.run(['wc', '--lines', filename], capture_output=True, text=True)
    expected = int(res.stdout.split()[0])
    
    ccwc = subprocess.run(['../src/ccwc/ccwc', '-l', filename], capture_output=True, text=True)
    actual = int(ccwc.stdout.split()[0])

    return (expected, actual)


def test_zero():
    expected, actual = count_bytes_on('zero.txt')
    assert expected == 0, 'wc should return 0 bytes!'
    assert actual == expected, f'Should be {expected}, got {actual}'


def test_bytes():
    expected, actual = count_bytes_on('test.txt')
    assert expected == 342190, 'wc should return 342190 bytes!'
    assert actual == expected, f'Should be {expected}, got {actual}'


def test_lines():
    expected, actual = count_lines_on('test.txt')
    assert expected == 7145, 'wc should return 7145 lines!'
    assert actual == expected, f'Should be {expected}, got {actual}'


if __name__ == '__main__':
    pytest.main()
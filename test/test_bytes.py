import subprocess
import pytest

def test_zero():
    f = 'zero.txt'
    res = subprocess.run(['wc', '--bytes', f], capture_output=True, text=True)
    wc = int(res.stdout.split()[0])
    ccwc = 1

    assert wc == 0, 'wc should return 0!'
    assert ccwc == wc, f'Should be zero, got {ccwc}'


if __name__ == '__main__':
    pytest.main()
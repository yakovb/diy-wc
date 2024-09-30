import pytest
import subprocess


def do_count(cmd_wc, cmd_ccwc):
    res = subprocess.run(cmd_wc, capture_output=True, text=True)
    expected = int(res.stdout.split()[0])
    
    ccwc = subprocess.run(cmd_ccwc, capture_output=True, text=True)
    actual = int(ccwc.stdout.split()[0])

    return (expected, actual)


def count_bytes_on(filename):
    return do_count(
        ['wc', '-c', filename],
        ['../src/ccwc/ccwc', '-c', filename]
    )


def count_lines_on(filename):
    return do_count(
        ['wc', '-l', filename],
        ['../src/ccwc/ccwc', '-l', filename]
    )


def count_words_on(filename):
    return do_count(
        ['wc', '-w', filename],
        ['../src/ccwc/ccwc', '-w', filename]
    )


def count_chars_on(filename):
    return do_count(
        ['wc', '-m', filename],
        ['../src/ccwc/ccwc', '-m', filename]
    )

def count_all_on(filename):
    res = subprocess.run(['wc', filename], capture_output=True, text=True)
    expected = res.stdout.split()[:-1]
    
    ccwc = subprocess.run(['../src/ccwc/ccwc', filename], capture_output=True, text=True)
    actual = ccwc.stdout.split()[:-1]

    return (expected, actual)

def count_filename(filename):
    res = subprocess.run(['wc', filename], capture_output=True, text=True)
    expected = int(res.stdout.split()[-1])
    
    ccwc = subprocess.run(['../src/ccwc/ccwc', filename], capture_output=True, text=True)
    actual = int(ccwc.stdout.split()[-1])

    return (expected, actual)


def test_zero():
    expected, actual = count_bytes_on('zero.txt')
    assert expected == 0, 'wc should return 0 bytes!'
    assert actual == expected, f'Should be {expected}, got {actual}'


def test_bytes():
    expected, actual = count_bytes_on('test.txt')
    assert expected == 342190, 'wc should return 342190 bytes!'
    assert actual == expected, f'Should be {expected}, got {actual}'


def test_multibytes():
    expected, actual = count_bytes_on('multibyte.txt')
    assert expected == 7, 'wc should return 7 bytes!'
    assert actual == expected, f'Should be {expected}, got {actual}'


def test_lines():
    expected, actual = count_lines_on('test.txt')
    assert expected == 7145, 'wc should return 7145 lines!'
    assert actual == expected, f'Should be {expected}, got {actual}'


def test_words():
    expected, actual = count_words_on('test.txt')
    assert expected == 58164, 'wc should return 58164 words!'
    assert actual == expected, f'Should be {expected}, got {actual}'


def test_chars():
    expected, actual = count_chars_on('test.txt')
    assert expected == 339292, 'wc should return 339292 characters!'
    assert actual == expected, f'Should be {expected}, got {actual}'


def test_multibyte_chars():
    expected, actual = count_chars_on('multibyte.txt')
    assert expected == 5, 'wc should return 5 characters!'
    assert actual == expected, f'Should be {expected}, got {actual}'

def test_all():
    expected, actual = count_all_on('test.txt')
    assert expected == ['7145', '58164', '342190'], 'wc should return 7145, 58164, 342190!'
    assert actual == expected, f'Should be {expected}, got {actual}'

def test_all_multibyte():
    expected, actual = count_all_on('multibyte.txt')
    print(expected)
    assert expected == ['0', '3', '7'], 'wc should return 0, 3, 7!'
    assert actual == expected, f'Should be {expected}, got {actual}'

def test_filename():
    f = 'test.txt'
    expected, actual = count_filename(f)
    assert expected == f, 'wc should return test.txt!'
    assert actual == expected, f'Should be {expected}, got {actual}'


if __name__ == '__main__':
    pytest.main()
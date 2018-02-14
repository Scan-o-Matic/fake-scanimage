def test_scan_prints_file_stdout(capfdbinary, scanimage, history_file):
    with open(scanimage.get_scans()[0], 'rb') as fh:
        scan = fh.read()
    out, _ = capfdbinary.readouterr()
    assert len(out) == 0
    scanimage.scan()
    out, _ = capfdbinary.readouterr()
    assert scan == out


def test_scan_prints_second_file_stdout(capfdbinary, scanimage, history_file):
    with open(scanimage.get_scans()[1], 'rb') as fh:
        scan = fh.read()
    scanimage.scan()
    out, _ = capfdbinary.readouterr()
    scanimage.scan()
    out, _ = capfdbinary.readouterr()
    assert scan == out

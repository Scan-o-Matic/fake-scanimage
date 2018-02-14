import os


def test_gets_expected_count(scanimage):
    assert len(scanimage.get_scans()) == 3


def test_all_files_exits(scanimage):
    for f in scanimage.get_scans():
        assert os.path.isfile(f)


def test_all_files_are_tiffs(scanimage):
    for f in scanimage.get_scans():
        assert f.endswith('.tiff')


def test_files_are_sorted(scanimage):
    scans = scanimage.get_scans()
    assert "_0000_" in scans[0]
    assert "_0001_" in scans[1]
    assert "_0002_" in scans[2]

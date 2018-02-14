import pytest
import imp
import os
import tempfile


@pytest.fixture(scope='session')
def scanimage():
    return imp.load_source('scanimage', os.path.join(
        os.path.dirname(__file__),
        '../src/scanimage')
    )


@pytest.fixture
def history_file():
    with tempfile.NamedTemporaryFile() as tmp:
        os.environ['FAKE_SCANIMAGE_HISTORY'] = tmp.name
        yield tmp


@pytest.fixture
def scans():
    return ['img1.tiff', 'img2.tiff', 'img3.tiff', 'img4.tiff']

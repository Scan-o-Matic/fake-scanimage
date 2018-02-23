from datetime import datetime, timedelta

from freezegun import freeze_time
import pytest


def test_get_history_when_non_exists(scanimage, history_file):
    assert scanimage.get_stored_history() == {'scans': []}


def test_storing_and_then_loading_history(scanimage, history_file):
    history = scanimage.get_stored_history()
    assert history == {'scans': []}
    dt = datetime(1990, 10, 15, 8, 13)
    history['scans'].append(dt)
    scanimage.dump_history(history)
    with open(history_file.name, 'rb') as fh:
        assert (
            fh.read().decode() == '{"scans": ["1990-10-15T08:13:00.000000Z"]}'
        )
    assert scanimage.get_stored_history() == {'scans': [dt]}


class TestIsInSequence:
    def test_less_than_two_is_true(self, scanimage, history_file, scans):
        history = scanimage.get_stored_history()
        assert scanimage.is_in_sequence(history, scans)
        dt = datetime(1990, 10, 15, 8, 13)
        history['scans'].append(dt)
        assert scanimage.is_in_sequence(history, scans)

    def test_having_used_up_all_images_is_false(
        self, scanimage, history_file, scans,
    ):
        history = scanimage.get_stored_history()
        dt = datetime(1990, 10, 15, 8, 13)
        history['scans'] = [dt for _ in range(5)]
        assert not scanimage.is_in_sequence(history, scans)

    def test_having_used_up_all_images_trumps_less_than_two(
        self, scanimage, history_file, scans,
    ):
        history = scanimage.get_stored_history()
        dt = datetime(1990, 10, 15, 8, 13)
        history['scans'] = [dt]
        assert not scanimage.is_in_sequence(history, scans[:1])

    @pytest.mark.parametrize('delta_minutes,expect', (
        (11, True),
        (20, True),
        (39, True),
        (9, False),
        (41, False),
    ))
    def test_having_expected_delta_is_true(
        self, scanimage, history_file, scans, delta_minutes, expect
    ):
        history = scanimage.get_stored_history()
        dt1 = datetime(1990, 10, 15, 8, 13)
        dt2 = datetime(1990, 10, 15, 8, 33)
        history['scans'] = [dt1, dt2]
        with freeze_time((dt2 + timedelta(minutes=delta_minutes)).isoformat()):
            assert scanimage.is_in_sequence(history, scans) is expect

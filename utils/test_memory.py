import os
import pytest
from memory import update_history, display_history, delete_history


@pytest.fixture(autouse=True)
def setup_tmp_history(tmp_path, monkeypatch):
    """
    Redirect history file to a temporary directory for isolated tests.
    """
    tmp_history = tmp_path / "history"
    monkeypatch.setattr("memory.open", lambda *args, **kwargs: open(tmp_history, *args, **kwargs))
    monkeypatch.setattr("memory.os.remove", lambda *args, **kwargs: os.remove(tmp_history))
    monkeypatch.setattr("memory.os.path.exists", lambda *args, **kwargs: tmp_history.exists())


def test_update_history_add():
    update_history("1 add 2")
    assert display_history() == "1 | 1 + 2"


def test_update_history_modulo():
    delete_history()
    update_history("9 modulo 5")
    assert display_history() == "1 | 9 % 5"


def test_display_empty_history():
    delete_history()  # ensure empty
    # A new empty file exists → no content
    assert display_history() == "History is empty."


def test_display_no_history_file(monkeypatch):
    # Simulate FileNotFoundError
    monkeypatch.setattr("memory.open", lambda *args, **kwargs: (_ for _ in ()).throw(FileNotFoundError()))
    assert display_history() == "No history found."


def test_delete_history():
    update_history("5 multiply 2")
    result = delete_history()
    assert result == "History cleared."
    # Now there should be no entries
    assert display_history() == "History is empty."
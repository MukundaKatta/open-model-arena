"""Tests for ArenaManager."""
import pytest
from src.arenamanager import ArenaManager

def test_init():
    obj = ArenaManager()
    stats = obj.get_stats()
    assert stats["total_ops"] == 0

def test_operation():
    obj = ArenaManager()
    result = obj.create_battle(input="test")
    assert result["processed"] is True
    assert result["operation"] == "create_battle"

def test_multiple_ops():
    obj = ArenaManager()
    for m in ['create_battle', 'record_vote', 'update_elo']:
        getattr(obj, m)(data="test")
    assert obj.get_stats()["total_ops"] == 3

def test_caching():
    obj = ArenaManager()
    r1 = obj.create_battle(key="same")
    r2 = obj.create_battle(key="same")
    assert r2.get("cached") is True

def test_reset():
    obj = ArenaManager()
    obj.create_battle()
    obj.reset()
    assert obj.get_stats()["total_ops"] == 0

def test_stats():
    obj = ArenaManager()
    obj.create_battle(x=1)
    obj.record_vote(y=2)
    stats = obj.get_stats()
    assert stats["total_ops"] == 2
    assert "ops_by_type" in stats

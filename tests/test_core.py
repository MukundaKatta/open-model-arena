"""Tests for OpenModelArena."""
from src.core import OpenModelArena
def test_init(): assert OpenModelArena().get_stats()["ops"] == 0
def test_op(): c = OpenModelArena(); c.process(x=1); assert c.get_stats()["ops"] == 1
def test_multi(): c = OpenModelArena(); [c.process() for _ in range(5)]; assert c.get_stats()["ops"] == 5
def test_reset(): c = OpenModelArena(); c.process(); c.reset(); assert c.get_stats()["ops"] == 0
def test_service_name(): c = OpenModelArena(); r = c.process(); assert r["service"] == "open-model-arena"

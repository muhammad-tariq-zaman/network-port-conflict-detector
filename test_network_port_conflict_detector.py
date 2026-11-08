import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import unittest
from main import find_conflicts

def row(h, p, s):
    return {"host": h, "port": str(p), "service": s}

class TestPortConflicts(unittest.TestCase):
    def test_conflict_found(self):
        c = find_conflicts([row("PC-1", 8080, "web"), row("PC-1", 8080, "proxy")])
        self.assertEqual(c, [("PC-1", 8080, ["proxy", "web"])])
    def test_no_conflict_different_ports(self):
        self.assertEqual(find_conflicts([row("PC-1", 80, "web"), row("PC-1", 443, "web")]), [])
    def test_same_service_twice_not_conflict(self):
        self.assertEqual(find_conflicts([row("PC-1", 8080, "web"), row("PC-1", 8080, "web")]), [])
    def test_same_port_different_hosts_ok(self):
        self.assertEqual(find_conflicts([row("PC-1", 8080, "web"), row("PC-2", 8080, "proxy")]), [])
    def test_lowest_port_first(self):
        c = find_conflicts([row("PC-1", 9000, "a"), row("PC-1", 9000, "b"),
                            row("PC-1", 80, "a"), row("PC-1", 80, "b")])
        self.assertEqual(c[0][1], 80)
    def test_empty_input(self):
        self.assertEqual(find_conflicts([]), [])

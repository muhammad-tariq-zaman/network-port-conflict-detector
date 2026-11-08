"""Detect port conflicts: two different services on one host:port.

Usage: python3 main.py ports.csv
CSV columns: host,port,service.
A conflict is the same host and port claimed by two or more
different services. The same port on different hosts is fine,
and the same service listed twice is not a conflict.
Conflicts are listed lowest port first.
"""
import argparse, csv, sys
from collections import defaultdict

def find_conflicts(rows):
    by_endpoint = defaultdict(set)
    for row in rows:
        key = (row["host"].strip(), int(row["port"]))
        by_endpoint[key].add(row["service"].strip())
    conflicts = []
    for (host, port), services in by_endpoint.items():
        if len(services) > 1:
            conflicts.append((host, port, sorted(services)))
    return sorted(conflicts, key=lambda c: (c[1], c[0]))

def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("path")
    args = parser.parse_args(argv)
    with open(args.path, newline="", encoding="utf-8") as f:
        conflicts = find_conflicts(list(csv.DictReader(f)))
    for host, port, services in conflicts:
        print(f"{host}:{port}: CONFLICT ({', '.join(services)})")
    if not conflicts:
        print("No port conflicts found.")
    else:
        print(f"{len(conflicts)} conflict(s) found.")
    return 0

if __name__ == "__main__":
    sys.exit(main())

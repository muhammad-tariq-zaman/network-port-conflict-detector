# network-port-conflict-detector

Detect port conflicts from a CSV of host, port and service: the same host:port claimed by two or more different services is a CONFLICT — lowest port first.

## How to run

```sh
python3 main.py ports.csv
```

## Example output

```
PC-1:8080: CONFLICT (proxy, web)
1 conflict(s) found.
```

Standard library only. Run the tests with `python3 -m unittest discover`.

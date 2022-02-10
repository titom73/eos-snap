# eos-snap

Work in Progress

## Install

### For testing only

```bash
git clone
cd eos-snap
pip install .
```

### For development

```bash
git clone
cd eos-snap
python setup.py develop
```

### Update eapi configuration

Edit [eapi.conf](.tests/../tests/eapi.conf) to match your setup

```ini
[connection:veos01]
host: 10.73.1.241
port: 8033
transport: https
username: ansible
password: ansible
```

> Configuration reference available in [pyeapi documentation](https://pyeapi.readthedocs.io/en/master/configfile.html)

Load eAPI configuration in your shell:

```bash
source load-eos-test-env.sh
```

## Launch scripts

### Collect snapshots

```bash
$ python bin/eos-snapshot --configuration tests/data/config.yml --verbose debug --rootpath demo --stage pre

2022-01-27 16:13:09.375 | DEBUG    | __main__:<module>:44 - configuration is {'devices': ['veos01'], 'test_cases': [{'name': 'Test01', 'command': 'show version', 'path': 'unset', 'check_key': 'unset', 'iterator': 'unset', 'snapshot': {}}, {'name': 'Test02', 'command': 'show interfaces description', 'path': 'unset', 'check_key': 'unset', 'iterator': 'unset', 'snapshot': {}}, {'name': 'Test01', 'command': 'show bgp evpn summary', 'path': 'unset', 'check_key': 'unset', 'iterator': 'unset', 'snapshot': {}}]}

2022-01-27 16:13:09.375 | INFO     | __main__:<module>:46 - Collecting snapshot for device(s): ['veos01']

2022-01-27 16:13:09.375 | INFO     | __main__:<module>:48 -   - Grab data from device veos01

2022-01-27 16:13:10.164 | INFO     | eos_snap.devices:save_snapshot:51 - Save command "show version" to demo/veos01/
pre/show_version.json for host veos01

2022-01-27 16:13:10.165 | INFO     | eos_snap.devices:save_snapshot:51 - Save command "show interfaces description" to demo/veos01/pre/show_interfaces_description.json for host veos01

2022-01-27 16:13:10.166 | INFO     | eos_snap.devices:save_snapshot:51 - Save command "show bgp evpn summary" to demo/veos01/pre/show_bgp_evpn_summary.json for host veos01
```

__Remember__: As we do snapshot comparison, you do have to collect `pre` and `post` stages

> A fake configuration file is available under [tests/data/config.yml](.tests/data/config.yml)

### Compare snapshots

```bash
python bin/eos-snap-compare --configuration tests/data/config.yml --rootpath demo
2022-02-10 15:35:57.307 | INFO     | __main__:<module>:44 - Loading snapshot
2022-02-10 15:35:57.416 | INFO     | __main__:<module>:57 - Load test [ EOS Version ]
2022-02-10 15:35:57.468 | WARNING  | __main__:<module>:65 -   * Test result is: {'state': True, 'errors': []}
2022-02-10 15:35:57.468 | INFO     | __main__:<module>:57 - Load test [ BGP Session ]
2022-02-10 15:35:57.510 | ERROR    | __main__:<module>:65 -   * Test result is: {'state': False, 'errors': [{'key': '192.168.255.3', 'pre': 'Established', 'post': 'Down'}, {'key': '192.168.255.4', 'pre': 'Active', 'post': 'Established'}]}
2022-02-10 15:35:57.510 | INFO     | __main__:<module>:57 - Load test [ BGP Session Maintenance ]
2022-02-10 15:35:57.557 | ERROR    | __main__:<module>:65 -   * Test result is: {'state': False, 'errors': [{'key': '192.168.255.3', 'pre': '4', 'post': '5'}, {'key': '192.168.255.4', 'pre': 'False', 'post': 'True'}]}
```

Tests are defined in configuration file.  A fake configuration file is available under [tests/data/config.yml](.tests/data/config.yml)

## Supported tests

- `is_equal`: Ensure value of given keys are equal in `pre` and `post` snapshots.

## Configuration syntax

Tests are all saved under `test_cases` knob with the following syntax:

- `name`: Test Name and is user defined
- `command`: EOS CLI command to use to get data
- `iterator`: JSON Path to use to get data. You can search for a dictionary or a nested dictionary where you can iterate.
- `check_keys`: JSON Path keys to compare in the test.
- `operator`: Type of comparison to use.

```yaml
  test_cases:
    - name: EOS Version
      command: 'show version'
      check_keys: ['version']
      iterator: '$'
      snapshot: {}
      operator: is_equal

    - name: BGP Session
      command: 'show bgp evpn summary'
      check_keys: ['peerState']
      iterator: 'vrfs.default.peers[*]'
      snapshot: {}
      operator: is_equal

    - name: BGP Session Maintenance
      command: 'show bgp evpn summary'
      check_keys: ['underMaintenance', 'version']
      iterator: 'vrfs.default.peers[*]'
      snapshot: {}
      operator: is_equal
```

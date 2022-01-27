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

## Launch script

```bash
$ python bin/eos-snapshot --configuration tests/data/config.yml --verbose debug --rootpath demo

2022-01-27 16:13:09.375 | DEBUG    | __main__:<module>:44 - configuration is {'devices': ['veos01'], 'test_cases': [{'name': 'Test01', 'command': 'show version', 'path': 'unset', 'check_key': 'unset', 'iterator': 'unset', 'snapshot': {}}, {'name': 'Test02', 'command': 'show interfaces description', 'path': 'unset', 'check_key': 'unset', 'iterator': 'unset', 'snapshot': {}}, {'name': 'Test01', 'command': 'show bgp evpn summary', 'path': 'unset', 'check_key': 'unset', 'iterator': 'unset', 'snapshot': {}}]}

2022-01-27 16:13:09.375 | INFO     | __main__:<module>:46 - Collecting snapshot for device(s): ['veos01']

2022-01-27 16:13:09.375 | INFO     | __main__:<module>:48 -   - Grab data from device veos01

2022-01-27 16:13:10.164 | INFO     | eos_snap.devices:save_snapshot:51 - Save command "show version" to demo/veos01/
pre/show_version.json for host veos01

2022-01-27 16:13:10.165 | INFO     | eos_snap.devices:save_snapshot:51 - Save command "show interfaces description" to demo/veos01/pre/show_interfaces_description.json for host veos01

2022-01-27 16:13:10.166 | INFO     | eos_snap.devices:save_snapshot:51 - Save command "show bgp evpn summary" to demo/veos01/pre/show_bgp_evpn_summary.json for host veos01
```

> A fake configuration file is available under [tests/data/config.yml](.tests/data/config.yml)

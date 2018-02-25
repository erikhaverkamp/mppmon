# mppmon
System to keep PV modules in MPP and measure IV curves

# configuration
Configure module settings in config.py

# private (hidden) configuration
The system expects a file named private.py. In here some private variables need to be declared:
```
COMPORT = '/dev/serial/by-id/NAME_OF_USB_DEV'
INFLUX_HOST = 'https://INFLUX_SERVER:8086'
INFLUX_DB = 'INFLUX_DB'
INFLUX_USER = 'INFLUX_USERNAME'
INFLUX_PWD = 'INFLUX_PASSWORD'
```

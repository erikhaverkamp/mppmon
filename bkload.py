import sys
import dcload
from time import sleep
err = sys.stderr.write


class IvTracer:
    def __init__(self, comport, max_voltage=500, max_current=15):
        self.MaxVoltage = max_voltage
        self.MaxCurrent = max_current
        self.load = dcload.DCLoad()
        self.load.Initialize(comport, 38400)
        self.load.SetRemoteControl()
        self.load.SetMode('cv')
        self.load.SetMaxVoltage(max_voltage)
        self.load.SetMaxCurrent(max_current)
        self.load.SetCVVoltage(max_voltage)

        values = self.load.GetProductInformation()
        for value in values.split("\t"): print "    ", value

    def get_load_object(self):
        return self.load

    def measure_values(self):
        s = self.load.GetInputValues()
        vals = s.split('\t')
        return {'voltage': float(vals[0].split(' ')[0]),
                'current': float(vals[1].split(' ')[0])}

    def set_voltage(self, voltage):
        self.load.SetCVVoltage(voltage)

    def set_max_voltage(self, voltage):
        self.load.SetMaxVoltage(voltage)

    def set_max_current(self, voltage):
        self.load.SetMaxCurrent(voltage)

    def get_voc(self):
        self.load.SetCVVoltage(self.MaxVoltage)
        self.on()
        d = self.measure_values()
        self.off()
        return d['voltage']

    def measure_iv(self, points, delay=0.1):
        result = []
        start = self.get_voc()
        print('start: %f' % (start))
        if start < 3:
            print('voc too low')
            return {}
        step = start / points
        print('step: %f' % (step))
        self.set_voltage(0.4)
        self.on()

        for i in range(points):
            sleep(delay)
            self.set_voltage(step * i + 0.4)
            result.append(self.measure_values())

        self.off()
        self.set_voltage(self.MaxVoltage)
        return result

    def on(self):
        self.load.TurnLoadOn()

    def off(self):
        self.load.TurnLoadOff()

    def close(self):
        self.load.SetLocalControl()
        self.load.ClosePort()



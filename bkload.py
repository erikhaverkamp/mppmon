import sys, dcload

err = sys.stderr.write


class IvTracer:
    def __init__(self, comport):
        load = dcload.DCLoad()
        load = dcload.DCLoad()
        load.Initialize(comport, 38400)
        load.SetRemoteControl()
        print "Time from DC Load =", load.TimeNow()
        load.SetCVVoltage(10)
        values = load.GetProductInformation()
        for value in values.split("\t"): print "    ", value
        load.SetLocalControl()
        load.ClosePort()
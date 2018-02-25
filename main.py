from multiplexer import Multiplexer
import bkload
import datetime
import config as cfg
import private
import logging
import os


LOG_FOLDER = './log'
INFLUX_FOLDER = './influx_lines'
DATE_FILENAME = datetime.datetime.now().strftime("%Y%m%d")


def store_iv_curves(iv, timestamp):
    try:
        with open(os.path.join(INFLUX_FOLDER, DATE_FILENAME + '.line', 'a') as f:
            f.write("voltage\tcurrent\tpower\n")
            for d in iv:
                f.write("%f\t%f\t%f\n" % (d['voltage'], d['current'], d['power']))
            f.close()

    except Exception, e:
        print(e)
        logging.exception(e)
        raise SystemExit(0)


def setup_folders(log_dir, influx_dir):
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)

    if not os.path.exists(influx_dir):
        os.makedirs(influx_dir)


def main():
    setup_folders(LOG_FOLDER, INFLUX_FOLDER)
    logging.basicConfig(filename=os.path.join(LOG_FOLDER, DATE_FILENAME + '.log'),
                        level=logging.INFO)
    logging.info('start mppmon')

    try:
        t = bkload.IvTracer(private.COMPORT)
    except Exception, e:
        print(e)
        logging.error(e)
        raise SystemExit(0)

    try:
        mp = Multiplexer()
        mp.SelectChannel(-1)
    except Exception, e:
        print(e)
        logging.exception(e)
        raise SystemExit(0)

    for k in cfg.sweep_settings.keys():
        p = cfg.sweep_settings[k]
        if p.enabled:
            mp.SelectChannel(p.channel)

            d = t.measure_iv(p.points, p.sweeptime/p.points)
            store_iv_curves(d, datetime.datetime.now())


if __name__ == '__main__':
    main()
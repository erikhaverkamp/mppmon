from multiplexer import Multiplexer
import bkload
import datetime
import config as cfg
import private
import logging
import os
import inflect
import requests
import iv_curve_sample

LOG_FOLDER = './log'
INFLUX_FOLDER = './influx_lines'
DATE_FILENAME = datetime.datetime.now().strftime("%Y%m%d")


def post_to_influx(msg):
    url = private.INFLUX_HOST + ":8086/write?db=" + private.INFLUX_DB + "&precision=ms"
    r = requests.post(url, data=msg, auth=(private.INFLUX_USER, private.INFLUX_PWD))
    print(r)


def store_iv_curve(iv, tag, timestamp):
    ts = 1000 * int((timestamp - datetime.datetime(1970, 1, 1)).total_seconds())
    try:
        with open(os.path.join(INFLUX_FOLDER, DATE_FILENAME + '.line'), 'a') as f:
            for d in iv:
                v_line = "IVpoints,module=%s voltage=%f %d\n" %(tag, d['voltage'], ts)
                i_line = "IVpoints,module=%s current=%f %d\n" % (tag, d['current'], ts)
                f.write(v_line)
                f.write(i_line)
                post_to_influx(v_line)
                post_to_influx(i_line)
                ts = ts + 1
            f.close()

    except Exception, e:
        print(e)
        logging.error(e)
        raise SystemExit(0)


def setup_folders(log_dir, influx_dir):
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)

    if not os.path.exists(influx_dir):
        os.makedirs(influx_dir)


def main():
    z = inflect.engine()
    setup_folders(LOG_FOLDER, INFLUX_FOLDER)
    logging.basicConfig(filename=os.path.join(LOG_FOLDER, DATE_FILENAME + '.log'),
                        level=logging.INFO)
    logging.info('start mppmon')

    store_iv_curve(iv_curve_sample.curve, p.number_to_words(5), datetime.datetime.now())

    try:
        t = bkload.IvTracer(private.COMPORT)
    except Exception, e:
        print(e)
        logging.error(e)
        raise SystemExit(0)

    try:
        mp = Multiplexer()
        mp.ChannelsOff()
    except Exception, e:
        print(e)
        logging.error(e)
        raise SystemExit(0)

    for k in cfg.sweep_settings.keys():
        p = cfg.sweep_settings[k]
        if p.enabled:
            mp.SelectChannel(p.channel)
            d = t.measure_iv(p.points, p.sweeptime/p.points)
            store_iv_curve(d, z.number_to_words(p.channel+1), datetime.datetime.now())


if __name__ == '__main__':
    main()
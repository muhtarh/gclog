import matplotlib.pyplot as plt
import numpy as np
import cdf.cdf as cdf
import parser.go_parser as go_parser


def generate_chart(file_path, chart_title):
    print('parsing log file' + file_path)
    lats = go_parser.parse_gc_log_sorted(file_path)
    t = np.arange(0.1, 150.0, 0.001)
    print('generating cdf from' + file_path)
    cdf_value = cdf.generate_cdf(lats, t)
    plt.plot(t, cdf_value)
    plt.xlabel('latency time (ms)')
    plt.ylabel('CDF')
    plt.title(chart_title)
    chart_name = 'chart/' + chart_title + '.png'
    print('save chart : ' + chart_name)
    plt.savefig(chart_name)
    plt.clf()

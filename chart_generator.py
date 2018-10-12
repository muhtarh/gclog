import matplotlib.pyplot as plt
import numpy as np
import cdf.cdf as cdf
import parser.go_parser as go_parser


def generate_chart(file_path):
    print('parsing log file')
    lats = go_parser.parse_gc_log_sorted(file_path)
    t = np.arange(0.1, 150.0, 0.001)
    print('generating cdf')
    cdf_value = cdf.generate_cdf(lats, t)
    plt.plot(t, cdf_value)
    plt.xlabel('latency time (ms)')
    plt.ylabel('CDF')
    plt.title('Golang GC Latency')
    chart_name = 'chart/mychart.png'
    print('save chart : ' + chart_name)
    plt.savefig(chart_name)
    plt.clf()

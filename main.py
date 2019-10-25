import os
import chart_generator as chart

root = os.environ['GO_GC_LOG']
for root, dirs, files in os.walk(root):
    for filename in files:
        filePath = os.path.join(root, filename)
        chart_title = 'Message Size ' + filename
        chart.generate_chart(filePath, chart_title)

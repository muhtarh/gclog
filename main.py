import os
import chart_generator as chart

root = '/home/muhtar-hartopo/playground/go-exp/gc/logs/go'
for root, dirs, files in os.walk(root):
    for filename in files:
        filePath = os.path.join(root, filename)
        chart_title = 'Message Size ' + filename
        chart.generate_chart(filePath, chart_title)

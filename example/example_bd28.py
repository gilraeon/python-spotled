import spotled
import time
import sys

sender = spotled.LedConnection(sys.argv[1])
print('sending text')
sender.set_text_bd28('%4BA1212   VIE\nDEP.      %2+00:14',font="5x7",line_height=8)
print('text sent')

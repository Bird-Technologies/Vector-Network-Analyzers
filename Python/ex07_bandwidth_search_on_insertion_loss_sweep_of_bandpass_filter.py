"""
Example Description:
        This example shows how to use remote commands to perform the
        bandpass filter characterization steps that are covered in the
        associated application note featured on the VNA landing pages
        on birdrf.com. Specifically, this includes defining the frequency
        range of interest, measuring insertion loss at select points
        using markers; enabling the bandwidth search to help evaluate
        the capability of the bandpass filter inserted between the two
        test ports. 

@verbatim

The MIT License (MIT)

Copyright (c) 2024 Bird

Permission is hereby granted, free of charge, to any person obtaining a copy of
this software and associated documentation files (the "Software"), to deal in
the Software without restriction, including without limitation the rights to
use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies
of the Software, and to permit persons to whom the Software is furnished to do
so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

@endverbatim

@file ex07_bandwidth_search_on_insertion_loss_sweep_of_bandpass_filter.py
 
"""
from bird_vector_network_analyzer import BirdVectorNetworkAnalyzer
from time import sleep

bna1k = BirdVectorNetworkAnalyzer()

# Connect to the instrument and clear out any error conditions. 
bna1k.initialize("TCPIP0::127.0.0.1::inst0::INSTR")
bna1k.get_error_list()
bna1k.system.preset()
bna1k.opc_query()

bna1k.channel = 1
bna1k.trace = 1

# Set the center frequency, span, and points
bna1k.sense.frequency.center = 433e6
bna1k.sense.frequency.span = 20e6
bna1k.sense.sweep.points = 1601

############################################################
#       If you have not yet performed calibration it
#       is highly recommended that you do so useing the
#       start, stop, and point attributes applied 
#       above. 
############################################################

# Do S11 for return loss, setting three markers at points of 
# interest: both -10 dB points at either side of the band of
# interest as well as one at the center point. Get the marker
# data and print to the console. 
bna1k.calculate.parameter.tracecount = 1
bna1k.calculate.parameter.traceselect = 1
temp = bna1k.calculate.parameter.trace_sparam
bna1k.display.window.maximize = 1
bna1k.calculate.parameter.trace_sparam = "s21"
bna1k.calculate.format.type = "mlog"
bna1k.display.window.trace.y.autoscale()

bna1k.marker = 1
bna1k.calculate.marker.state = 1
bna1k.calculate.marker.set("center")
val1, val2 = bna1k.calculate.marker.y()

bna1k.marker = 2
bna1k.calculate.marker.state = 1
bna1k.calculate.marker.x = 428e6
val1, val2 = bna1k.calculate.marker.y()

bna1k.marker = 3
bna1k.calculate.marker.state = 1
bna1k.calculate.marker.x = 438e6
val1, val2 = bna1k.calculate.marker.y()

# clear existing limit lines
bna1k.calculate.limit.clearlines()
# add a limit line
bna1k.calculate.limit.addline(1, 'maximum', 428e6, 438e6, -17.0, -17.0)
# enable the limit test
bna1k.calculate.limit.teststate = 1
# enable the limit line
bna1k.calculate.limit.lineenable = 1
# enable the large fail sign
bna1k.display.failsign(1)
# get the limit test state and print to the console
print(bna1k.calculate.limit.failstatus())

bna1k.close()

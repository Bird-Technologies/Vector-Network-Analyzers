"""
Example Description:
        This example shows how to configure the VNA for a segmented sweep
        using a single port return loss measurement (S11 parameters). The
        segments are chosen based on the four most prominent return loss
        areas witnessed when evaluating a Bird AT-800 antenna at 329 MHz,
        834 MHz, 888 MHz, and 2.4 GHz. The number of sweep points and time
        are returned to the operator then the segment table is saved to
        file for later recall. 


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

@file ex04_triggered_return_loss_sweep.py
 
"""
from bird_vector_network_analyzer import BirdVectorNetworkAnalyzer

bna1k = BirdVectorNetworkAnalyzer()

# Connect to the instrument and clear out any error conditions
bna1k.initialize("TCPIP0::127.0.0.1::inst0::INSTR")
bna1k.get_error_list()

bna1k.channel = 1
bna1k.trace = 1

# Halt continuous triggering, configure for bus triggering
bna1k.initiate.continuous = 0
bna1k.trigger.source = 'bus'

bna1k.sense.sweep.sweeptype = "segment"
tempj = bna1k.sense.sweep.sweeptype

recall_seg_table = 0
if recall_seg_table == 0:
        bna1k.sense.segment.create_segment_table(mode=0, ifbw_en=1, pwr_en=0, del_en=0, swp_en=0, segment_count=8,
                                         start_n=(300e3, 290e6, 350e6, 824e6, 850e6, 878e6, 898e6, 2.3e9),
                                         stop_n= (290e6, 350e6, 824e6, 850e6, 878e6, 898e6, 2.3e9, 2.5e9),
                                         pts_n=  (    2,   101,     2,   101,     2,   101,     2,   101), 
                                         ifbw_n= ( 70e3,  70e3,  70e3,  70e3,  70e3,  70e3,  70e3,  70e3))
        bna1k.mmemory.store.segment_table("ant800.seg")
else:
        bna1k.mmemory.load.segment_table("ant800.seg")

point_count = bna1k.sense.segment.sweep.points()
point_time = bna1k.sense.segment.sweep.time()

# Include this to show how a user can enable and disable measurements for different segments for a given sweep. 
bna1k.sense.segment.list.controldata = (1,1,1,1,1,1,1,1)

############################################################
#       If you have not yet performed calibration it
#       is highly recommended that you do so useing the
#       start, stop, and point attributes applied 
#       above. 
############################################################

# Do S11 for return loss, setting three markers at points of 
# interest: both -10 dB points at either side of the band of
# interest as well as one at the lowest point. Get the marker
# data and print to the console. 
bna1k.calculate.parameter.tracecount = 1
bna1k.calculate.parameter.traceselect = 1
temp = bna1k.calculate.parameter.trace_sparam
bna1k.calculate.parameter.trace_sparam = "s11"
print(bna1k.calculate.format.type)
bna1k.calculate.format.type = "mlog"

# Trigger the sweep the autoscale the trace.
bna1k.trigger.immediate()
bna1k.opc_query()
bna1k.display.window.trace.y.autoscale()

bna1k.marker = 1
print(bna1k.calculate.marker.state)
bna1k.calculate.marker.state = 1
bna1k.calculate.marker.set("center")
val1, val2 = bna1k.calculate.marker.y()

bna1k.marker = 2
bna1k.calculate.marker.state = 1
bna1k.calculate.marker.x = 824e6
val1, val2 = bna1k.calculate.marker.y()

bna1k.marker = 3
bna1k.calculate.marker.state = 1
bna1k.calculate.marker.x = 900e6
val1, val2 = bna1k.calculate.marker.y()

bna1k.close()


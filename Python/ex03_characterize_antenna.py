"""
Example Description:
        This example shows how to use remote commands to perform the
        antenna characterization steps that are covered in our the
        associated application note featured on the VNA landing pages
        on birdrf.com.

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

@file ex03_characterize_antenna.py
 
"""
from bird_vector_network_analyzer import BirdVectorNetworkAnalyzer

bna1k = BirdVectorNetworkAnalyzer()

# Connect to the instrument and clear out any error conditions
bna1k.initialize("TCPIP0::127.0.0.1::inst0::INSTR")
bna1k.get_error_list()

bna1k.channel = 1
bna1k.trace = 1

# Set the center frequency, span, and points
bna1k.sense.frequency.start = 800e6
bna1k.sense.frequency.stop = 925e6
bna1k.sense.sweep.points = 1001

############################################################
#       If you have not yet performed calibration it
#       is highly recommended that you do so useing the
#       start, stop, and point attributes applied 
#       above. 
############################################################

# If needed perform the following port extension measurement
# if any unexpected connnector gets applied after the 
# measurement calibration is performed. Note that the act of
# successfully performing auto extension measurement will
# enable the feature. 
bna1k.port = 2
bna1k.sense.correction.extension.auto.port = "off"
bna1k.port = 1
bna1k.sense.correction.extension.auto.port = "on"
bna1k.sense.correction.extension.auto.measure("open")

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
bna1k.display.window.trace.y.autoscale()

bna1k.marker = 1
print(bna1k.calculate.marker.state)
bna1k.calculate.marker.state = 1
bna1k.calculate.marker.set("center")
val1, val2 = bna1k.calculate.marker.y()

bna1k.marker = 2
bna1k.calculate.marker.state = 1
bna1k.calculate.marker.x = 824e6

bna1k.marker = 3
bna1k.calculate.marker.state = 1
bna1k.calculate.marker.x = 900e6

# Add a second trace in the same channel to display VSWR, 
# make it active, and use the same markers to help print
# data to the console. 
bna1k.calculate.parameter.tracecount = 2
bna1k.trace = 2
bna1k.calculate.parameter.traceselect = bna1k.trace
temp = bna1k.calculate.parameter.trace_sparam
bna1k.calculate.parameter.trace_sparam = "s11"
bna1k.calculate.format.type = "swr"
bna1k.display.window.trace.y.autoscale()

# Add a third trace and allocate it in a different pane, 
# make it active, measure the impedance values on the 
# Smith chart. Print the marker data to the console. 


# Next

# Set the calibration kit to be used 
bna1k.sense.correction.collection.calkit.select = 1
input("Connect the OPEN standard then enter y to continue.")
bna1k.sense.correction.collection.calibrate_open(1)
input("Connect the SHORT standard then enter y to continue.")
bna1k.sense.correction.collection.calibrate_short(1)
input("Connect the LOAD standard then enter y to continue.")
bna1k.sense.correction.collection.calibrate_load(1)

bna1k.sense.correction.collection.calibrate_save()

bna1k.close()


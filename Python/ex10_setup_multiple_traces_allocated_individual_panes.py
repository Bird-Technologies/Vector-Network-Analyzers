"""
Example Description:
        This example shows how to use remote commands to perform a single
        port calibration on the vector network analyzer.

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

@file ex01_single_port_calibration.py
 
"""
from bird_vector_network_analyzer import BirdVectorNetworkAnalyzer

bna1k = BirdVectorNetworkAnalyzer()

# Connect to the instrument and clear out any error conditions. 
bna1k.initialize("TCPIP0::127.0.0.1::inst0::INSTR")
bna1k.get_error_list()

bna1k.system.preset()
bna1k.channel = 1
bna1k.trace = 1

# Set the start and stop frequencies along with the points
bna1k.sense.frequency.start = 350e6
bna1k.sense.frequency.stop = 2.7e9
bna1k.sense.sweep.points = 1001

# Allocate four traces within the channel and lay them out in a 2x2 matrix
bna1k.calculate.parameter.tracecount = 4
bna1k.display.window.layout = 7

# Configure trace 1 for S11 & log magnitude measurements
bna1k.calculate.parameter.trace_sparam = "s11"
bna1k.calculate.format.type = "mlog"
divs = bna1k.display.window.trace.y.scale
bna1k.display.window.trace.y.autoscale()
bna1k.display.window.trace.y.scale = 10.0

# Configure trace 2 for S21 & log magnitude measurements
bna1k.trace = 2
bna1k.calculate.parameter.trace_sparam = "s21"
divs = bna1k.display.window.trace.y.scale
bna1k.calculate.format.type = "mlog"
bna1k.display.window.trace.y.autoscale()
bna1k.display.window.trace.y.scale = 10.0

# Configure trace 3 for S12 & log magnitude measurements
bna1k.trace = 3
bna1k.calculate.parameter.trace_sparam = "s12"
divs = bna1k.display.window.trace.y.scale
bna1k.calculate.format.type = "mlog"
bna1k.display.window.trace.y.autoscale()
bna1k.display.window.trace.y.scale = 10.0

# Configure trace 4 for S22 & log magnitude measurements
bna1k.trace = 4
bna1k.calculate.parameter.trace_sparam = "s22"
divs = bna1k.display.window.trace.y.scale
bna1k.calculate.format.type = "mlog"
bna1k.display.window.trace.y.autoscale()
bna1k.display.window.trace.y.scale = 10.0

# Set markers at select frequencies
bna1k.trace = 1
bna1k.marker = 1
mkr_freqs = (380e6, 423e6, 770.5e6, 816e6, 876.5e6, 921.5e6, 940.1e6, 1.4595e9, 1.8451e9, 1.9050e9, 2.1454e9, 2.6550e9)
for freq in mkr_freqs:
    bna1k.calculate.marker.state = 1
    bna1k.calculate.marker.x = freq
    bna1k.marker += 1
    st = bna1k.opc_query()

for trace in range(1, 5):
    bna1k.trace = trace
    for j in range(1, 13):
        bna1k.marker = j
        val1, val2 = bna1k.calculate.marker.y()
        print(f"Trace{bna1k.trace}, Marker{bna1k.marker}: {val1}, {val2}")
        
bna1k.close()

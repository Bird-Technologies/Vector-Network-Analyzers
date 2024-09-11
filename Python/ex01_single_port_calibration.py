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

# Set the center frequency, span, and points
bna1k.sense.frequency.center = 433e6
bna1k.sense.frequency.span = 20e6
bna1k.sense.sweep.points = 1001

# Set the calibration kit to be used and step through connections
bna1k.sense.correction.collection.calkit.select = 1
input("Connect the OPEN standard then enter y to continue.")
bna1k.sense.correction.collection.calibrate_open(1)
input("Connect the SHORT standard then enter y to continue.")
bna1k.sense.correction.collection.calibrate_short(1)
input("Connect the LOAD standard then enter y to continue.")
bna1k.sense.correction.collection.calibrate_load(1)

# Save the correction coefficients obtained during cal measurements
bna1k.sense.correction.collection.calibrate_save()

bna1k.close()

"""
Example Description:
        This example shows how to use remote commands to perform a two
        port calibration on the vector network analyzer using the ECal
        (electronic calibration) module. You will note that in comparison
        to the manual 2-port calibration, the coding is simpler which
        aligns with the simplicity and limited connections to the ECal
        standard/module. 

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

@file ex05_two_port_calibration_using_ecal_module.py
 
"""
from bird_vector_network_analyzer import BirdVectorNetworkAnalyzer
from time import sleep

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

# Identify the ports to be calibrated, notify the operator of connections
# needed, then execute the Ecal. A mimimum delay time of 5 s is applied
# before the operation complete query is issued. 
porta = 1
portb = 2

input(f"Connect ports {porta} and {portb} to the Ecal module then enter y to continue.")

bna1k.sense.correction.collection.electronic_calibration('solt2', 1, 2)
sleep(5000)
bna1k.opc_query()

bna1k.close()

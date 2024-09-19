/*
 * 
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

@file ex01_single_port_calibration.cs
 
 * 
 */
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using NationalInstruments.Visa;

namespace ex01_single_port_calibration_alt01
{
    internal class ex01_single_port_calibration
    {
        static void Main(string[] args)
        {
            MessageBasedSession mbSession;
            var rmSession = new ResourceManager();
            mbSession = (MessageBasedSession)rmSession.Open("TCPIP0::127.0.0.1::inst0::INSTR");

            // Read out all errors first.
            mbSession.RawIO.Write(":SYST:ERR?\n");
            string[] temp1 = mbSession.RawIO.ReadString().Split(',');
            while (Convert.ToInt32(temp1[0]) != 0)
            {
                mbSession.RawIO.Write(":SYST:ERR?\n");
                temp1 = mbSession.RawIO.ReadString().Split(',');
            }

            mbSession.RawIO.Write("*IDN?\n");
            string temp2 = mbSession.RawIO.ReadString();
            Console.WriteLine("{0}", temp2);

            // Place the VNA in the system default state
            mbSession.RawIO.Write(":SYST:PRES\n");
            // Set the center frequency for the device
            mbSession.RawIO.Write(":SENS1:FREQ:CENT 433000000.0\n");
            // Set the span around the center frequency
            mbSession.RawIO.Write(":SENS1:FREQ:SPAN 20000000.0\n");
            // Set the number of measurement points
            mbSession.RawIO.Write(":SENS1:SWE:POIN 1001\n");
            // Set the manual cal kit option to use; in this case the Bird SOL device
            mbSession.RawIO.Write(":SENS1:CORR:COLL:CKIT 1\n");
            // Disable the measurement corrections/cal
            mbSession.RawIO.Write(":SENS1:CORR:STAT 0\n");
            // Define the system or characteristic impedance
            mbSession.RawIO.Write(":SENS1:CORR:IMP 50.0\n");
            // Define the type of calibration to be performed, full 1-port
            mbSession.RawIO.Write(":SENS1:CORR:COLL:METH:SOLT1 1\n");
            // After the user connects the open device, capture a measurement and wait for the operation to complete
            mbSession.RawIO.Write(":SENS1:CORR:COLL:OPEN 1\n");
            mbSession.RawIO.Write("*OPC?\n");
            temp2 = mbSession.RawIO.ReadString();
            // After the user connects the short device, capture a measurement and wait for the operation to complete
            mbSession.RawIO.Write(":SENS1:CORR:COLL:SHOR 1\n");
            mbSession.RawIO.Write("*OPC?\n");
            temp2 = mbSession.RawIO.ReadString();
            // After the user connects the load device, capture a measurement and wait for the operation to complete
            mbSession.RawIO.Write(":SENS1:CORR:COLL:LOAD 1\n");
            mbSession.RawIO.Write("*OPC?\n");
            temp2 = mbSession.RawIO.ReadString();
            // Save the calibration data then enable the measurement corrections/cal
            mbSession.RawIO.Write(":SENS1:CORR:COLL:SAVE\n");
            mbSession.RawIO.Write(":SENS1:CORR:STAT 1\n");
           
            mbSession.Dispose();
        }
    }
}

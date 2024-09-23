/*
 * 
 Example Description:
        This example shows how to use remote commands to perform a two port
        calibration on the vector network analyzer using the ECal (electronic
        calibration) module. You will note that in comparison to the manual 
        2-port calibration, the coding is simpler which aligns with the 
        simplicity and limited connections to the ECal standard/module.

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

@file ex05_two_port_calibration_using_ecal_module.cs
 
 * 
 */

using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Threading;
using NationalInstruments.Visa;

namespace ex05_two_port_calibration_using_ecal_module
{
    internal class ex05_two_port_calibration_using_ecal_module
    {
        static void Main(string[] args)
        {
            var rmSession = new ResourceManager();
            MessageBasedSession mbSession = (MessageBasedSession)rmSession.Open("TCPIP0::127.0.0.1::inst0::INSTR");

            // Read out any/all errors first.
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

            // Configure for S11, log magnitude format, then auto scale
            mbSession.RawIO.Write(":CALC1:PAR:COUN 1\n");
            mbSession.RawIO.Write(":CALC1:PAR1:SEL\n");
            mbSession.RawIO.Write(":CALC1:PAR1:DEF S11\n");
            mbSession.RawIO.Write(":CALC1:TRAC1:FORM MLOG\n");
            mbSession.RawIO.Write(":DISP:WIND1:TRAC1:Y:AUTO\n");

            // Ensure all setup is complete
            mbSession.RawIO.Write("*OPC?\n");
            temp2 = mbSession.RawIO.ReadString();

            // Trigger a measurement sweep. Again, another key command to inform the triggered operation. 
            mbSession.RawIO.Write(":SENS1:CORR:COLL:ECAL:SOLT2 1,2\n");

            // Ensure calibration is complete. A sleep timer is added to the operation complete
            // command since the default command timeout is 10 s and the duration of the calibration
            // will depend on the number of ports and other measurement settings. 
            Thread.Sleep(5000); // 5 s delay
            mbSession.RawIO.Write("*OPC?\n");
            temp2 = mbSession.RawIO.ReadString();

            mbSession.Dispose();
        }
    }
}

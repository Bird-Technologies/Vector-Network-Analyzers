/*
 * 
 Example Description:
        This example shows how to use remote commands to perform configure the
        VNA for a triggered sweep of return loss (S11). Measurements are then
        acquired from marker points and returned to the user.

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

@file ex04_triggered_return_loss_sweep.cs
 
 * 
 */

using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using NationalInstruments.Visa;

namespace ex04_triggered_return_loss_sweep
{
    internal class ex04_triggered_return_loss_sweep
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

            // Configure for bus triggering. NOTE this is one of the key configuration modifications for this setup. 
            mbSession.RawIO.Write(":TRIG:SOUR BUS\n");

            // Set the start frequency for the device
            mbSession.RawIO.Write("SENS1:FREQ:STAR 800000000.0\n");
            // Set the stop frequency for the device
            mbSession.RawIO.Write("SENS1:FREQ:STOP 925000000.0\n");
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
            mbSession.RawIO.Write(":TRIG\n");

            // Ensure sweep is complete
            mbSession.RawIO.Write("*OPC?\n");
            temp2 = mbSession.RawIO.ReadString();

            // Autoscale again for best fit
            mbSession.RawIO.Write(":DISP:WIND1:TRAC1:Y:AUTO\n");

            // Do a check to see if marker 1 is visible then enable it; set it to the center frqeuncy, then grab the marker measurement data
            mbSession.RawIO.Write(":CALC1:MARK1?\n");
            temp2 = mbSession.RawIO.ReadString();
            mbSession.RawIO.Write(":CALC1:MARK1 1\n");
            mbSession.RawIO.Write(":CALC1:MARK1:SET CENT\n");
            mbSession.RawIO.Write(":CALC1:MARK1:Y?\n");
            temp2 = mbSession.RawIO.ReadString();

            // Enable marker 2 then move it to approximatel the lower end cutoff frequency then acquire the marker measurement data
            mbSession.RawIO.Write(":CALC1:MARK2 1\n");
            mbSession.RawIO.Write(":CALC1:MARK2:X 824000000.0\n");
            mbSession.RawIO.Write(":CALC1:MARK2:Y?\n");
            temp2 = mbSession.RawIO.ReadString();

            // Enable marker 3 then move it to approximatel the upper end cutoff frequency then acquire the marker measurement data
            mbSession.RawIO.Write(":CALC1:MARK3 1\n");
            mbSession.RawIO.Write(":CALC1:MARK3:X 824000000.0\n");
            mbSession.RawIO.Write(":CALC1:MARK3:Y?\n");
            temp2 = mbSession.RawIO.ReadString();

            mbSession.Dispose();
        }
    }
}

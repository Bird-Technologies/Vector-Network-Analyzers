/*
 * 
 Example Description:
        This example shows how to use remote commands to perform the bandpass
        filter characterization steps that are covered in the associated
        application note featured on the VNA landing pages on birdrf.com. This
        includes defining the frequency range of interest; measuring return
        loss, VSWR, and insertion loss at select points using markers; enabling
        the limit test for the return loss trace defining the test region and
        making limit lines and pass/fail indicators visible in the software UI
        as well as reporting the pass/fail status over the instrument bus.
        Marker search is also used.

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

@file ex06_limit_test_on_return_loss_sweep_of_bandpass_filter.cs
 
 * 
 */

using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Threading;
using NationalInstruments.Visa;

namespace ex06_limit_test_on_return_loss_sweep_of_bandpass_filter
{
    internal class ex06_limit_test_on_return_loss_sweep_of_bandpass_filter
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
            string temp2 = mbSession.RawIO.ReadString();

            // Do a check to see if marker 1 is visible then enable it; set it to the center frqeuncy, then grab the marker measurement data
            mbSession.RawIO.Write(":CALC1:MARK1?\n");
            temp2 = mbSession.RawIO.ReadString();
            mbSession.RawIO.Write(":CALC1:MARK1 1\n");
            mbSession.RawIO.Write(":CALC1:MARK1:SET CENT\n");
            mbSession.RawIO.Write(":CALC1:MARK1:Y?\n");
            temp2 = mbSession.RawIO.ReadString();

            // Enable marker 2 then move it to approximatel the lower end then perform a marker search to the loss level of interest
            mbSession.RawIO.Write(":CALC1:MARK2 1\n");
            mbSession.RawIO.Write(":CALC1:MARK2:X 423000000.0\n");
            mbSession.RawIO.Write(":CALC1:MARK2:FUNC:TYPE TARG\n");
            mbSession.RawIO.Write(":CALC1:MARK2:FUNC:TARG -16.5\n");
            mbSession.RawIO.Write(":CALC1:MARK2:FUNC:EXEC\n");

            // Find out what frequency the marker searched to then get the data at that point. 
            mbSession.RawIO.Write(":CALC1:MARK2:X?\n");
            temp2 = mbSession.RawIO.ReadString();
            mbSession.RawIO.Write(":CALC1:MARK2:Y?\n");
            temp2 = mbSession.RawIO.ReadString();

            // Enable marker 3 then move it to approximatel the upper end then perform a marker seach to the loss level of interest
            mbSession.RawIO.Write(":CALC1:MARK3 1\n");
            mbSession.RawIO.Write(":CALC1:MARK3:X 443000000.0\n");
            mbSession.RawIO.Write(":CALC1:MARK3:FUNC:TYPE TARG\n");
            mbSession.RawIO.Write(":CALC1:MARK3:FUNC:TARG -16.5\n");
            mbSession.RawIO.Write(":CALC1:MARK3:FUNC:EXEC\n");

            // Find out what frequency the marker searched to then get the data at that point. 
            mbSession.RawIO.Write(":CALC1:MARK3:X?\n");
            temp2 = mbSession.RawIO.ReadString();
            mbSession.RawIO.Write(":CALC1:MARK3:Y?\n");
            temp2 = mbSession.RawIO.ReadString();

            // Clear then create an entry in the limit test table
            mbSession.RawIO.Write(":CALC1:LIM:DATA 0\n");
            mbSession.RawIO.Write(":CALC1:LIM:DATA 1,1,428000000.0,438000000.0,-17.0,-17.0\n");

            // Turn on the limit test, turn on the limit line, then the large fail sign, finally reading back the limit test state
            mbSession.RawIO.Write(":CALC1:LIM 1\n");
            mbSession.RawIO.Write(":CALC1:LIM:DISP 1\n");
            mbSession.RawIO.Write(":DISP:FSIG 1\n");
            mbSession.RawIO.Write(":CALC1:LIM:FAIL?\n");
            temp2 = mbSession.RawIO.ReadString();


            // Enable a second trace and make it the trace of focus; set for S11 and VSWR format; autoscale then take a measurement data from each of the three markers
            mbSession.RawIO.Write(":CALC1:PAR:COUN 2\n");
            mbSession.RawIO.Write(":CALC1:PAR2:SEL\n");
            mbSession.RawIO.Write(":CALC1:PAR2:DEF S11\n");
            mbSession.RawIO.Write(":CALC1:TRAC2:FORM SWR\n");
            mbSession.RawIO.Write(":DISP:WIND1:TRAC2:Y:AUTO\n");
            mbSession.RawIO.Write(":CALC1:MARK1:Y?\n");
            temp2 = mbSession.RawIO.ReadString();
            mbSession.RawIO.Write(":CALC1:MARK2:Y?\n");
            temp2 = mbSession.RawIO.ReadString();
            mbSession.RawIO.Write(":CALC1:MARK3:Y?\n");
            temp2 = mbSession.RawIO.ReadString();

            // Enable a third trace and make it the one of focus
            mbSession.RawIO.Write(":CALC1:PAR:COUN 3\n");
            mbSession.RawIO.Write(":CALC1:PAR3:SEL\n");
            // Change the trace allocation to three separate stacked, but then maximize the one holding trace 3
            mbSession.RawIO.Write(":DISP:WIND1:SPL D123\n");
            mbSession.RawIO.Write(":DISP:WIND1:MAX 1\n");

            mbSession.RawIO.Write(":CALC1:PAR3:DEF S21\n");
            mbSession.RawIO.Write(":CALC1:TRAC3:FORM MLOG\n");
            mbSession.RawIO.Write(":DISP:WIND1:TRAC3:Y:AUTO\n");
            mbSession.RawIO.Write(":CALC1:MARK1:Y?\n");
            temp2 = mbSession.RawIO.ReadString();
            mbSession.RawIO.Write(":CALC1:MARK2:Y?\n");
            temp2 = mbSession.RawIO.ReadString();
            mbSession.RawIO.Write(":CALC1:MARK3:Y?\n");
            temp2 = mbSession.RawIO.ReadString();

            mbSession.Dispose();
            rmSession.Dispose();
        }
    }
}

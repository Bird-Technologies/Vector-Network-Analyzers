/*
 * 
 Example Description:
        This example shows how to use remote commands to perform save and recall 
        of user setups. The state type is first specifed, helping to point out 
        to the user that calibration and data items can be preserved along with 
        the instrument setup. The setup is saved to file. A preset is then called 
        to return to system defaults, eliminating all prior configurations. Then 
        the state is recalled.

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

@file ex08_save_and_recall_setups.cs
 
 * 
 */

using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using NationalInstruments.Visa;

namespace ex08_save_and_recall_setups
{
    internal class ex08_save_and_recall_setups
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
            mbSession.RawIO.Write(":SENS1:SWE:POIN 1601\n");

            // Configure for S11, log magnitude format, then auto scale
            mbSession.RawIO.Write(":CALC1:PAR:COUN 1\n");
            mbSession.RawIO.Write(":CALC1:PAR1:SEL\n");
            mbSession.RawIO.Write(":CALC1:PAR1:DEF S21\n");
            mbSession.RawIO.Write(":CALC1:TRAC1:FORM MLOG\n");
            mbSession.RawIO.Write(":DISP:WIND1:TRAC1:Y:AUTO\n");

            // Ensure all setup is complete
            mbSession.RawIO.Write("*OPC?\n");
            string temp2 = mbSession.RawIO.ReadString();

            // Maximize the trace window
            mbSession.RawIO.Write(":DISP:WIND1:MAX 1\n");

            // Do a check to see if marker 1 is visible then enable it; set it to the center frqeuncy, then grab the marker measurement data
            mbSession.RawIO.Write(":CALC1:MARK1?\n");
            temp2 = mbSession.RawIO.ReadString();
            mbSession.RawIO.Write(":CALC1:MARK1 1\n");
            mbSession.RawIO.Write(":CALC1:MARK1:SET CENT\n");
            mbSession.RawIO.Write(":CALC1:MARK1:Y?\n");
            temp2 = mbSession.RawIO.ReadString();

            // Enable marker 2 then move it to approximatel the lower end then perform a marker search to the loss level of interest
            mbSession.RawIO.Write(":CALC1:MARK2 1\n");
            mbSession.RawIO.Write(":CALC1:MARK2:X 428000000.0\n");

            // Find out what frequency the marker searched to then get the data at that point. 
            mbSession.RawIO.Write(":CALC1:MARK2:X?\n");
            temp2 = mbSession.RawIO.ReadString();
            mbSession.RawIO.Write(":CALC1:MARK2:Y?\n");
            temp2 = mbSession.RawIO.ReadString();

            // Enable marker 3 then move it to approximatel the upper end then perform a marker seach to the loss level of interest
            mbSession.RawIO.Write(":CALC1:MARK3 1\n");
            mbSession.RawIO.Write(":CALC1:MARK3:X 438000000.0\n");

            // Find out what frequency the marker searched to then get the data at that point. 
            mbSession.RawIO.Write(":CALC1:MARK3:X?\n");
            temp2 = mbSession.RawIO.ReadString();
            mbSession.RawIO.Write(":CALC1:MARK3:Y?\n");
            temp2 = mbSession.RawIO.ReadString();

            // Specify that calibration and information state data are to be saved
            // 
            mbSession.RawIO.Write(":MMEM:STOR:STYP CST\n");

            // Then execute the save operation with the file name specified
            mbSession.RawIO.Write(":MMEM:STOR mystate.sta\n");

            // Use the preset command to wipe out the previously configured setup and calibration
            mbSession.RawIO.Write(":SYST:PRES\n");

            // Then execute the load operation to recall and restore from file
            mbSession.RawIO.Write(":MMEM:LOAD mystate.sta\n");

            mbSession.Dispose();
            rmSession.Dispose();
        }
    }
}

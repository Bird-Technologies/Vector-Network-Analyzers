using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using NationalInstruments.Visa;

namespace ex02_two_port_calibration
{
    internal class ex02_two_port_calibration
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
            mbSession.RawIO.Write("SENS1:CORR:COLL:METH:SOLT2 1,2\n");
            
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

            // After the user connects the open device, capture a measurement and wait for the operation to complete
            mbSession.RawIO.Write(":SENS1:CORR:COLL:OPEN 2\n");
            mbSession.RawIO.Write("*OPC?\n");
            temp2 = mbSession.RawIO.ReadString();
            // After the user connects the short device, capture a measurement and wait for the operation to complete
            mbSession.RawIO.Write(":SENS1:CORR:COLL:SHOR 2\n");
            mbSession.RawIO.Write("*OPC?\n");
            temp2 = mbSession.RawIO.ReadString();
            // After the user connects the load device, capture a measurement and wait for the operation to complete
            mbSession.RawIO.Write(":SENS1:CORR:COLL:LOAD 2\n");
            mbSession.RawIO.Write("*OPC?\n");
            temp2 = mbSession.RawIO.ReadString();

            // After the user connects the thru device, capture a measurements (in both directions) and wait for the operation to complete
            mbSession.RawIO.Write(":SENS1:CORR:COLL:THRU 1,2\n");
            mbSession.RawIO.Write("*OPC?\n");
            temp2 = mbSession.RawIO.ReadString();
            mbSession.RawIO.Write(":SENS1:CORR:COLL:THRU 2,1\n");
            mbSession.RawIO.Write("*OPC?\n");
            temp2 = mbSession.RawIO.ReadString();

            // Save the calibration data then enable the measurement corrections/cal
            mbSession.RawIO.Write(":SENS1:CORR:COLL:SAVE\n");
            mbSession.RawIO.Write(":SENS1:CORR:STAT 1\n");

            mbSession.Dispose();
        }
    }
}

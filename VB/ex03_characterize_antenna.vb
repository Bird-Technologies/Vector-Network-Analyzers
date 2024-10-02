' Example Description:
'        This example shows how a user can measure return loss, VSWR, and impedance
'        values(via Smith Chart) To aid In characterizing an antenna. It Is expected
'        that the Operator will have already performed at least a Single port (SOL)
'        measurement calibration, but the code also shows how port extensions might
'        be used To account For connectors added after the cal. For more information
'        on antenna characterization, see the application note featured on the Vector
'        Network Analyzers landing page at birdrf.com that covers this topic.
'
' @verbatim
'
' The MIT License (MIT)
'
' Copyright(c) 2024 Bird
'
' Permission Is hereby granted, free Of charge, to any person obtaining a copy of
' this software And associated documentation files (the "Software"), To deal In
' the Software without restriction, including without limitation the rights To
' use, copy, modify, merge, publish, distribute, sublicense, And/Or sell copies
' of the Software, And to permit persons to whom the Software Is furnished to do
' so, subject to the following conditions:

' The above copyright notice And this permission notice shall be included In all
' copies Or substantial portions of the Software.

' THE SOFTWARE Is PROVIDED "AS IS", WITHOUT WARRANTY Of ANY KIND, EXPRESS Or
' IMPLIED, INCLUDING BUT Not LIMITED To THE WARRANTIES Of MERCHANTABILITY,
' FITNESS FOR A PARTICULAR PURPOSE And NONINFRINGEMENT. IN NO EVENT SHALL THE
' AUTHORS Or COPYRIGHT HOLDERS BE LIABLE For ANY CLAIM, DAMAGES Or OTHER
' LIABILITY, WHETHER In AN ACTION Of CONTRACT, TORT Or OTHERWISE, ARISING FROM,
' OUT OF Or IN CONNECTION WITH THE SOFTWARE Or THE USE Or OTHER DEALINGS IN THE
' SOFTWARE.
'
' @endverbatim

' @file ex03_characterize_antenna.vb

Imports System
Imports NationalInstruments.Visa

Module ex03_characterize_antenna

    Sub Main()
        ' Initialize the resource manager and open a VISA session
        Dim rmSession As New ResourceManager()
        Dim mbSession As MessageBasedSession = CType(rmSession.Open("TCPIP0::127.0.0.1::inst0::INSTR"), MessageBasedSession)

        ' Read out all errors first.
        mbSession.RawIO.Write(":SYST:ERR?\n")
        Dim temp1() As String = mbSession.RawIO.ReadString().Split(",")

        While Convert.ToInt32(temp1(1)) = 0
            mbSession.RawIO.Write(":SYST:ERR?\n")
            temp1 = mbSession.RawIO.ReadString().Split(",")
        End While

        mbSession.RawIO.Write("*IDN?\n")
        Dim temp2 As String = mbSession.RawIO.ReadString()
        Console.WriteLine("{0}", temp2)

        ' Place the VNA in the system default state
        mbSession.RawIO.Write(":SYST:PRES\n")
        ' Set the start frequency for the device
        mbSession.RawIO.Write("SENS1:FREQ:STAR 800000000.0\n")
        ' Set the stop frequency for the device
        mbSession.RawIO.Write("SENS1:FREQ:STOP 925000000.0\n")
        ' Set the number of measurement points
        mbSession.RawIO.Write(":SENS1:SWE:POIN 1001\n")

        ' Focus only on applying port extentions to port 1 where the device will be tested
        mbSession.RawIO.Write(":SENS1:CORR:EXT:AUTO:PORT2 OFF\n")
        mbSession.RawIO.Write(":SENS1:CORR:EXT:AUTO:PORT1 ON\n")

        ' Perform an extensions measurement with the adapter/connector in place
        mbSession.RawIO.Write(":SENS1:CORR:EXT:AUTO:MEAS OPEN\n")

        ' Configure for S11, log magnitude format, then auto scale
        mbSession.RawIO.Write(":CALC1:PAR:COUN 1\n")
        mbSession.RawIO.Write(":CALC1:PAR1:SEL\n")
        mbSession.RawIO.Write(":CALC1:PAR1:DEF S11\n")
        mbSession.RawIO.Write(":CALC1:TRAC1:FORM MLOG\n")
        mbSession.RawIO.Write(":DISP:WIND1:TRAC1:Y:AUTO\n")

        ' Do a check to see if marker 1 Is visible then enable it  set it to the center frqeuncy, then grab the marker measurement data
        mbSession.RawIO.Write(":CALC1:MARK1?\n")
        temp2 = mbSession.RawIO.ReadString()
        mbSession.RawIO.Write(":CALC1:MARK1 1\n")
        mbSession.RawIO.Write(":CALC1:MARK1:SET CENT\n")
        mbSession.RawIO.Write(":CALC1:MARK1:Y?\n")
        temp2 = mbSession.RawIO.ReadString()

        ' Enable marker 2 then move it to approximatel the lower end cutoff frequency then acquire the marker measurement data
        mbSession.RawIO.Write(":CALC1:MARK2 1\n")
        mbSession.RawIO.Write(":CALC1:MARK2:X 824000000.0\n")
        mbSession.RawIO.Write(":CALC1:MARK2:Y?\n")
        temp2 = mbSession.RawIO.ReadString()

        ' Enable marker 3 then move it to approximatel the upper end cutoff frequency then acquire the marker measurement data
        mbSession.RawIO.Write(":CALC1:MARK3 1\n")
        mbSession.RawIO.Write(":CALC1:MARK3:X 824000000.0\n")
        mbSession.RawIO.Write(":CALC1:MARK3:Y?\n")
        temp2 = mbSession.RawIO.ReadString()

        ' Enable a second trace And make it the trace of focus  set for S11 And VSWR format  autoscale then take a measurement data from each of the three markers
        mbSession.RawIO.Write(":CALC1:PAR:COUN 2\n")
        mbSession.RawIO.Write(":CALC1:PAR2:SEL\n")
        mbSession.RawIO.Write(":CALC1:PAR2:DEF S11\n")
        mbSession.RawIO.Write(":CALC1:TRAC2:FORM SWR\n")
        mbSession.RawIO.Write(":DISP:WIND1:TRAC2:Y:AUTO\n")
        mbSession.RawIO.Write(":CALC1:MARK1:Y?\n")
        temp2 = mbSession.RawIO.ReadString()
        mbSession.RawIO.Write(":CALC1:MARK2:Y?\n")
        temp2 = mbSession.RawIO.ReadString()
        mbSession.RawIO.Write(":CALC1:MARK3:Y?\n")
        temp2 = mbSession.RawIO.ReadString()

        ' Enable a third trace And make it the one of focus
        mbSession.RawIO.Write(":CALC1:PAR:COUN 3\n")
        mbSession.RawIO.Write(":CALC1:PAR3:SEL\n")
        ' Change the trace allocation to three separate stacked, but then maximize the one holding trace 3
        mbSession.RawIO.Write(":DISP:WIND1:SPL D123\n")
        mbSession.RawIO.Write(":DISP:WIND1:MAX 1\n")

        mbSession.RawIO.Write(":CALC1:PAR3:DEF S11\n")
        mbSession.RawIO.Write(":CALC1:TRAC3:FORM SMIT\n")
        mbSession.RawIO.Write(":DISP:WIND1:TRAC3:Y:AUTO\n")
        mbSession.RawIO.Write(":CALC1:MARK1:Y?\n")
        temp2 = mbSession.RawIO.ReadString()
        mbSession.RawIO.Write(":CALC1:MARK2:Y?\n")
        temp2 = mbSession.RawIO.ReadString()
        mbSession.RawIO.Write(":CALC1:MARK3:Y?\n")
        temp2 = mbSession.RawIO.ReadString()

        mbSession.Dispose()
    End Sub

End Module

' Example Description:
'        This example shows how to use remote commands to perform configure the
'        VNA for a triggered sweep of return loss (S11). Measurements are then
'        acquired from marker points And returned To the user.
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

' @file ex04_triggered_return_loss_sweep.vb

Imports System
Imports NationalInstruments.Visa

Module ex04_triggered_return_loss_sweep

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

        ' Configure for bus triggering. NOTE this Is one of the key configuration modifications for this setup. 
        mbSession.RawIO.Write(":TRIG:SOUR BUS\n")

        ' Set the start frequency for the device
        mbSession.RawIO.Write("SENS1:FREQ:STAR 800000000.0\n")
        ' Set the stop frequency for the device
        mbSession.RawIO.Write("SENS1:FREQ:STOP 925000000.0\n")
        ' Set the number of measurement points
        mbSession.RawIO.Write(":SENS1:SWE:POIN 1001\n")

        ' Configure for S11, log magnitude format, then auto scale
        mbSession.RawIO.Write(":CALC1:PAR:COUN 1\n")
        mbSession.RawIO.Write(":CALC1:PAR1:SEL\n")
        mbSession.RawIO.Write(":CALC1:PAR1:DEF S11\n")
        mbSession.RawIO.Write(":CALC1:TRAC1:FORM MLOG\n")
        mbSession.RawIO.Write(":DISP:WIND1:TRAC1:Y:AUTO\n")

        ' Ensure all setup Is complete
        mbSession.RawIO.Write("*OPC?\n")
        temp2 = mbSession.RawIO.ReadString()

        ' Trigger a measurement sweep. Again, another key command to inform the triggered operation. 
        mbSession.RawIO.Write(":TRIG\n")

        ' Ensure sweep Is complete
        mbSession.RawIO.Write("*OPC?\n")
        temp2 = mbSession.RawIO.ReadString()

        ' Autoscale again for best fit
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

        mbSession.Dispose()
    End Sub

End Module

' Example Description:
'        This example shows how to use remote commands to perform a two port
'        calibration on the vector network analyzer using the ECal (electronic
'        calibration) module. You will note that in comparison to the manual 
'        2-port calibration, the coding Is simpler which aligns with the 
'        simplicity And limited connections to the ECal standard/module.
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

' @file ex05_two_port_calibration_using_ecal_module.vb

Imports System
Imports System.Threading
Imports NationalInstruments.Visa


Module ex05_two_port_calibration_using_ecal_module

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

        ' Set the center frequency for the device
        mbSession.RawIO.Write(":SENS1:FREQ:CENT 433000000.0\n")
        ' Set the span around the center frequency
        mbSession.RawIO.Write(":SENS1:FREQ:SPAN 20000000.0\n")
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
        mbSession.RawIO.Write(":SENS1:CORR:COLL:ECAL:SOLT2 1,2\n")

        ' Ensure calibration Is complete. A sleep timer Is added to the operation complete
        ' command since the default command timeout Is 10 s And the duration of the calibration
        ' will depend on the number of ports And other measurement settings. 
        Thread.Sleep(5000)  ' 5 s delay
        mbSession.RawIO.Write("*OPC?\n")
        temp2 = mbSession.RawIO.ReadString()

        mbSession.Dispose()
    End Sub

End Module

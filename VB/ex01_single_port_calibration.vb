' Example Description:
'        This example shows how To use remote commands To perform a Single
'        port calibration On the vector network analyzer.
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

' @file ex01_single_port_calibration.vb
Imports System
Imports NationalInstruments.Visa
Module ex01_single_port_calibration

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
        ' Set the manual cal kit option to use  in this case the Bird SOL device
        mbSession.RawIO.Write(":SENS1:CORR:COLL:CKIT 1\n")
        ' Disable the measurement corrections/cal
        mbSession.RawIO.Write(":SENS1:CORR:STAT 0\n")
        ' Define the system Or characteristic impedance
        mbSession.RawIO.Write(":SENS1:CORR:IMP 50.0\n")
        ' Define the type of calibration to be performed, full 1-port
        mbSession.RawIO.Write(":SENS1:CORR:COLL:METH:SOLT1 1\n")
        ' After the user connects the open device, capture a measurement And wait for the operation to complete
        mbSession.RawIO.Write(":SENS1:CORR:COLL:OPEN 1\n")
        mbSession.RawIO.Write("*OPC?\n")
        temp2 = mbSession.RawIO.ReadString()
        ' After the user connects the short device, capture a measurement And wait for the operation to complete
        mbSession.RawIO.Write(":SENS1:CORR:COLL:SHOR 1\n")
        mbSession.RawIO.Write("*OPC?\n")
        temp2 = mbSession.RawIO.ReadString()
        ' After the user connects the load device, capture a measurement And wait for the operation to complete
        mbSession.RawIO.Write(":SENS1:CORR:COLL:LOAD 1\n")
        mbSession.RawIO.Write("*OPC?\n")
        temp2 = mbSession.RawIO.ReadString()
        ' Save the calibration data then enable the measurement corrections/cal
        mbSession.RawIO.Write(":SENS1:CORR:COLL:SAVE\n")
        mbSession.RawIO.Write(":SENS1:CORR:STAT 1\n")

        mbSession.Dispose()

    End Sub

End Module


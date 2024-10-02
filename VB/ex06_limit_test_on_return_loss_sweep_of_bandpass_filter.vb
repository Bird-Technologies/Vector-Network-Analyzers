' Example Description:
'        This example shows how to use remote commands to perform the bandpass
'        filter characterization steps that are covered In the associated
'        application note featured On the VNA landing pages On birdrf.com. This
'        includes defining the frequency range Of interest  measuring Return
'        loss, VSWR, And insertion loss at select points using markers  enabling
'        the limit test For the Return loss trace defining the test region And
'        making limit lines And pass/fail indicators visible In the software UI
'        as well as reporting the pass/fail status over the instrument bus.
'        Marker search Is also used.
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

' @file ex06_limit_test_on_return_loss_sweep_of_bandpass_filter.vb

Imports System
Imports System.Threading
Imports NationalInstruments.Visa

Module ex06_limit_test_on_return_loss_sweep_of_bandpass_filter

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

        ' Do a check to see if marker 1 Is visible then enable it  set it to the center frqeuncy, then grab the marker measurement data
        mbSession.RawIO.Write(":CALC1:MARK1?\n")
        temp2 = mbSession.RawIO.ReadString()
        mbSession.RawIO.Write(":CALC1:MARK1 1\n")
        mbSession.RawIO.Write(":CALC1:MARK1:SET CENT\n")
        mbSession.RawIO.Write(":CALC1:MARK1:Y?\n")
        temp2 = mbSession.RawIO.ReadString()

        ' Enable marker 2 then move it to approximatel the lower end then perform a marker search to the loss level of interest
        mbSession.RawIO.Write(":CALC1:MARK2 1\n")
        mbSession.RawIO.Write(":CALC1:MARK2:X 423000000.0\n")
        mbSession.RawIO.Write(":CALC1:MARK2:FUNC:TYPE TARG\n")
        mbSession.RawIO.Write(":CALC1:MARK2:FUNC:TARG -16.5\n")
        mbSession.RawIO.Write(":CALC1:MARK2:FUNC:EXEC\n")

        ' Find out what frequency the marker searched to then get the data at that point. 
        mbSession.RawIO.Write(":CALC1:MARK2:X?\n")
        temp2 = mbSession.RawIO.ReadString()
        mbSession.RawIO.Write(":CALC1:MARK2:Y?\n")
        temp2 = mbSession.RawIO.ReadString()

        ' Enable marker 3 then move it to approximatel the upper end then perform a marker seach to the loss level of interest
        mbSession.RawIO.Write(":CALC1:MARK3 1\n")
        mbSession.RawIO.Write(":CALC1:MARK3:X 443000000.0\n")
        mbSession.RawIO.Write(":CALC1:MARK3:FUNC:TYPE TARG\n")
        mbSession.RawIO.Write(":CALC1:MARK3:FUNC:TARG -16.5\n")
        mbSession.RawIO.Write(":CALC1:MARK3:FUNC:EXEC\n")

        ' Find out what frequency the marker searched to then get the data at that point. 
        mbSession.RawIO.Write(":CALC1:MARK3:X?\n")
        temp2 = mbSession.RawIO.ReadString()
        mbSession.RawIO.Write(":CALC1:MARK3:Y?\n")
        temp2 = mbSession.RawIO.ReadString()

        ' Clear then create an entry in the limit test table
        mbSession.RawIO.Write(":CALC1:LIM:DATA 0\n")
        mbSession.RawIO.Write(":CALC1:LIM:DATA 1,1,428000000.0,438000000.0,-17.0,-17.0\n")

        ' Turn on the limit test, turn on the limit line, then the large fail sign, finally reading back the limit test state
        mbSession.RawIO.Write(":CALC1:LIM 1\n")
        mbSession.RawIO.Write(":CALC1:LIM:DISP 1\n")
        mbSession.RawIO.Write(":DISP:FSIG 1\n")
        mbSession.RawIO.Write(":CALC1:LIM:FAIL?\n")
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

        mbSession.RawIO.Write(":CALC1:PAR3:DEF S21\n")
        mbSession.RawIO.Write(":CALC1:TRAC3:FORM MLOG\n")
        mbSession.RawIO.Write(":DISP:WIND1:TRAC3:Y:AUTO\n")
        mbSession.RawIO.Write(":CALC1:MARK1:Y?\n")
        temp2 = mbSession.RawIO.ReadString()
        mbSession.RawIO.Write(":CALC1:MARK2:Y?\n")
        temp2 = mbSession.RawIO.ReadString()
        mbSession.RawIO.Write(":CALC1:MARK3:Y?\n")
        temp2 = mbSession.RawIO.ReadString()

        mbSession.Dispose()
        rmSession.Dispose()
    End Sub

End Module

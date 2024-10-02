' Example Description:
'        This example shows how to use remote commands to perform save and recall 
'        of user setups. The state type Is first specifed, helping to point out 
'        to the user that calibration And data items can be preserved along with 
'        the instrument setup. The setup Is saved To file. A preset Is Then called 
'        to return to system defaults, eliminating all prior configurations. Then 
'        the state Is recalled.
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

' @file ex08_save_and_recall_setups.vb

Imports System.Threading
Imports NationalInstruments.Visa

Module ex08_save_and_recall_setups

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
        mbSession.RawIO.Write(":SENS1:SWE:POIN 1601\n")

        ' Configure for S11, log magnitude format, then auto scale
        mbSession.RawIO.Write(":CALC1:PAR:COUN 1\n")
        mbSession.RawIO.Write(":CALC1:PAR1:SEL\n")
        mbSession.RawIO.Write(":CALC1:PAR1:DEF S21\n")
        mbSession.RawIO.Write(":CALC1:TRAC1:FORM MLOG\n")
        mbSession.RawIO.Write(":DISP:WIND1:TRAC1:Y:AUTO\n")

        ' Ensure all setup Is complete
        mbSession.RawIO.Write("*OPC?\n")
        temp2 = mbSession.RawIO.ReadString()

        ' Maximize the trace window
        mbSession.RawIO.Write(":DISP:WIND1:MAX 1\n")

        ' Do a check to see if marker 1 Is visible then enable it  set it to the center frqeuncy, then grab the marker measurement data
        mbSession.RawIO.Write(":CALC1:MARK1?\n")
        temp2 = mbSession.RawIO.ReadString()
        mbSession.RawIO.Write(":CALC1:MARK1 1\n")
        mbSession.RawIO.Write(":CALC1:MARK1:SET CENT\n")
        mbSession.RawIO.Write(":CALC1:MARK1:Y?\n")
        temp2 = mbSession.RawIO.ReadString()

        ' Enable marker 2 then move it to approximatel the lower end then perform a marker search to the loss level of interest
        mbSession.RawIO.Write(":CALC1:MARK2 1\n")
        mbSession.RawIO.Write(":CALC1:MARK2:X 428000000.0\n")

        ' Find out what frequency the marker searched to then get the data at that point. 
        mbSession.RawIO.Write(":CALC1:MARK2:X?\n")
        temp2 = mbSession.RawIO.ReadString()
        mbSession.RawIO.Write(":CALC1:MARK2:Y?\n")
        temp2 = mbSession.RawIO.ReadString()

        ' Enable marker 3 then move it to approximatel the upper end then perform a marker seach to the loss level of interest
        mbSession.RawIO.Write(":CALC1:MARK3 1\n")
        mbSession.RawIO.Write(":CALC1:MARK3:X 438000000.0\n")

        ' Find out what frequency the marker searched to then get the data at that point. 
        mbSession.RawIO.Write(":CALC1:MARK3:X?\n")
        temp2 = mbSession.RawIO.ReadString()
        mbSession.RawIO.Write(":CALC1:MARK3:Y?\n")
        temp2 = mbSession.RawIO.ReadString()

        ' Specify that calibration And information state data are to be saved
        ' 
        mbSession.RawIO.Write(":MMEM:STOR:STYP CST\n")

        ' Then execute the save operation with the file name specified
        mbSession.RawIO.Write(":MMEM:STOR mystate.sta\n")

        ' Use the preset command to wipe out the previously configured setup And calibration
        mbSession.RawIO.Write(":SYST:PRES\n")

        ' Then execute the load operation to recall And restore from file
        mbSession.RawIO.Write(":MMEM:LOAD mystate.sta\n")

        mbSession.Dispose()
        rmSession.Dispose()
    End Sub

End Module

"""
Example Description:
        This class code presents a Python driver foundation which can be
        used with the Bird family of vector network analyzer instruments.

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

@file bird_vector_network_analyzer.py
 
"""
import pyvisa as visa


class BirdVectorNetworkAnalyzer():
    """
    This is a driver. 
    """
    def __init__(self):
        self.__resource_manager = None
        self.__instr_obj = None
        self.__channel = None
        self.__trace = None
        self.__port = None
        self.__marker = None
        self.__parameter = None
        self.__standard = None
        self.__cal_kit = None

        self.calculate = None
        self.display = None
        self.format = None
        self.hardcopy = None
        self.initiate = None
        self.mmemory = None
        self.sense = None
        self.service = None
        self.source = None
        self.status = None
        self.system = None
        self.trigger = None

        try:
            if self.__resource_manager is None:
                self.__resource_manager = visa.ResourceManager()
        except visa.VisaIOError as visaerror:
            print(f"{visaerror}")
        except visa.VisaIOWarning as visawarning:
            print(f"{visawarning}")

    def initialize(self, instrument_resource_string, *args):
        """
        Temporary, provisional docstring
        """
        try:
            self.__instr_obj = self.__resource_manager.open_resource(
                instrument_resource_string)
            
            self.calculate = self.Calculate(self.__instr_obj)
            self.display = self.Display(self.__instr_obj)
            self.format = self.Format(self.__instr_obj)
            self.hardcopy = self.HardCopy(self.__instr_obj)
            self.mmemory = self.Mmemory(self.__instr_obj)
            self.sense = self.Sense(self.__instr_obj)
            self.service = self.Service(self.__instr_obj)
            self.source = self.Source(self.__instr_obj)
            self.status = self.Status(self.__instr_obj)
            self.system = self.System(self.__instr_obj)
            self.trigger = self.Trigger(self.__instr_obj)

        except visa.VisaIOError as visaerr:
            print(f"{visaerr}")
        return

    def close(self):
        """
        Temporary, provisional docstring
        """
        try:
            self.__instr_obj.close()
        except visa.VisaIOError as visaerr:
            print(f"{visaerr}")
        return

    def write(self, command:str=None):
        """
        Temporary, provisional docstring
        """
        try:
            self.__instr_obj.write(command)
        except visa.VisaIOError as visaerr:
            print(f"{visaerr}")
        return

    def query(self, command):
        """
        Temporary, provisional docstring
        """
        response = ""
        try:
            response = self.__instr_obj.query(command).rstrip()
        except visa.VisaIOError as visaerr:
            print(f"{visaerr}")

        return response
    
    def abort(self):
        """
        Aborts the sweep. The channels in the Single trigger initiation 
        mode transition to the Hold state. The channels in the Continuous 
        trigger initiation mode transition to the trigger waiting state, if the 
        trigger source is set to Internal, the channel immediately starts a 
        new sweep.
        """
        self.write("ABOR")

    def opc_query(self):
        """Reads out the OPC bit (bit 0) of the Standard Event Status Register at the completion of all pending operations.
        """
        self.query("*OPC?")
    
    def reset(self):
        self.write("*RST")

    def get_error_list(self) -> list[str]:
        fnclst = []
        while True:
            tmpstr = self.__instr_obj.query("SYST:ERR?")
            if "No error" in tmpstr:
                break
            else:
                fnclst.append(tmpstr)
        return fnclst

    @property
    def cal_kit(self):
        return self.__cal_kit
    
    @cal_kit.setter
    def cal_kit(self, kit_number):
        self.__cal_kit = kit_number
        self.calculate._set_cal_kit(self.__cal_kit)
        self.display._set_cal_kit(self.__cal_kit)
        self.format._set_cal_kit(self.__cal_kit)
        self.hardcopy._set_cal_kit(self.__cal_kit)
        self.mmemory._set_cal_kit(self.__cal_kit)
        self.sense._set_cal_kit(self.__cal_kit)
        self.service._set_cal_kit(self.__cal_kit)
        self.source._set_cal_kit(self.__cal_kit)
        self.status._set_cal_kit(self.__cal_kit)
        self.system._set_cal_kit(self.__cal_kit)
        self.trigger._set_cal_kit(self.__cal_kit)

    @property
    def channel(self):
        return self.__instr_obj
    
    @channel.setter
    def channel(self, channel):
        self.__channel = channel
        self.calculate._set_channel(self.__channel)
        self.display._set_channel(self.__channel)
        self.format._set_channel(self.__channel)
        self.hardcopy._set_channel(self.__channel)
        self.mmemory._set_channel(self.__channel)
        self.sense._set_channel(self.__channel)
        self.service._set_channel(self.__channel)
        self.source._set_channel(self.__channel)
        self.status._set_channel(self.__channel)
        self.system._set_channel(self.__channel)
        self.trigger._set_channel(self.__channel)
    
    @property
    def marker(self):
        return self.__marker
    
    @marker.setter
    def marker(self, marker):
        self.__marker = marker
        self.calculate._set_marker(self.__marker)
        self.display._set_marker(self.__marker)
        self.format._set_marker(self.__marker)
        self.hardcopy._set_marker(self.__marker)
        self.mmemory._set_marker(self.__marker)
        self.sense._set_marker(self.__marker)
        self.service._set_marker(self.__marker)
        self.source._set_marker(self.__marker)
        self.status._set_marker(self.__marker)
        self.system._set_marker(self.__marker)
        self.trigger._set_marker(self.__marker)

    @property
    def parameter(self):
        return self.__parameter
    
    @parameter.setter
    def parameter(self, parameter):
        self.__parameter = parameter
        self.calculate._set_parameter(self.__parameter)
        self.display._set_parameter(self.__parameter)
        self.format._set_parameter(self.__parameter)
        self.hardcopy._set_parameter(self.__parameter)
        self.mmemory._set_parameter(self.__parameter)
        self.sense._set_parameter(self.__parameter)
        self.service._set_parameter(self.__parameter)
        self.source._set_parameter(self.__parameter)
        self.status._set_parameter(self.__parameter)
        self.system._set_parameter(self.__parameter)
        self.trigger._set_parameter(self.__parameter)

    @property
    def port(self):
        return self.__port
    
    @port.setter
    def port(self, port):
        self.__port = port
        self.calculate._set_port(self.__port)
        self.display._set_port(self.__port)
        self.format._set_port(self.__port)
        self.hardcopy._set_port(self.__port)
        self.mmemory._set_port(self.__port)
        self.sense._set_port(self.__port)
        self.service._set_port(self.__port)
        self.source._set_port(self.__port)
        self.status._set_port(self.__port)
        self.system._set_port(self.__port)
        self.trigger._set_port(self.__port)
    
    @property
    def standard(self):
        return self.__standard
    
    @standard.setter
    def standard(self, standard):
        self.__standard = standard
        self.calculate._set_standard(self.__standard)
        self.display._set_standard(self.__standard)
        self.format._set_standard(self.__standard)
        self.hardcopy._set_standard(self.__standard)
        self.mmemory._set_standard(self.__standard)
        self.sense._set_standard(self.__standard)
        self.service._set_standard(self.__standard)
        self.source._set_standard(self.__standard)
        self.status._set_standard(self.__standard)
        self.system._set_standard(self.__standard)
        self.trigger._set_standard(self.__standard)

    @property
    def trace(self):
        return self.__trace 
    
    @trace.setter
    def trace(self, trace):
        self.__trace = trace
        self.calculate._set_trace(self.__trace)
        self.display._set_trace(self.__trace)
        self.format._set_trace(self.__trace)
        self.hardcopy._set_trace(self.__trace)
        self.mmemory._set_trace(self.__trace)
        self.sense._set_trace(self.__trace)
        self.service._set_trace(self.__trace)
        self.source._set_trace(self.__trace)
        self.status._set_trace(self.__trace)
        self.system._set_trace(self.__trace)
        self.trigger._set_trace(self.__trace)

    class Calculate():
        def __init__(self, instrobj):
            self.__instr_obj = instrobj
            self.__channel = None
            self.__trace = None
            self.__marker = None
            self.__port = None
            self.__parameter = None
            self.__standard = None
            self.__cal_kit = None

            self.conversion     = self.Conversion(self.__instr_obj)
            self.correction     = self.Correction(self.__instr_obj)
            self.data           = self.Data(self.__instr_obj)
            self.format         = self.Format(self.__instr_obj)
            self.fixturesimulate= self.FixtureSimulate(self.__instr_obj)
            self.function       = self.Function(self.__instr_obj)
            self.hold           = self.Hold(self.__instr_obj)
            self.limit          = self.Limit(self.__instr_obj)
            self.marker         = self.Marker(self.__instr_obj)
            self.math           = self.Math(self.__instr_obj)
            self.mathstatistics = self.MathStatistics(self.__instr_obj)
            self.parameter      = self.Parameter(self.__instr_obj)
            self.ripplelimit    = self.RippleLimit(self.__instr_obj)
            self.smoothing      = self.Smoothing(self.__instr_obj)
            self.transform      = self.Transform(self.__instr_obj)

        def _set_channel(self, channel):
            self.__channel = channel
            self.conversion._set_channel(self.__channel)
            self.correction._set_channel(self.__channel)
            self.data._set_channel(self.__channel)
            self.format._set_channel(self.__channel)
            self.fixturesimulate._set_channel(self.__channel)
            self.function._set_channel(self.__channel)
            self.hold._set_channel(self.__channel)
            self.limit._set_channel(self.__channel)
            self.marker._set_channel(self.__channel)
            self.math._set_channel(self.__channel)
            self.mathstatistics._set_channel(self.__channel)
            self.parameter._set_channel(self.__channel)
            self.ripplelimit._set_channel(self.__channel)
            self.smoothing._set_channel(self.__channel)
            self.transform._set_channel(self.__channel)

        def _set_trace(self, trace):
            self.__trace = trace
            self.conversion._set_trace(self.__trace)
            self.data._set_trace(self.__trace)
            self.format._set_trace(self.__trace)
            self.fixturesimulate._set_trace(self.__trace)
            self.function._set_trace(self.__trace)
            self.hold._set_trace(self.__trace)
            self.limit._set_trace(self.__trace)
            self.marker._set_trace(self.__trace)
            self.math._set_trace(self.__trace)
            self.mathstatistics._set_trace(self.__trace)
            self.parameter._set_trace(self.__trace)
            self.ripplelimit._set_trace(self.__trace)
            self.smoothing._set_trace(self.__trace)
            self.transform._set_trace(self.__trace)

        def _set_marker(self, marker):
            self.__marker = marker
            self.conversion._set_marker(self.__marker)
        
        def _set_port(self, port):
            self.__port = port
            self.conversion._set_port(self.__port)

        def _set_parameter(self, parameter):
            self.__parameter = parameter
            self.conversion._set_parameter(self.__parameter)
        
        def _set_standard(self, standard):
            self.__standard = standard
            self.conversion._set_standard(self.__standard)
        
        def _set_cal_kit(self, kit):
            self.__cal_kit = kit
            self.conversion._set_cal_kit(self.__cal_kit)

        class Conversion():
            def __init__(self, instrobj):
                self.__instr_obj = instrobj
                self.__channel = None
                self.__trace = None
                self.__marker = None
                self.__port = None
                self.__parameter = None
                self.__standard = None
                self.__cal_kit = None

            def _set_channel(self, channel):
                self.__channel = channel
            
            def _set_trace(self, trace):
                self.__trace = trace

            def _set_marker(self, marker):
                self.__marker = marker
            
            def _set_port(self, port):
                self.__port = port
            
            def _set_parameter(self, parameter):
                self.__parameter = parameter
            
            def _set_standard(self, standard):
                self.__standard = standard
            
            def _set_cal_kit(self, kit):
                self.__cal_kit = kit

            @property
            def conversion(self):
                return f"CALC{self.__channel}:CONV?"
            
            @conversion.setter
            def conversion(self, state):
                val = f"CALC{self.__channel}:CONV {state}"
                print(val)

            @property
            def function(self):
                return f"CALC{self.__channel}:CONV:FUNC?"
            
            @function.setter
            def conversion_function(self, function):
                val = f"CALC{self.__channel}:CONV:FUNC {function}"

            @property
            def state(self):
                return f"CALC{self.__channel}:CONV:FUNC?"
            
            @state.setter
            def state(self, state):
                val = state

        class Correction():
            def __init__(self, instrobj):
                self.__instr_obj = instrobj
                self.__channel = None
                self.__trace = None
                self.__marker = None
                self.__port = None
                self.__parameter = None
                self.__standard = None
                self.__cal_kit = None

                self.electrical_delay   = self.ElectricalDelay(self.__instr_obj)
                self.offset             = self.Offset(self.__instr_obj)

            def _set_channel(self, channel):
                self.__channel = channel
                self.electrical_delay._set_channel(self.__channel)
            
            def _set_trace(self, trace):
                self.__trace = trace
                self.electrical_delay._set_trace(self.__trace)
            
            def _set_marker(self, marker):
                self.__marker = marker
            
            def _set_port(self, port):
                self.__port = port
            
            def _set_parameter(self, parameter):
                self.__parameter = parameter
            
            def _set_standard(self, standard):
                self.__standard = standard
            
            def _set_cal_kit(self, kit):
                self.__cal_kit = kit

            class ElectricalDelay():
                def __init__(self, instrobj):
                    self.__instr_obj = instrobj
                    self.__channel = None
                    self.__trace = None
                    self.__marker = None
                    self.__port = None
                    self.__parameter = None
                    self.__standard = None
                    self.__cal_kit = None

                def _set_channel(self, channel):
                    self.__channel = channel
                
                def _set_trace(self, trace):
                    self.__trace = trace

                def _set_marker(self, marker):
                    self.__marker = marker
                
                def _set_port(self, port):
                    self.__port = port
                
                def _set_parameter(self, parameter):
                    self.__parameter = parameter
                
                def _set_standard(self, standard):
                    self.__standard = standard
                
                def _set_cal_kit(self, kit):
                    self.__cal_kit = kit
                
                @property
                def media(self) -> str:
                    """This command gets the type of media in the electrical delay function.

                    Returns:
                        str: COAXial or WAVEguide
                    """
                    return self.__instr_obj.query(f"CALC{self.__channel}:TRAC{self.__trace}:CORR:EDEL:MED?").rstrip()
                
                @media.setter
                def media(self, type:str):
                    """This command sets the type of media in the electrical delay function.

                    Args:
                        type (str): COAXial or WAVEguide
                    """
                    self.__instr_obj.write(f"CALC{self.__channel}:TRAC{self.__trace}:CORR:EDEL:MED {type}")
                
                @property
                def time(self) -> float:
                    """This command gets the electrical delay time of the active or selected channel and trace.

                    Returns:
                        float: Electrical time delay from -10.0 to 10.0
                    """
                    return float(self.__instr_obj.query(f"CALC{self.__channel}:TRAC{self.__trace}:CORR:EDEL:TIME?").rstrip())
                
                @time.setter
                def time(self, value:float):
                    """This command sets the electrical delay time of the active or selected channel and trace.

                    Args:
                        value (float): Electrical time delay from -10.0 to 10.0
                    """
                    self.__instr_obj.write(f"CALC{self.__channel}:TRAC{self.__trace}:CORR:EDEL:TIME {value}")
            
                class Distance():
                    def __init(self, instrobj):
                        self.__instr_obj = instrobj
                        self.__channel = None
                        self.__trace = None
                        self.__marker = None
                    
                    def _set_channel(self, channel):
                        self.__channel = channel
                    
                    def _set_trace(self, trace):
                        self.__trace = trace

                    def _set_marker(self, marker):
                        self.__marker = marker

                    @property
                    def distance(self):
                        """Reads out the value of the equivalent distance in the electrical delay function. 

                        Returns:
                            float: The distance value.
                        """
                        return float(self.__instr_obj.query(f"CALC{self.__channel}:TRAC{self.__trace}:CORR:EDEL:DIST?").rstrip())
                    
                    @distance.setter
                    def distance(self, dist:float=0.1):
                        """Sets the value of the equivalent distance in the electrical delay function. 

                        Args:
                            dist (float): The distance value.
                        """
                        self.__instr_obj.write(f"CALC{self.__channel}:TRAC{self.__trace}:CORR:EDEL:DIST {dist}")
                    
                    @property
                    def units(self):
                        return 1
                    
                    @units.setter
                    def units(self, units):
                        val = units

                @property
                def media(self):
                    """This command reads the type of media in the electrical delay function.

                    Returns:
                        str: Return COAX for coaxial or WAVE for waveguide. 
                    """
                    return self.__instr_obj.query(f"CALC{self.__channel}:TRAC{self.__trace}:CORR:EDEL:MED?").rstrip()
                
                @media.setter
                def media(self, type):
                    """_summary_This command sets the type of media in the electrical delay function.

                    Args:
                        type (str): Pass COAX for coaxial or WAVE for waveguide.
                    """
                    self.__instr_obj.write(f"CALC{self.__channel}:TRAC{self.__trace}:CORR:EDEL:MED {type}")

            class Offset():
                def __init__(self, instrobj):
                    self.__instr_obj = instrobj
                    self.__channel = None
                    self.__trace = None
                    self.__marker = None
                    self.__port = None
                    self.__parameter = None
                    self.__standard = None
                    self.__cal_kit = None

                def _set_channel(self, channel):
                    self.__channel = channel
                
                def _set_trace(self, trace):
                    self.__trace = trace

                def _set_marker(self, marker):
                    self.__marker = marker
                
                def _set_port(self, port):
                    self.__port = port
                
                def _set_parameter(self, parameter):
                    self.__parameter = parameter
                
                def _set_standard(self, standard):
                    self.__standard = standard
                
                def _set_cal_kit(self, kit):
                    self.__cal_kit = kit

                @property
                def phase(self) -> float:
                    """This command gets the phase offset of the active or selected channel and trace.

                    Returns:
                        float: Phase in degrees. 
                    """
                    return float(self.__instr_obj.query(f"CALC{self.__channel}:TRAC{self.__trace}:CORR:OFFS:PHAS?").rstrip())
                
                @phase.setter
                def phase(self, value:float):
                    """This command sets the phase offset of the active or selected channel and trace.

                    Args:
                        value (float): Phase in degrees, -360.0 to 360.0.
                    """
                    self.__instr_obj.write(f"CALC{self.__channel}:TRAC{self.__trace}:CORR:OFFS:PHAS {value}")

        class Data():
            def __init__(self, instrobj):
                self.__instr_obj = instrobj
                self.__channel = None
                self.__trace = None
                self.__marker = None
                self.__port = None
                self.__parameter = None
                self.__standard = None
                self.__cal_kit = None

            def _set_channel(self, channel):
                self.__channel = channel
            
            def _set_trace(self, trace):
                self.__trace = trace

            def _set_marker(self, marker):
                self.__marker = marker
            
            def _set_port(self, port):
                self.__port = port
            
            def _set_parameter(self, parameter):
                self.__parameter = parameter
            
            def _set_standard(self, standard):
                self.__standard = standard
            
            def _set_cal_kit(self, kit):
                self.__cal_kit = kit

            @property
            def format_data(self) -> list[float]:
                """For the active or selected trace of a given channel, this command returns the formatted data array.

                Returns:
                    list[float]: Formatted data array as a list. 
                """
                strlist = self.__instr_obj.query(f"CALC{self.__channel}:TRAC{self.__trace}:DATA:FDAT?").rstrip().split(',')
                return strlist
            
            @format_data.setter
            def format_data(self, numeric_list:list[float]):
                """For the active or selected trace of a given channel, this command writes out the formatted data array.

                Args:
                    numeric_list (list[float]): Formatted data array as a list.
                """
                strlist = ""
                for val in numeric_list:
                    strlist = strlist + str(val) + ","
                self.__instr_obj.write(f"CALC{self.__channel}:TRAC{self.__trace}:DATA:FDAT {strlist}")
            
            @property
            def mult_trace_format_data(self) -> list[float]:
                """This command gets the formatted data array of multiple traces (traces n, m, .... to l) of the selected channel

                Returns:
                    list[float]: Formatted data array of multiple traces as a list. 
                """
                strlist = self.__instr_obj.query(f"CALC{self.__channel}:DATA:MDAT?").rstrip().split(',')
                return strlist
            
            @property
            def mult_trace_corrected_data(self) -> list[float]:
                """This command gets the corrected data array of multiple traces (traces n, m, .... to l) of the selected channel

                Returns:
                    list[float]: Corrected data array of multiple traces as a list. 
                """
                strlist = self.__instr_obj.query(f"CALC{self.__channel}:DATA:SDAT?").rstrip().split(',')
                return strlist
            
            @property
            def formatted_memory(self) -> list[float]:
                """This command gets the formatted memory array of the active or selected channel and trace. 

                Returns:
                    list[float]: 
                """
                return self.__instr_obj.query(f"CALC{self.__channel}:TRAC{self.__trace}:DATA:FMEM?").rstrip().split(',')
            
            @formatted_memory.setter
            def formatted_memory(self, numeric_list:list[float]):
                """This command sets the formatted memory array of the active or selected channel and trace. 

                Args:
                    numeric_list (list[float]): Values of formatted memory. 
                """
                strlist = ""
                for val in numeric_list:
                    strlist = strlist + str(val) + ","
                self.__instr_obj.write(f"CALC{self.__channel}:TRAC{self.__trace}:DATA:FMEM {numeric_list}")
            
            @property
            def corrected_data(self) -> list[float]:
                """This command gets the corrected data array of the active or selected channel and trace. 

                Returns:
                    list[float]: Values of corrected data. 
                """
                return self.__instr_obj.query(f"CALC{self.__channel}:TRAC{self.__trace}:DATA:SDAT?").rstrip().split(',')
            
            @corrected_data.setter
            def corrected_data(self, numeric_list:list[float]):
                """This command sets the corrected data array of the active or selected channel and trace. 

                Args:
                    numeric_list (list[float]): Values of corrected data.
                """
                strlist = ""
                for val in numeric_list:
                    strlist = strlist + str(val) + ","
                self.__instr_obj.write(f"CALC{self.__channel}:TRAC{self.__trace}:DATA:SDAT {numeric_list}")
            
            @property
            def corrected_memory(self) -> list[float]:
                """This command gets the corrected memory array of the active or selected channel and trace. 

                Returns:
                    list[float]: Values of corrected memory. 
                """
                return self.__instr_obj.query(f"CALC{self.__channel}:TRAC{self.__trace}:DATA:SMEM?").rstrip().split(',')
            
            @corrected_memory.setter
            def corrected_memory(self, numeric_list:list[float]):
                """This command sets the corrected memory array of the active or selected channel and trace. 

                Args:
                    numeric_list (list[float]): Values of corrected memory.
                """
                strlist = ""
                for val in numeric_list:
                    strlist = strlist + str(val) + ","
                self.__instr_obj.write(f"CALC{self.__channel}:TRAC{self.__trace}:DATA:SMEM {numeric_list}")
            
            @property
            def x_axis(self) -> list[float]:
                """This command reads the data of measurement points of X axis of the active or selected channel and trace.

                Returns:
                    list[float]: Values of x-axis measurement points.
                """
                return self.__instr_obj.query(f"CALC{self.__channel}:TRAC{self.__trace}:DATA:XAX?").rstrip().split(',')

        class Filter():
            def __init__(self, instrobj):
                self.__instr_obj = instrobj
                self.__channel = None
                self.__trace = None
                self.__marker = None
                self.__port = None
                self.__parameter = None
                self.__standard = None
                self.__cal_kit = None

                self.time = self.Time(self.__instr_obj)

            def _set_channel(self, channel):
                self.__channel = channel
            
            def _set_trace(self, trace):
                self.__trace = trace
            
            def _set_marker(self, marker):
                self.__marker = marker
            
            def _set_port(self, port):
                self.__port = port
            
            def _set_parameter(self, parameter):
                self.__parameter = parameter
            
            def _set_standard(self, standard):
                self.__standard = standard
            
            def _set_cal_kit(self, kit):
                self.__cal_kit = kit

            class Time():
                def __init__(self, instrobj):
                    self.__instr_obj = instrobj
                    self.__channel = None
                    self.__trace = None
                    self.__marker = None
                    self.__port = None
                    self.__parameter = None
                    self.__standard = None
                    self.__cal_kit = None
                
                def _set_channel(self, channel):
                    self.__channel = channel
                
                def _set_trace(self, trace):
                    self.__trace = trace
                
                def _set_marker(self, marker):
                    self.__marker = marker
                
                def _set_port(self, port):
                    self.__port = port
                
                def _set_parameter(self, parameter):
                    self.__parameter = parameter
                
                def _set_standard(self, standard):
                    self.__standard = standard
                
                def _set_cal_kit(self, kit):
                    self.__cal_kit = kit
                
                @property
                def type(self) -> str:
                    """This command gets the gate type used for the gating function of the time domain function of the acive or selected channel and trace.

                    Returns:
                        str: Responds with BPASs or NOTCh.
                    """
                    return self.__instr_obj.query(f"CALC{self.__channel}:TRAC{self.__trace}:FILT:TIME:TYPE?")
                
                @type.setter
                def type(self, type:str=""):
                    """This command sets the gate type used for the gating function of the time domain function of the acive or selected channel and trace.

                    Args:
                        type (str, optional): BPASs or NOTCh. Defaults to "BPAS".
                    """
                    self.__instr_obj.write(f"CALC{self.__channel}:TRAC{self.__trace}:FILT:TIME:TYPE {type}")

                @property
                def center(self) -> float:
                    """This command gets the center value of the gate used for the gating function of the time domain function of the active or selected channel and trace. 

                    Returns:
                        float: The center value from -66.73E9 to +66.73E9.
                    """
                    return float(self.__instr_obj.query(f"CALC{self.__channel}:TRAC{self.__trace}:FILT:TIME:CENT?").rstrip())
                
                @center.setter
                def center(self, value:float):
                    """This command sets the center value of the gate used for the gating function of the time domain function of the active or selected channel and trace. 

                    Args:
                        value (float): The center value -66.73E9 to +66.73E9.
                    """
                    self.__instr_obj.write(f"CALC{self.__channel}:TRAC{self.__trace}:FILT:TIME:CENT {value}")

                @property
                def shape(self) -> str:
                    """This command gets the shape of the gate used for the gating function of the time domain function of the active or selected channel and trace. 

                    Returns:
                        str: Either MAXimum, MINimum, NORMal, or WIDE
                    """
                    return self.__instr_obj.query(f"CALC{self.__channel}:TRAC{self.__trace}:FILT:TIME:SHAP?").rstrip()
                
                @shape.setter
                def shape(self, shape:str="NORM"):
                    """This command sets the shape of the gate used for the gating function of the time domain function of the active or selected channel and trace. 

                    Args:
                        shape (str, optional): Pass MAXimum, MINimum, NORMal, or WIDE. Defaults to "NORM".
                    """
                    self.__instr_obj.write(f"CALC{self.__channel}:TRAC{self.__trace}:FILT:TIME:SHAP {shape}")

                @property
                def start(self) -> float:
                    """This command gets the start value of the gate used for the gating function of the time domain function of the active or selected channel and trace. 

                    Returns:
                        float: The start value for the gating function. 
                    """
                    return self.__instr_obj.query(f"CALC{self.__channel}:TRAC{self.__trace}:FILT:TIME:STAR?")
                
                @start.setter
                def start(self, value:float):
                    """This command sets the start value of the gate used for the gating function of the time domain function of the active or selected channel and trace. 

                    Args:
                        value (float): The start value for the gating function. 
                    """
                    self.__instr_obj.write(f"CALC{self.__channel}:TRAC{self.__trace}:FILT:TIME:STAR {value}")
                
                @property
                def state(self) -> bool:
                    """Reports the state of the gating function of the time domain function of the active or selected channel and trace. 

                    Returns:
                        bool: _description_
                    """
                    valstr = self.__instr_obj.query(f"CALC{self.__trace}:TRAC{self.__trace}:FILT:TIME:STAT?").rstrip()
                    if "0" in valstr:
                        retval = False
                    else:
                        retval = True
                    return retval

                @state.setter
                def state(self, enabled:bool=False):
                    """This command turns ON/OFF the gating function of the time domain function of the active or selected channel and trace. 

                    Args:
                        enabled (bool, optional): False = OFF, True = ON. Defaults to False.
                    """
                    altstr = ""
                    if enabled is False:
                        altstr = "OFF"
                    else:
                        altstr = "ON"
                    self.__instr_obj.write(f"CALC{self.__trace}:TRAC{self.__trace}:FILT:TIME:STATe {altstr}")

        class Format():
            def __init__(self, instrobj):
                self.__instr_obj = instrobj
                self.__channel = None
                self.__trace = None
                self.__marker = None
                self.__port = None
                self.__parameter = None
                self.__standard = None
                self.__cal_kit = None

            def _set_channel(self, channel):
                self.__channel = channel
            
            def _set_trace(self, trace):
                self.__trace = trace
            
            def _set_marker(self, marker):
                self.__marker = marker
            
            def _set_port(self, port):
                self.__port = port
            
            def _set_parameter(self, parameter):
                self.__parameter = parameter
            
            def _set_standard(self, standard):
                self.__standard = standard
            
            def _set_cal_kit(self, kit):
                self.__cal_kit = kit

            @property
            def type(self) -> str:
                """This command gets the data format of the active trace of a select channel.

                Returns:
                    str: Returned format type of MLOG, PHAS, GDEL, SLIN, SLOG, SCOM, SMIT, SADM, PLIN, PLOG, POL, MLIN, SWR, REAL, IMAG or UPH.
                """
                return self.__instr_obj.query(f"CALC{self.__channel}:TRAC{self.__trace}>:FORMat?").rstrip().lower()
            
            @type.setter
            def type(self, type:str="mlog"):
                """This command sets the data format of the active trace of a select channel.

                Args:
                    type (str, optional): Use one of the following - MLOGarithmic, PHASe, GDELay, SLINear, SLOGarithmic, SCOMplex, SMITh, SADMittance, PLINear, PLOGarithmic, POLar, MLINear, SWR, REAL, IMAGinary, UPHase. Defaults to "MLOG".
                """
                self.__instr_obj.write(f"CALC{self.__channel}:TRAC{self.__trace}:FORMat {type.upper()}")

        class FixtureSimulate():
            def __init__(self, instrobj):
                self.__instr_obj = instrobj
                self.__channel = None
                self.__trace = None
                self.__marker = None
                self.__port = None
                self.__parameter = None
                self.__standard = None
                self.__cal_kit = None
                
                self.balance = self.Balance(self.__instr_obj)
                self.embed = self.Embed(self.__instr_obj)
                self.send = self.Send(self.__instr_obj)

            def _set_channel(self, channel):
                self.__channel = channel
            
            def _set_trace(self, trace):
                self.__trace = trace
            
            def _set_marker(self, marker):
                self.__marker = marker
            
            def _set_port(self, port):
                self.__port = port
            
            def _set_parameter(self, parameter):
                self.__parameter = parameter
            
            def _set_standard(self, standard):
                self.__standard = standard
            
            def _set_cal_kit(self, kit):
                self.__cal_kit = kit

            class Balance():
                def __init__(self, instrobj):
                    self.__instr_obj = instrobj
                    self.__channel = None
                    self.__trace = None
                    self.__marker = None
                    self.__port = None
                    self.__parameter = None
                    self.__standard = None
                    self.__cal_kit = None

                    self.czconversion = self.CZConversion(self.__instr_obj)
                    self.diff_matching_circuit = self.DifferentialMatchingCircuit(self.__instr_obj)
                    self.diffzconversion = self.DifferentialImpedanceConversion(self.__instr_obj)
                    self.parameter = self.Parameter(self.__instr_obj)
                    self.top = self.Top(self.__instr_obj)

                def _set_channel(self, channel):
                    self.__channel = channel
                
                def _set_trace(self, trace):
                    self.__trace = trace
                
                def _set_marker(self, marker):
                    self.__marker = marker
                
                def _set_port(self, port):
                    self.__port = port
                
                def _set_parameter(self, parameter):
                    self.__parameter = parameter
                
                def _set_standard(self, standard):
                    self.__standard = standard
                
                def _set_cal_kit(self, kit):
                    self.__cal_kit = kit

                class CZConversion():
                    def __init__(self, instrobj):
                        self.__instr_obj = instrobj
                        self.__channel = None
                        self.__trace = None
                        self.__marker = None
                        self.__port = None
                        self.__parameter = None
                        self.__standard = None
                        self.__cal_kit = None

                        self.balance_port = self.BalancePort(self.__instr_obj)

                    def _set_channel(self, channel):
                        self.__channel = channel
                    
                    def _set_trace(self, trace):
                        self.__trace = trace

                    def _set_marker(self, marker):
                        self.__marker = marker
                    
                    def _set_port(self, port):
                        self.__port = port
                    
                    def _set_parameter(self, parameter):
                        self.__parameter = parameter
                    
                    def _set_standard(self, standard):
                        self.__standard = standard
                    
                    def _set_cal_kit(self, kit):
                        self.__cal_kit = kit

                    class BalancePort():
                        def __init__(self, instrobj):
                            self.__instr_obj = instrobj
                            self.__channel = None
                            self.__trace = None
                            self.__marker = None
                            self.__port = None
                            self.__parameter = None
                            self.__standard = None
                            self.__cal_kit = None

                        def _set_channel(self, channel):
                            self.__channel = channel
                        
                        def _set_trace(self, trace):
                            self.__trace = trace

                        def _set_marker(self, marker):
                            self.__marker = marker
                        
                        def _set_port(self, port):
                            self.__port = port
                        
                        def _set_parameter(self, parameter):
                            self.__parameter = parameter
                        
                        def _set_standard(self, standard):
                            self.__standard = standard
                        
                        def _set_cal_kit(self, kit):
                            self.__cal_kit = kit

                    @property
                    def state(self):
                        return 1
                    
                    @state.setter
                    def state(self, state):
                        v = state

                @property
                def device(self):
                    return 1
                
                @device.setter
                def device(self, type):
                    val = type
                
                class DifferentialMatchingCircuit():
                    def __init__(self, instrobj):
                        self.__instr_obj = instrobj
                        self.__channel = None
                        self.__trace = None
                    
                        self.balance_port = self.BalancePort(self.__instr_obj)
                        self.__marker = None
                        self.__port = None
                        self.__parameter = None
                        self.__standard = None
                        self.__cal_kit = None

                    def _set_channel(self, channel):
                        self.__channel = channel
                    
                    def _set_trace(self, trace):
                        self.__trace = trace

                    def _set_marker(self, marker):
                        self.__marker = marker
                    
                    def _set_port(self, port):
                        self.__port = port
                    
                    def _set_parameter(self, parameter):
                        self.__parameter = parameter
                    
                    def _set_standard(self, standard):
                        self.__standard = standard
                    
                    def _set_cal_kit(self, kit):
                        self.__cal_kit = kit

                    class BalancePort():
                        def __init__(self, instrobj):
                            self.__instr_obj = instrobj
                            self.__channel = None
                            self.__trace = None
                            self.__marker = None
                            self.__port = None
                            self.__parameter = None
                            self.__standard = None
                            self.__cal_kit = None

                        def _set_channel(self, channel):
                            self.__channel = channel
                        
                        def _set_trace(self, trace):
                            self.__trace = trace

                        def _set_marker(self, marker):
                            self.__marker = marker
                        
                        def _set_port(self, port):
                            self.__port = port
                        
                        def _set_parameter(self, parameter):
                            self.__parameter = parameter
                        
                        def _set_standard(self, standard):
                            self.__standard = standard
                        
                        def _set_cal_kit(self, kit):
                            self.__cal_kit = kit

                    @property
                    def state(self):
                        return 1
                    
                    @state.setter
                    def state(self, state):
                        v = state

                class DifferentialImpedanceConversion():
                    def __init__(self, instrobj):
                        self.__instr_obj = instrobj
                        self.__channel = None
                        self.__trace = None
                        self.__marker = None
                        self.__port = None
                        self.__parameter = None
                        self.__standard = None
                        self.__cal_kit = None

                        self.balance_port = self.BalancePort(self.__instr_obj)

                    def _set_channel(self, channel):
                        self.__channel = channel
                    
                    def _set_trace(self, trace):
                        self.__trace = trace

                    def _set_marker(self, marker):
                        self.__marker = marker
                    
                    def _set_port(self, port):
                        self.__port = port
                    
                    def _set_parameter(self, parameter):
                        self.__parameter = parameter
                    
                    def _set_standard(self, standard):
                        self.__standard = standard
                    
                    def _set_cal_kit(self, kit):
                        self.__cal_kit = kit

                    class BalancePort():
                        def __init__(self, instrobj):
                            self.__instr_obj = instrobj
                            self.__channel = None
                            self.__trace = None
                            self.__marker = None
                            self.__port = None
                            self.__parameter = None
                            self.__standard = None
                            self.__cal_kit = None

                        def _set_channel(self, channel):
                            self.__channel = channel
                        
                        def _set_trace(self, trace):
                            self.__trace = trace

                        def _set_marker(self, marker):
                            self.__marker = marker
                        
                        def _set_port(self, port):
                            self.__port = port
                        
                        def _set_parameter(self, parameter):
                            self.__parameter = parameter
                        
                        def _set_standard(self, standard):
                            self.__standard = standard
                        
                        def _set_cal_kit(self, kit):
                            self.__cal_kit = kit

                    @property
                    def state(self):
                        return 1
                    
                    @state.setter
                    def state(self, state):
                        v = state

                class Parameter():
                    def __init__(self, instrobj):
                        self.__instr_obj = instrobj
                        self.__channel = None
                        self.__trace = None
                        self.__marker = None
                        self.__port = None
                        self.__parameter = None
                        self.__standard = None
                        self.__cal_kit = None

                    def _set_channel(self, channel):
                        self.__channel = channel
                    
                    def _set_trace(self, trace):
                        self.__trace = trace

                    def _set_marker(self, marker):
                        self.__marker = marker
                    
                    def _set_port(self, port):
                        self.__port = port
                    
                    def _set_parameter(self, parameter):
                        self.__parameter = parameter
                    
                    def _set_standard(self, standard):
                        self.__standard = standard
                    
                    def _set_cal_kit(self, kit):
                        self.__cal_kit = kit

                class Top():
                    def __init__(self, instrobj):
                        self.__instr_obj = instrobj
                        self.__channel = None
                        self.__trace = None
                        self.__marker = None
                        self.__port = None
                        self.__parameter = None
                        self.__standard = None
                        self.__cal_kit = None

                    def _set_channel(self, channel):
                        self.__channel = channel
                    
                    def _set_trace(self, trace):
                        self.__trace = trace

                    def _set_marker(self, marker):
                        self.__marker = marker
                    
                    def _set_port(self, port):
                        self.__port = port
                    
                    def _set_parameter(self, parameter):
                        self.__parameter = parameter
                    
                    def _set_standard(self, standard):
                        self.__standard = standard
                    
                    def _set_cal_kit(self, kit):
                        self.__cal_kit = kit

            class Embed():
                def __init__(self, instrobj):
                    self.__instr_obj = instrobj
                    self.__channel = None
                    self.__trace = None
                    self.__marker = None
                    self.__port = None
                    self.__parameter = None
                    self.__standard = None
                    self.__cal_kit = None

                    self.network = self.Network(self.__instr_obj)
                    self.topology = self.Topology(self.__instr_obj)

                def _set_channel(self, channel):
                    self.__channel = channel
                
                def _set_trace(self, trace):
                    self.__trace = trace

                def _set_marker(self, marker):
                    self.__marker = marker
                
                def _set_port(self, port):
                    self.__port = port
                
                def _set_parameter(self, parameter):
                    self.__parameter = parameter
                
                def _set_standard(self, standard):
                    self.__standard = standard
                
                def _set_cal_kit(self, kit):
                    self.__cal_kit = kit

                class Network():
                    def __init__(self, instrobj):
                        self.__instr_obj = instrobj
                        self.__channel = None
                        self.__trace = None
                        self.__marker = None
                        self.__port = None
                        self.__parameter = None
                        self.__standard = None
                        self.__cal_kit = None

                    def _set_channel(self, channel):
                        self.__channel = channel
                    
                    def _set_trace(self, trace):
                        self.__trace = trace

                    def _set_marker(self, marker):
                        self.__marker = marker
                    
                    def _set_port(self, port):
                        self.__port = port
                    
                    def _set_parameter(self, parameter):
                        self.__parameter = parameter
                    
                    def _set_standard(self, standard):
                        self.__standard = standard
                    
                    def _set_cal_kit(self, kit):
                        self.__cal_kit = kit

                @property
                def state(self):
                    return 1
                
                @state.setter
                def state(self, state):
                    val = state

                class Topology():
                    def __init__(self, instrobj):
                        self.__instr_obj = instrobj
                        self.__channel = None
                        self.__trace = None
                        self.__marker = None
                        self.__port = None
                        self.__parameter = None
                        self.__standard = None
                        self.__cal_kit = None

                    def _set_channel(self, channel):
                        self.__channel = channel
                    
                    def _set_trace(self, trace):
                        self.__trace = trace

                    def _set_marker(self, marker):
                        self.__marker = marker
                    
                    def _set_port(self, port):
                        self.__port = port
                    
                    def _set_parameter(self, parameter):
                        self.__parameter = parameter
                    
                    def _set_standard(self, standard):
                        self.__standard = standard
                    
                    def _set_cal_kit(self, kit):
                        self.__cal_kit = kit

                @property
                def type(self):
                    return 1
                
                @type.setter
                def type(self, type):
                    val = 1

            class Send():
                def __init__(self, instrobj):
                    self.__instr_obj = instrobj
                    self.__channel = None
                    self.__trace = None

                    self.deembed = self.Deembed(self.__instr_obj)
                    self.port_match_ckt = self.PortMatchCircuit(self.__instr_obj)
                    self.z_conversion = self.ZConversion(self.__instr_obj)

                def _set_channel(self, channel):
                    self.__channel = channel
                    self.deembed._set_channel(self.__channel)
                    self.port_match_ckt._set_channel(self.__channel)
                    self.z_conversion._set_channel(self.__channel)
                
                def _set_trace(self, trace):
                    self.__trace = trace
                    self.deembed._set_trace(self.__trace)
                    self.port_match_ckt._set_trace(self.__trace)
                    self.z_conversion._set_trace(self.__trace)

                class Deembed():
                    def __init__(self, instrobj):
                        self.__instr_obj = instrobj
                        self.__channel = None
                        self.__trace = None
                        self.__marker = None
                        self.__port = None
                        self.__parameter = None
                        self.__standard = None
                        self.__cal_kit = None

                    def _set_channel(self, channel):
                        self.__channel = channel
                    
                    def _set_trace(self, trace):
                        self.__trace = trace

                    def _set_marker(self, marker):
                        self.__marker = marker
                    
                    def _set_port(self, port):
                        self.__port = port
                    
                    def _set_parameter(self, parameter):
                        self.__parameter = parameter
                    
                    def _set_standard(self, standard):
                        self.__standard = standard
                    
                    def _set_cal_kit(self, kit):
                        self.__cal_kit = kit
                
                class PortMatchCircuit():
                    def __init__(self, instrobj):
                        self.__instr_obj = instrobj
                        self.__channel = None
                        self.__trace = None
                        self.__marker = None
                        self.__port = None
                        self.__parameter = None
                        self.__standard = None
                        self.__cal_kit = None

                    def _set_channel(self, channel):
                        self.__channel = channel
                    
                    def _set_trace(self, trace):
                        self.__trace = trace

                    def _set_marker(self, marker):
                        self.__marker = marker
                    
                    def _set_port(self, port):
                        self.__port = port
                    
                    def _set_parameter(self, parameter):
                        self.__parameter = parameter
                    
                    def _set_standard(self, standard):
                        self.__standard = standard
                    
                    def _set_cal_kit(self, kit):
                        self.__cal_kit = kit

                class ZConversion():
                    def __init__(self, instrobj):
                        self.__instr_obj = instrobj
                        self.__channel = None
                        self.__trace = None
                        self.__marker = None
                        self.__port = None
                        self.__parameter = None
                        self.__standard = None
                        self.__cal_kit = None

                    def _set_channel(self, channel):
                        self.__channel = channel
                    
                    def _set_trace(self, trace):
                        self.__trace = trace

                    def _set_marker(self, marker):
                        self.__marker = marker
                    
                    def _set_port(self, port):
                        self.__port = port
                    
                    def _set_parameter(self, parameter):
                        self.__parameter = parameter
                    
                    def _set_standard(self, standard):
                        self.__standard = standard
                    
                    def _set_cal_kit(self, kit):
                        self.__cal_kit = kit
            
            @property
            def state(self):
                return 1
            
            @state.setter
            def state(self, state):
                val = 1
        
        class Function():
            def __init__(self, instrobj):
                self.__instr_obj = instrobj
                self.__channel = None
                self.__trace = None
                self.__marker = None
                self.__port = None
                self.__parameter = None
                self.__standard = None
                self.__cal_kit = None

                self.domain = self.Domain(self.__instr_obj)

            def _set_channel(self, channel):
                self.__channel = channel
                self.domain._set_channel(self.__channel)
            
            def _set_trace(self, trace):
                self.__trace = trace
                self.domain._set_trace(self.__trace)

            def _set_marker(self, marker):
                self.__marker = marker
                self.domain._set_marker(self.__marker)
            
            def _set_port(self, port):
                self.__port = port
                self.domain._set_port(self.__port)
            
            def _set_parameter(self, parameter):
                self.__parameter = parameter
                self.domain._set_parameter(self.__parameter)
            
            def _set_standard(self, standard):
                self.__standard = standard
                self.domain._set_standard(self.__standard)
            
            def _set_cal_kit(self, kit):
                self.__cal_kit = kit
                self.domain._set_cal_kit(self.__cal_kit)

            class Domain():
                def __init__(self, instrobj):
                    self.__instr_obj = instrobj
                    self.__channel = None
                    self.__trace = None
                    self.__marker = None
                    self.__port = None
                    self.__parameter = None
                    self.__standard = None
                    self.__cal_kit = None

                def _set_channel(self, channel):
                    self.__channel = channel
                
                def _set_trace(self, trace):
                    self.__trace = trace

                def _set_marker(self, marker):
                    self.__marker = marker
                
                def _set_port(self, port):
                    self.__port = port
                
                def _set_parameter(self, parameter):
                    self.__parameter = parameter
                
                def _set_standard(self, standard):
                    self.__standard = standard
                
                def _set_cal_kit(self, kit):
                    self.__cal_kit = kit


        class Hold():
            def __init__(self, instrobj):
                self.__instr_obj = instrobj
                self.__channel = None
                self.__trace = None
                self.__marker = None
                self.__port = None
                self.__parameter = None
                self.__standard = None
                self.__cal_kit = None
            
            def _set_channel(self, channel):
                self.__channel = channel
                #self.report._set_channel = self.__channel
            
            def _set_trace(self, trace):
                self.__trace = trace

            def _set_marker(self, marker):
                self.__marker = marker
            
            def _set_port(self, port):
                self.__port = port
            
            def _set_parameter(self, parameter):
                self.__parameter = parameter
            
            def _set_standard(self, standard):
                self.__standard = standard
            
            def _set_cal_kit(self, kit):
                self.__cal_kit = kit

        class Limit():
            def __init__(self, instrobj):
                self.__instr_obj = instrobj
                self.__channel = None
                self.__trace = None
                self.__marker = None
                self.__port = None
                self.__parameter = None
                self.__standard = None
                self.__cal_kit = None
                self.report = self.Report(self.__instr_obj)
                self.offset = self.Offset(self.__instr_obj)
            
            def _set_channel(self, channel):
                self.__channel = channel
                self.report._set_channel = self.__channel
            
            def _set_trace(self, trace):
                self.__trace = trace

            def _set_marker(self, marker):
                self.__marker = marker
            
            def _set_port(self, port):
                self.__port = port
            
            def _set_parameter(self, parameter):
                self.__parameter = parameter
            
            def _set_standard(self, standard):
                self.__standard = standard
            
            def _set_cal_kit(self, kit):
                self.__cal_kit = kit

            class Report():
                def __init__(self, instrobj):
                    self.__instr_obj = instrobj
                    self.__channel = None
                    self.__trace = None
                    self.__marker = None
                    self.__port = None
                    self.__parameter = None
                    self.__standard = None
                    self.__cal_kit = None

                def _set_channel(self, channel):
                    self.__channel = channel
                
                def _set_trace(self, trace):
                    self.__trace = trace

                def _set_marker(self, marker):
                    self.__marker = marker
                
                def _set_port(self, port):
                    self.__port = port
                
                def _set_parameter(self, parameter):
                    self.__parameter = parameter
                
                def _set_standard(self, standard):
                    self.__standard = standard
                
                def _set_cal_kit(self, kit):
                    self.__cal_kit = kit
            
            class Offset():
                def __init__(self, instrobj):
                    self.__instr_obj = instrobj
                    self.__channel = None
                    self.__trace = None
                    self.__marker = None
                    self.__port = None
                    self.__parameter = None
                    self.__standard = None
                    self.__cal_kit = None

                def _set_channel(self, channel):
                    self.__channel = channel
                
                def _set_trace(self, trace):
                    self.__trace = trace

                def _set_marker(self, marker):
                    self.__marker = marker
                
                def _set_port(self, port):
                    self.__port = port
                
                def _set_parameter(self, parameter):
                    self.__parameter = parameter
                
                def _set_standard(self, standard):
                    self.__standard = standard
                
                def _set_cal_kit(self, kit):
                    self.__cal_kit = kit

        class Marker():
            def __init__(self, instrobj):
                self.__instr_obj = instrobj
                self.__channel = None
                self.__trace = None
                self.__marker = None
                self.__port = None
                self.__parameter = None
                self.__standard = None
                self.__cal_kit = None

            def _set_channel(self, channel):
                self.__channel = channel
            
            def _set_trace(self, trace):
                self.__trace = trace

            def _set_marker(self, marker):
                self.__marker = marker
            
            def _set_port(self, port):
                self.__port = port
            
            def _set_parameter(self, parameter):
                self.__parameter = parameter
            
            def _set_standard(self, standard):
                self.__standard = standard
            
            def _set_cal_kit(self, kit):
                self.__cal_kit = kit

        class Math():
            def __init__(self, instrobj):
                self.__instr_obj = instrobj
                self.__channel = None
                self.__trace = None
                self.__marker = None
                self.__port = None
                self.__parameter = None
                self.__standard = None
                self.__cal_kit = None

            def _set_channel(self, channel):
                self.__channel = channel
            
            def _set_trace(self, trace):
                self.__trace = trace

            def _set_marker(self, marker):
                self.__marker = marker
            
            def _set_port(self, port):
                self.__port = port
            
            def _set_parameter(self, parameter):
                self.__parameter = parameter
            
            def _set_standard(self, standard):
                self.__standard = standard
            
            def _set_cal_kit(self, kit):
                self.__cal_kit = kit

        class MathStatistics():
            def __init__(self, instrobj):
                self.__instr_obj = instrobj
                self.__channel = None
                self.__trace = None
                self.__marker = None
                self.__port = None
                self.__parameter = None
                self.__standard = None
                self.__cal_kit = None

            def _set_channel(self, channel):
                self.__channel = channel
            
            def _set_trace(self, trace):
                self.__trace = trace
            
            def _set_marker(self, marker):
                self.__marker = marker
            
            def _set_port(self, port):
                self.__port = port
            
            def _set_parameter(self, parameter):
                self.__parameter = parameter
            
            def _set_standard(self, standard):
                self.__standard = standard
            
            def _set_cal_kit(self, kit):
                self.__cal_kit = kit

        class Parameter():
            def __init__(self, instrobj):
                self.__instr_obj = instrobj
                self.__channel = None
                self.__trace = None
                self.__marker = None
                self.__port = None
                self.__parameter = None
                self.__standard = None
                self.__cal_kit = None

            def _set_channel(self, channel):
                self.__channel = channel
            
            def _set_trace(self, trace):
                self.__trace = trace
            
            def _set_marker(self, marker):
                self.__marker = marker
            
            def _set_port(self, port):
                self.__port = port
            
            def _set_parameter(self, parameter):
                self.__parameter = parameter
            
            def _set_standard(self, standard):
                self.__standard = standard
            
            def _set_cal_kit(self, kit):
                self.__cal_kit = kit

            @property
            def tracecount(self) -> int:
                """Gets the number of traces available for the active channel.

                Returns:
                    int: Number of traces.
                """
                return self.__instr_obj.query(f":CALC{self.__channel}:PAR:COUN?")

            @tracecount.setter
            def tracecount(self, count:int=1):
                """Sets the number of traces available for teh active channel.

                Args:
                    count (int, optional): The number of traces for the channel to use. Defaults to 1.
                """
                self.__instr_obj.write(f":CALC{self.__channel}:PAR:COUN {count}")

            @property
            def traceselect(self) -> int:
                """Gets the active trace within the active channel.

                Returns:
                    int: The trace number of interest.
                """
                return self.__instr_obj.query(f":CALC{self.__channel}:PAR{self.__trace}:SEL?")
            
            @traceselect.setter
            def traceselect(self, activetrace:int=1):
                """Sets the active trace within the active channel.

                Args:
                    activetrace (int, optional): _description_. Defaults to 1.
                """
                self.__instr_obj.write(f":CALC{self.__channel}:PAR{activetrace}:SEL")

            @property
            def trace_sparam(self) -> str:
                """Gets the measurement scattering parameters of the select trace of a select channel.

                Returns:
                    str: Model/port count depended. Examples: "s11", "s22", "s12", "s21", "s13", etc. 
                """
                return self.__instr_obj.query(f":CALC{self.__channel}:PAR{self.__trace}:DEF?").rstrip()
            
            @trace_sparam.setter
            def trace_sparam(self, sparam:str="s11"):
                """Sets the measurement scattering parameters for the select trace of a select channel.

                Args:
                    sparam (str, optional): Model, port count dependent. Options include "s11", "s22", "s12", "s21", "s13", etc.  Defaults to "s11".
                """
                self.__instr_obj.write(f":CALC{self.__channel}:PAR{self.__trace}:DEF {sparam.upper()}")

        class RippleLimit():
            def __init__(self, instrobj):
                self.__instr_obj = instrobj
                self.__channel = None
                self.__trace = None
                self.__marker = None
                self.__port = None
                self.__parameter = None
                self.__standard = None
                self.__cal_kit = None

            def _set_channel(self, channel):
                self.__channel = channel
                #self.report._set_channel = self.__channel
            
            def _set_trace(self, trace):
                self.__trace = trace
            
            def _set_marker(self, marker):
                self.__marker = marker
            
            def _set_port(self, port):
                self.__port = port
            
            def _set_parameter(self, parameter):
                self.__parameter = parameter
            
            def _set_standard(self, standard):
                self.__standard = standard
            
            def _set_cal_kit(self, kit):
                self.__cal_kit = kit

        class Smoothing():
            def __init__(self, instrobj):
                self.__instr_obj = instrobj
                self.__channel = None
                self.__trace = None
                self.__marker = None
                self.__port = None
                self.__parameter = None
                self.__standard = None
                self.__cal_kit = None

            def _set_channel(self, channel):
                self.__channel = channel
            
            def _set_trace(self, trace):
                self.__trace = trace

            def _set_marker(self, marker):
                self.__marker = marker
            
            def _set_port(self, port):
                self.__port = port
            
            def _set_parameter(self, parameter):
                self.__parameter = parameter
            
            def _set_standard(self, standard):
                self.__standard = standard
            
            def _set_cal_kit(self, kit):
                self.__cal_kit = kit

        class Transform():
            def __init__(self, instrobj):
                self.__instr_obj = instrobj
                self.__channel = None
                self.__trace = None
                self.__marker = None
                self.__port = None
                self.__parameter = None
                self.__standard = None
                self.__cal_kit = None

            def _set_channel(self, channel):
                self.__channel = channel
            
            def _set_trace(self, trace):
                self.__trace = trace

            def _set_marker(self, marker):
                self.__marker = marker
            
            def _set_port(self, port):
                self.__port = port
            
            def _set_parameter(self, parameter):
                self.__parameter = parameter
            
            def _set_standard(self, standard):
                self.__standard = standard
            
            def _set_cal_kit(self, kit):
                self.__cal_kit = kit

    class Display():
        def __init__(self, instrobj):
            self.__instr_obj = instrobj
            self.__channel = None
            self.__trace = None
            self.__marker = None
            self.__port = None
            self.__parameter = None
            self.__standard = None
            self.__cal_kit = None

            self.color = self.Color(self.__instr_obj)
            self.window = self.Window(self.__instr_obj)

        def _set_channel(self, channel):
            self.__channel = channel
            self.color._set_channel(self.__channel)
            self.window._set_channel(self.__channel)

        def _set_trace(self, trace):
            self.__trace = trace
            self.color._set_trace(self.__trace)
            self.window._set_trace(self.__trace)
        
        def _set_marker(self, marker):
            self.__marker = marker
            self.color._set_marker(self.__marker)
            self.window._set_marker(self.__marker)
        
        def _set_port(self, port):
            self.__port = port
            self.color._set_port(self.__port)
            self.window._set_port(self.__port)
        
        def _set_parameter(self, parameter):
            self.__parameter = parameter
        
        def _set_standard(self, standard):
            self.__standard = standard
        
        def _set_cal_kit(self, kit):
            self.__cal_kit = kit

        class Color():
            def __init__(self, instrobj):
                self.__instr_obj = instrobj
                self.__channel = None
                self.__trace = None
                self.__marker = None
                self.__port = None
                self.__parameter = None
                self.__standard = None

                self.trace = self.Trace(self.__instr_obj)

            def _set_channel(self, channel):
                self.__channel = channel
                self.trace._set_channel(self.__channel)

            def _set_trace(self, trace):
                self.__trace = trace
                self.trace._set_trace(self.__trace)
            
            def _set_marker(self, marker):
                self.__marker = marker
                self.trace._set_marker(self.__marker)
            
            def _set_port(self, port):
                self.__port = port
                self.trace._set_port(self.__port)

            def reset(self):
                """
                This command resets the display color settings for all the items to the factory preset state, for normal display.
                """
                self.__instr_obj.write(f":DISP:COL:RES")

            class Trace():
                def __init__(self, instrobj):
                    self.__instr_obj = instrobj
                    self.__channel = None
                    self.__trace = None
                    self.__marker = None
                    self.__port = None
                
                def _set_channel(self, channel):
                    self.__channel = channel

                def _set_trace(self, trace):
                    self.__trace = trace
                
                def _set_marker(self, marker):
                    self.__marker = marker
                
                def _set_port(self, port):
                    self.__port = port

                def data(self, red:int=128, green:int=128, blue:int=128):
                    self.__instr_obj.write(f":DISP:COL:TRAC:DATA {red},{green},{blue}")  

                def memory(self, red:int=128, green:int=128, blue:int=128):
                    self.__instr_obj.write(f":DISP:COL:TRAC:MEM {red},{green},{blue}")  

        class Window():
            def __init__(self, instrobj):
                self.__instr_obj = instrobj
                self.__channel = None
                self.__trace = None
                self.__marker = None
                self.__port = None

                self.trace = self.Trace(self.__instr_obj)
            
            def _set_channel(self, channel):
                self.__channel = channel
                self.trace._set_channel(self.__channel)

            def _set_trace(self, trace):
                self.__trace = trace
                self.trace._set_trace(self.__trace)
            
            def _set_marker(self, marker):
                self.__marker = marker
                self.trace._set_marker(self.__marker)
            
            def _set_port(self, port):
                self.__port = port
                self.trace._set_port(self.__port)
            
            class Trace():
                def __init__(self, instrobj):
                    self.__instr_obj = instrobj
                    self.__channel = None
                    self.__trace = None
                    self.__marker = None
                    self.__port = None

                    self.y = self.Y(self.__instr_obj)
                
                def _set_channel(self, channel):
                    self.__channel = channel
                    self.y._set_channel(self.__channel)

                def _set_trace(self, trace):
                    self.__trace = trace
                    self.y._set_trace(self.__trace)

                def _set_marker(self, marker):
                    self.__marker = marker
                    self.y._set_marker(self.__marker)
                
                def _set_port(self, port):
                    self.__port = port
                    self.y._set_port(self.__port)
                
                class Y():
                    def __init__(self, instrobj):
                        self.__instr_obj = instrobj
                        self.__channel = None
                        self.__trace = None
                        self.__marker = None
                        self.__port = None
                    
                    def _set_channel(self, channel):
                        self.__channel = channel

                    def _set_trace(self, trace):
                        self.__trace = trace
                    
                    def _set_marker(self, marker):
                        self.__marker = marker
                    
                    def _set_port(self, port):
                        self.__port = port

                    def autoscale(self):
                        """For a select trace of a select channel, executes the auto scale (function to
                            automatically adjust the value of the reference graticule and the scale per
                            division to display t he trace appropriately).
                        """
                        self.__instr_obj.write(f"DISP:WIND{self.__channel}:TRAC{self.__trace}:Y:AUTO")

        @property
        def enable(self) -> int:
            self.__instr_obj.write(f":DISP:ENAB?")  
        
        @enable.setter
        def enable(self, state:str="on"):
            self.__instr_obj.write(f":DISP:ENAB {state}")

    class Format():
        def __init__(self, instrobj):
            self.__instr_obj = instrobj
            self.__channel = None
            self.__trace = None
            self.__marker = None
            self.__port = None
            self.__parameter = None
            self.__standard = None
            self.__cal_kit = None

        def _set_channel(self, channel):
            self.__channel = channel

        def _set_trace(self, trace):
            self.__trace = trace

        def _set_marker(self, marker):
            self.__marker = marker
        
        def _set_port(self, port):
            self.__port = port
        
        def _set_parameter(self, parameter):
            self.__parameter = parameter
        
        def _set_standard(self, standard):
            self.__standard = standard
        
        def _set_cal_kit(self, kit):
            self.__cal_kit = kit

    class HardCopy():
        def __init__(self, instrobj):
            self.__instr_obj = instrobj
            self.__channel = None
            self.__trace = None
            self.__marker = None
            self.__port = None
            self.__parameter = None
            self.__standard = None
            self.__cal_kit = None

        def _set_channel(self, channel):
            self.__channel = channel

        def _set_trace(self, trace):
            self.__trace = trace
        
        def _set_marker(self, marker):
            self.__marker = marker
        
        def _set_port(self, port):
            self.__port = port
        
        def _set_parameter(self, parameter):
            self.__parameter = parameter
        
        def _set_standard(self, standard):
            self.__standard = standard
        
        def _set_cal_kit(self, kit):
            self.__cal_kit = kit
    
    class Initiate():
        def __init__(self, instrobj):
            self.__instr_obj = instrobj
            self.__channel = None
            self.__trace = None
            self.__marker = None
            self.__port = None
            self.__parameter = None
            self.__standard = None
            self.__cal_kit = None

        def _set_channel(self, channel):
            self.__channel = channel

        def _set_trace(self, trace):
            self.__trace = trace

        def _set_marker(self, marker):
            self.__marker = marker
        
        def _set_port(self, port):
            self.__port = port
        
        def _set_parameter(self, parameter):
            self.__parameter = parameter
        
        def _set_standard(self, standard):
            self.__standard = standard
        
        def _set_cal_kit(self, kit):
            self.__cal_kit = kit

    class Mmemory():
        def __init__(self, instrobj):
            self.__instr_obj = instrobj
            self.__channel = None
            self.__trace = None
            self.__marker = None
            self.__port = None
            self.__parameter = None
            self.__standard = None
            self.__cal_kit = None

        def _set_channel(self, channel):
            self.__channel = channel

        def _set_trace(self, trace):
            self.__trace = trace

        def _set_marker(self, marker):
            self.__marker = marker
        
        def _set_port(self, port):
            self.__port = port
        
        def _set_parameter(self, parameter):
            self.__parameter = parameter
        
        def _set_standard(self, standard):
            self.__standard = standard
        
        def _set_cal_kit(self, kit):
            self.__cal_kit = kit
        
    @property
    def output(self):
        return "y"
    
    @output.setter
    def output(self, state):
        val = 1

    class Sense():
        def __init__(self, instrobj):
            self.__instr_obj = instrobj
            self.__channel = None
            self.__trace = None
            self.__marker = None
            self.__port = None
            self.__parameter = None
            self.__standard = None
            self.__cal_kit = None

            self.correction = self.Correction(self.__instr_obj)
            self.frequency  = self.Frequency(self.__instr_obj)
            self.sweep      = self.Sweep(self.__instr_obj)

        def _set_channel(self, channel):
            self.__channel = channel
            self.correction._set_channel(self.__channel)
            self.frequency._set_channel(self.__channel)
            self.sweep._set_channel(self.__channel)

        def _set_trace(self, trace):
            self.__trace = trace
            self.correction._set_trace(self.__trace)
            self.frequency._set_trace(self.__trace)

        def _set_marker(self, marker):
            self.__marker = marker
            self.correction._set_marker(self.__marker)
            self.frequency._set_marker(self.__marker)
        
        def _set_port(self, port):
            self.__port = port
            self.correction._set_port(self.__port)
            self.frequency._set_port(self.__port)
        
        def _set_parameter(self, parameter):
            self.__parameter = parameter
            self.correction._set_parameter(self.__parameter)
            self.frequency._set_parameter(self.__parameter)
        
        def _set_standard(self, standard):
            self.__standard = standard
            self.correction._set_standard(self.__standard)
            self.frequency._set_standard(self.__parameter)
        
        def _set_cal_kit(self, kit):
            self.__cal_kit = kit
            self.correction._set_cal_kit(self.__cal_kit)
            self.frequency._set_cal_kit(self.__cal_kit)
        
        class Correction():
            def __init__(self, instrobj):
                self.__instr_obj = instrobj
                self.__channel = None
                self.__trace = None
                self.__marker = None
                self.__port = None
                self.__parameter = None
                self.__standard = None
                self.__cal_kit = None

                self.collection = self.Collection(self.__instr_obj)
                self.extension   = self.Extension(self.__instr_obj)
                self.impedance  = self.Impedance(self.__instr_obj)
                self.offset     = self.Offset(self.__instr_obj)
                self.port       = self.Port(self.__instr_obj)
                self.receiver   = self.Receiver(self.__instr_obj)
                self.transform  = self.Transform(self.__instr_obj)
                self.trigger    = self.Trigger(self.__instr_obj)
                self.vmc        = self.VMC(self.__instr_obj)
                
            def _set_channel(self, channel):
                self.__channel = channel
                self.collection._set_channel(self.__channel)
                self.extension._set_channel(self.__channel)

            def _set_trace(self, trace):
                self.__trace = trace
                self.collection._set_trace(self.__trace)
                self.extension._set_trace(self.__trace)

            def _set_marker(self, marker):
                self.__marker = marker
                self.collection._set_marker(self.__marker)
                self.extension._set_marker(self.__marker)
            
            def _set_port(self, port):
                self.__port = port
                self.collection._set_port(self.__port)
                self.extension._set_port(self.__port)
            
            def _set_parameter(self, parameter):
                self.__parameter = parameter
                self.collection._set_parameter(self.__parameter)
                self.extension._set_parameter(self.__parameter)
            
            def _set_standard(self, standard):
                self.__standard = standard
                self.collection._set_standard(self.__standard)
                self.extension._set_standard(self.__standard)
            
            def _set_cal_kit(self, kit):
                self.__cal_kit = kit
                self.collection._set_cal_kit(self.__cal_kit)
                self.extension._set_cal_kit(self.__cal_kit)
            
            @property
            def characteristic_impedance(self) -> float:
                """This command gets the system characteristic impedance (Z0) value

                Returns:
                    float: _description_
                """
                return self.__instr_obj.query(f":SENS{self.__channel}:CORR:IMP?")
            
            @characteristic_impedance.setter
            def characteristic_impedance(self, value:float=50.0):
                """This command sets the system characteristic impedance (Z0) value

                Args:
                    value (float, optional): The characteristic impedance value. Defaults to 50.0.
                """
                self.__instr_obj.write(f":SENS{self.__channel}:CORR:IMP {value}")
            
            @property
            def state(self):
                """Queries the measurement calibration state.

                Args:
                    state (int, optional): 0 for OFF; 1 for ON. Defaults to 0.
                """
                self.__instr_obj.write(f":SENS{self.__channel}:CORR:STAT?")

            @state.setter
            def state(self, state:int=0):
                """Enables or disables the measurement calibration state.

                Args:
                    state (int, optional): 0 for OFF; 1 for ON. Defaults to 0.
                """
                self.__instr_obj.write(f":SENS{self.__channel}:CORR:STAT {state}")
            
            
            class Collection():
                def __init__(self, instrobj):
                    self.__instr_obj = instrobj
                    self.__channel = None
                    self.__trace = None
                    self.__marker = None
                    self.__port = None
                    self.__parameter = None
                    self.__standard = None
                    self.__cal_kit = None

                    self.calkit     = self.CalKit(self.__instr_obj)

                def _set_channel(self, channel):
                    self.__channel = channel
                    self.calkit._set_channel(self.__channel)

                def _set_trace(self, trace):
                    self.__trace = trace
                    self.calkit._set_trace(self.__trace)

                def _set_marker(self, marker):
                    self.__marker = marker
                    self.calkit._set_marker(self.__marker)
                
                def _set_port(self, port):
                    self.__port = port
                    self.calkit._set_port(self.__port)
                
                def _set_parameter(self, parameter):
                    self.__parameter = parameter
                    self.calkit._set_parameter(self.__parameter)
                
                def _set_standard(self, standard):
                    self.__standard = standard
                    self.calkit._set_standard(self.__standard)
                
                def _set_cal_kit(self, kit):
                    self.__cal_kit = kit
                    self.calkit._set_cal_kit(self.__cal_kit)

                def calibrate_load(self, port:int=1):
                    """Measures the calibration data of the load standard for the specified port.

                    Args:
                        port (int, optional): The number of port 1 to 4 (model dependent). Defaults to 1.
                    """
                    self.__instr_obj.write(f"SENS{self.__channel}:CORR:COLL:LOAD {port}")

                def calibrate_open(self, port:int=1):
                    """Measures the calibration data of the open standard for the specified port.

                    Args:
                        port (int, optional): The number of port 1 to 4 (model dependent). Defaults to 1.
                    """
                    self.__instr_obj.write(f"SENS{self.__channel}:CORR:COLL:OPEN {port}")
                
                def calibrate_save(self):
                    """From the measured calibration data, calculates the calibration coefficients
                    depending on the selected calibration type.
                    """
                    self.__instr_obj.write(f":SENS{self.__channel}:CORR:COLL:SAVE")
                
                def calibrate_short(self, port:int=1):
                    """Measures the calibration data of the short standard for the specified port.

                    Args:
                        port (int, optional): The number of port 1 to 4 (model dependent). Defaults to 1.
                    """
                    self.__instr_obj.write(f":SENS{self.__channel}:CORR:COLL:SHOR {port}")

                def calibrate_through(self, porta:int=1, portb:int=2):
                    """Measures the calibration data of the through standard for the specified port.

                    Args:
                        port (int, optional): The number of port 1 to 4 (model dependent). Defaults to 1.
                    """
                    self.__instr_obj.write(f":SENS{self.__channel}:CORR:COLL:THRU {porta},{portb}")

                def method(self, method:str='open', porta:int=1, portb:int=2, portc:int=3, portd:int=4):
                    """Sets the calibration method to be applied upon successful calibration measurements.

                    Args:
                        method (int, optional): Use "eres" for 2-port enhanced response;\n
                        "open" for Open;\n
                        "short" for Short;\n
                        "thru" for Thru;\n
                        "1port" for 1-port SOLT;\n
                        "2port" for 2-port SOLT;\n
                        "3port" for 3-port SOLT;\n
                        "4port for 4-port  SOLT.\n
                        Defaults to 1.
                        porta (int, optional): The first port used in during calibration. Defaults to 1.
                        portb (int, optional): The second port used in during calibration. Defaults to 2.
                        portc (int, optional): The third port used in during calibration. Defaults to 3.
                        portd (int, optional): The fourth port used in during calibration. Defaults to 4.
                    """
                    method_dict = {"eres": "ERES",
                                   "open": "OPEN",
                                   "short": "SHORT",
                                   "thru": "THRU",
                                   "1port": "SOLT1",
                                   "2port": "SOLT2",
                                   "3port": "SOLT3",
                                   "4port": "SOLT4",
                                   }
                    
                    if (method == "thru") or (method == "2port") or (method == "eres"):
                        self.__instr_obj.write(f"SENS{self.__channel}:CORR:COLL:METH:{method_dict[method]} {porta},{portb}")
                    elif method == "3port":
                        self.__instr_obj.write(f"SENS{self.__channel}:CORR:COLL:METH:{method_dict[method]} {porta},{portb},{portc}")
                    elif method == "4port":
                        self.__instr_obj.write(f"SENS{self.__channel}:CORR:COLL:METH:{method_dict[method]} {porta},{portb},{portc},{portd}")
                    else:
                        self.__instr_obj.write(f"SENS{self.__channel}:CORR:COLL:METH:{method_dict[method]} {porta}")

                class CalKit():
                    def __init__(self, instrobj):
                        self.__instr_obj = instrobj
                        self.__channel = None
                        self.__trace = None
                        self.__marker = None
                        self.__port = None
                        self.__parameter = None
                        self.__standard = None
                        self.__cal_kit = None

                    def _set_channel(self, channel):
                        self.__channel = channel

                    def _set_trace(self, trace):
                        self.__trace = trace

                    def _set_marker(self, marker):
                        self.__marker = marker
                    
                    def _set_port(self, port):
                        self.__port = port
                    
                    def _set_parameter(self, parameter):
                        self.__parameter = parameter
                    
                    def _set_standard(self, standard):
                        self.__standard = standard
                    
                    def _set_cal_kit(self, kit):
                        self.__cal_kit = kit

                    @property
                    def select(self) -> int:
                        """Reports the number of the selected calibration kit in the table
                        of calibration kits. The selected calibration kit is used in the subsequent
                        calibration and is used for editing by the commands SENS:CORR:COLL:CKIT:XXXX.

                        Returns:
                            int: Value associated with a defined calibration kit. 
                        """
                        return self.__instr_obj.query(f":SENS{self.__channel}:CORR:COLL:CKIT?")
                    
                    @select.setter
                    def select(self, kit_number:int=31):
                        """Sets the number of the selected calibration kit in the table
                        of calibration kits. The selected calibration kit is used in the subsequent
                        calibration and is used for editing by the commands SENS:CORR:COLL:CKIT:XXXX.

                        Args:
                            kit_number (int, optional): Value associated with a defined calibration
                            kit. Defaults to 31, 'SK-CAL-NSet-90'.
                        """
                        self.__instr_obj.write(f":SENS{self.__channel}:CORR:COLL:CKIT {kit_number}")

            class Extension():
                def __init__(self, instrobj):
                    self.__instr_obj = instrobj
                    self.__channel = None
                    self.__trace = None
                    self.__marker = None
                    self.__port = None
                    self.__parameter = None
                    self.__standard = None
                    self.__cal_kit = None

                    self.auto   = self.Auto(self.__instr_obj)
                    self.port   = self.Port(self.__instr_obj)

                def _set_channel(self, channel):
                    self.__channel = channel
                    self.auto._set_channel(self.__channel)
                    self.port._set_channel(self.__channel)

                def _set_trace(self, trace):
                    self.__trace = trace
                    self.auto._set_trace(self.__trace)
                    self.port._set_trace(self.__trace)

                def _set_marker(self, marker):
                    self.__marker = marker
                    self.auto._set_marker(self.__marker)
                    self.port._set_marker(self.__marker)
                
                def _set_port(self, port):
                    self.__port = port
                    self.auto._set_port(self.__port)
                    self.port._set_port(self.__port)
                
                def _set_parameter(self, parameter):
                    self.__parameter = parameter
                    self.auto._set_parameter(self.__parameter)
                    self.port._set_parameter(self.__parameter)
                
                def _set_standard(self, standard):
                    self.__standard = standard
                    self.auto._set_standard(self.__standard)
                    self.port._set_standard(self.__standard)
                
                def _set_cal_kit(self, kit):
                    self.__cal_kit = kit
                    self.auto._set_cal_kit(self.__cal_kit)
                    self.port._set_cal_kit(self.__cal_kit)

                class Auto():
                    def __init__(self, instrobj):
                        self.__instr_obj = instrobj
                        self.__channel = None
                        self.__trace = None
                        self.__marker = None
                        self.__port = None
                        self.__parameter = None
                        self.__standard = None
                        self.__cal_kit = None

                    def _set_channel(self, channel):
                        self.__channel = channel
                        
                    def _set_trace(self, trace):
                        self.__trace = trace

                    def _set_marker(self, marker):
                        self.__marker = marker
                    
                    def _set_port(self, port):
                        self.__port = port
                    
                    def _set_parameter(self, parameter):
                        self.__parameter = parameter
                    
                    def _set_standard(self, standard):
                        self.__standard = standard
                    
                    def _set_cal_kit(self, kit):
                        self.__cal_kit = kit
                    
                    def measure(self, meastype:str="open"):
                        """Performs the port extention auto measurement for the 

                        Args:
                            meastype (str, optional): _description_. Defaults to "open".
                        """
                        self.__instr_obj.write(f":SENS{self.__channel}:CORR:EXT:AUTO:MEAS {meastype.upper()}")

                    @property
                    def port(self) -> str:
                        """Indicates whether the port is enabled for the port extension measurement (ON|1), or disabled (OFF|0).

                        Returns:
                            str: Enabled (ON|1), or disabled (OFF|0).
                        """
                        self.__instr_obj.write(f":SENS{self.__channel}:CORR:EXT:AUTO:PORT{self.__port}?")

                    @port.setter
                    def port(self, state:str="off"):
                        """Sets the port is enabled for the port extension measurement (ON|1), or disabled (OFF|0).

                        Args:
                            state (str, optional): Pass "on" to enable or "off" to disable. Defaults to "off".
                        """
                        self.__instr_obj.write(f":SENS{self.__channel}:CORR:EXT:AUTO:PORT{self.__port} {state.upper()}")

                class Port():
                    def __init__(self, instrobj):
                        self.__instr_obj = instrobj
                        self.__channel = None
                        self.__trace = None
                        self.__marker = None
                        self.__port = None
                        self.__parameter = None
                        self.__standard = None
                        self.__cal_kit = None

                    def _set_channel(self, channel):
                        self.__channel = channel

                    def _set_trace(self, trace):
                        self.__trace = trace

                    def _set_marker(self, marker):
                        self.__marker = marker
                    
                    def _set_port(self, port):
                        self.__port = port
                    
                    def _set_parameter(self, parameter):
                        self.__parameter = parameter
                    
                    def _set_standard(self, standard):
                        self.__standard = standard
                    
                    def _set_cal_kit(self, kit):
                        self.__cal_kit = kit

            class Impedance():
                def __init__(self, instrobj):
                    self.__instr_obj = instrobj
                    self.__channel = None
                    self.__trace = None
                    self.__marker = None
                    self.__port = None
                    self.__parameter = None
                    self.__standard = None
                    self.__cal_kit = None

                    #self.auto   = self.Auto(self.__instr_obj)
                    #self.port   = self.Port(self.__instr_obj)

                def _set_channel(self, channel):
                    self.__channel = channel
                    self.auto._set_channel(self.__channel)
                    self.port._set_channel(self.__channel)

                def _set_trace(self, trace):
                    self.__trace = trace
                    self.auto._set_trace(self.__trace)
                    self.port._set_trace(self.__trace)

                def _set_marker(self, marker):
                    self.__marker = marker
                    self.auto._set_marker(self.__marker)
                    self.port._set_marker(self.__marker)
                
                def _set_port(self, port):
                    self.__port = port
                    self.auto._set_port(self.__port)
                    self.port._set_port(self.__port)
                
                def _set_parameter(self, parameter):
                    self.__parameter = parameter
                    self.auto._set_parameter(self.__parameter)
                    self.port._set_parameter(self.__parameter)
                
                def _set_standard(self, standard):
                    self.__standard = standard
                    self.auto._set_standard(self.__standard)
                    self.port._set_standard(self.__standard)
                
                def _set_cal_kit(self, kit):
                    self.__cal_kit = kit
                    self.auto._set_cal_kit(self.__cal_kit)
                    self.port._set_cal_kit(self.__cal_kit)

            class Offset():
                def __init__(self, instrobj):
                    self.__instr_obj = instrobj
                    self.__channel = None
                    self.__trace = None
                    self.__marker = None
                    self.__port = None
                    self.__parameter = None
                    self.__standard = None
                    self.__cal_kit = None

                    #self.auto   = self.Auto(self.__instr_obj)
                    #self.port   = self.Port(self.__instr_obj)

                def _set_channel(self, channel):
                    self.__channel = channel
                    #self.auto._set_channel(self.__channel)
                    #self.port._set_channel(self.__channel)

                def _set_trace(self, trace):
                    self.__trace = trace
                    #self.auto._set_trace(self.__trace)
                    #self.port._set_trace(self.__trace)

                def _set_marker(self, marker):
                    self.__marker = marker
                    #self.auto._set_marker(self.__marker)
                    #self.port._set_marker(self.__marker)
                
                def _set_port(self, port):
                    self.__port = port
                    #self.auto._set_port(self.__port)
                    #self.port._set_port(self.__port)
                
                def _set_parameter(self, parameter):
                    self.__parameter = parameter
                    #self.auto._set_parameter(self.__parameter)
                    #self.port._set_parameter(self.__parameter)
                
                def _set_standard(self, standard):
                    self.__standard = standard
                    #self.auto._set_standard(self.__standard)
                    #self.port._set_standard(self.__standard)
                
                def _set_cal_kit(self, kit):
                    self.__cal_kit = kit
                    #self.auto._set_cal_kit(self.__cal_kit)
                    #self.port._set_cal_kit(self.__cal_kit)

            class Port():
                def __init__(self, instrobj):
                    self.__instr_obj = instrobj
                    self.__channel = None
                    self.__trace = None
                    self.__marker = None
                    self.__port = None
                    self.__parameter = None
                    self.__standard = None
                    self.__cal_kit = None

                    #self.auto   = self.Auto(self.__instr_obj)
                    #self.port   = self.Port(self.__instr_obj)

                def _set_channel(self, channel):
                    self.__channel = channel
                    #self.auto._set_channel(self.__channel)
                    #self.port._set_channel(self.__channel)

                def _set_trace(self, trace):
                    self.__trace = trace
                    #self.auto._set_trace(self.__trace)
                    #self.port._set_trace(self.__trace)

                def _set_marker(self, marker):
                    self.__marker = marker
                    #self.auto._set_marker(self.__marker)
                    #self.port._set_marker(self.__marker)
                
                def _set_port(self, port):
                    self.__port = port
                    #self.auto._set_port(self.__port)
                    #self.port._set_port(self.__port)
                
                def _set_parameter(self, parameter):
                    self.__parameter = parameter
                    #self.auto._set_parameter(self.__parameter)
                    #self.port._set_parameter(self.__parameter)
                
                def _set_standard(self, standard):
                    self.__standard = standard
                    #self.auto._set_standard(self.__standard)
                    #self.port._set_standard(self.__standard)
                
                def _set_cal_kit(self, kit):
                    self.__cal_kit = kit
                    #self.auto._set_cal_kit(self.__cal_kit)
                    #self.port._set_cal_kit(self.__cal_kit)

            class Receiver():
                def __init__(self, instrobj):
                    self.__instr_obj = instrobj
                    self.__channel = None
                    self.__trace = None
                    self.__marker = None
                    self.__port = None
                    self.__parameter = None
                    self.__standard = None
                    self.__cal_kit = None

                    #self.auto   = self.Auto(self.__instr_obj)
                    #self.port   = self.Port(self.__instr_obj)

                def _set_channel(self, channel):
                    self.__channel = channel
                    #self.auto._set_channel(self.__channel)
                    #self.port._set_channel(self.__channel)

                def _set_trace(self, trace):
                    self.__trace = trace
                    #self.auto._set_trace(self.__trace)
                    #self.port._set_trace(self.__trace)

                def _set_marker(self, marker):
                    self.__marker = marker
                    #self.auto._set_marker(self.__marker)
                    #self.port._set_marker(self.__marker)
                
                def _set_port(self, port):
                    self.__port = port
                    #self.auto._set_port(self.__port)
                    #self.port._set_port(self.__port)
                
                def _set_parameter(self, parameter):
                    self.__parameter = parameter
                    #self.auto._set_parameter(self.__parameter)
                    #self.port._set_parameter(self.__parameter)
                
                def _set_standard(self, standard):
                    self.__standard = standard
                    #self.auto._set_standard(self.__standard)
                    #self.port._set_standard(self.__standard)
                
                def _set_cal_kit(self, kit):
                    self.__cal_kit = kit
                    #self.auto._set_cal_kit(self.__cal_kit)
                    #self.port._set_cal_kit(self.__cal_kit)

            class Transform():
                def __init__(self, instrobj):
                    self.__instr_obj = instrobj
                    self.__channel = None
                    self.__trace = None
                    self.__marker = None
                    self.__port = None
                    self.__parameter = None
                    self.__standard = None
                    self.__cal_kit = None

                    #self.auto   = self.Auto(self.__instr_obj)
                    #self.port   = self.Port(self.__instr_obj)

                def _set_channel(self, channel):
                    self.__channel = channel
                    #self.auto._set_channel(self.__channel)
                    #self.port._set_channel(self.__channel)

                def _set_trace(self, trace):
                    self.__trace = trace
                    #self.auto._set_trace(self.__trace)
                    #self.port._set_trace(self.__trace)

                def _set_marker(self, marker):
                    self.__marker = marker
                    #self.auto._set_marker(self.__marker)
                    #self.port._set_marker(self.__marker)
                
                def _set_port(self, port):
                    self.__port = port
                    #self.auto._set_port(self.__port)
                    #self.port._set_port(self.__port)
                
                def _set_parameter(self, parameter):
                    self.__parameter = parameter
                    #self.auto._set_parameter(self.__parameter)
                    #self.port._set_parameter(self.__parameter)
                
                def _set_standard(self, standard):
                    self.__standard = standard
                    #self.auto._set_standard(self.__standard)
                    #self.port._set_standard(self.__standard)
                
                def _set_cal_kit(self, kit):
                    self.__cal_kit = kit
                    #self.auto._set_cal_kit(self.__cal_kit)
                    #self.port._set_cal_kit(self.__cal_kit)

            class Trigger():
                def __init__(self, instrobj):
                    self.__instr_obj = instrobj
                    self.__channel = None
                    self.__trace = None
                    self.__marker = None
                    self.__port = None
                    self.__parameter = None
                    self.__standard = None
                    self.__cal_kit = None

                    #self.auto   = self.Auto(self.__instr_obj)
                    #self.port   = self.Port(self.__instr_obj)

                def _set_channel(self, channel):
                    self.__channel = channel
                    #self.auto._set_channel(self.__channel)
                    #self.port._set_channel(self.__channel)

                def _set_trace(self, trace):
                    self.__trace = trace
                    #self.auto._set_trace(self.__trace)
                    #self.port._set_trace(self.__trace)

                def _set_marker(self, marker):
                    self.__marker = marker
                    #self.auto._set_marker(self.__marker)
                    #self.port._set_marker(self.__marker)
                
                def _set_port(self, port):
                    self.__port = port
                    #self.auto._set_port(self.__port)
                    #self.port._set_port(self.__port)
                
                def _set_parameter(self, parameter):
                    self.__parameter = parameter
                    #self.auto._set_parameter(self.__parameter)
                    #self.port._set_parameter(self.__parameter)
                
                def _set_standard(self, standard):
                    self.__standard = standard
                    #self.auto._set_standard(self.__standard)
                    #self.port._set_standard(self.__standard)
                
                def _set_cal_kit(self, kit):
                    self.__cal_kit = kit
                    #self.auto._set_cal_kit(self.__cal_kit)
                    #self.port._set_cal_kit(self.__cal_kit)

            class VMC():
                def __init__(self, instrobj):
                    self.__instr_obj = instrobj
                    self.__channel = None
                    self.__trace = None
                    self.__marker = None
                    self.__port = None
                    self.__parameter = None
                    self.__standard = None
                    self.__cal_kit = None

                    #self.auto   = self.Auto(self.__instr_obj)
                    #self.port   = self.Port(self.__instr_obj)

                def _set_channel(self, channel):
                    self.__channel = channel
                    #self.auto._set_channel(self.__channel)
                    #self.port._set_channel(self.__channel)

                def _set_trace(self, trace):
                    self.__trace = trace
                    #self.auto._set_trace(self.__trace)
                    #self.port._set_trace(self.__trace)

                def _set_marker(self, marker):
                    self.__marker = marker
                    #self.auto._set_marker(self.__marker)
                    #self.port._set_marker(self.__marker)
                
                def _set_port(self, port):
                    self.__port = port
                    #self.auto._set_port(self.__port)
                    #self.port._set_port(self.__port)
                
                def _set_parameter(self, parameter):
                    self.__parameter = parameter
                    #self.auto._set_parameter(self.__parameter)
                    #self.port._set_parameter(self.__parameter)
                
                def _set_standard(self, standard):
                    self.__standard = standard
                    #self.auto._set_standard(self.__standard)
                    #self.port._set_standard(self.__standard)
                
                def _set_cal_kit(self, kit):
                    self.__cal_kit = kit
                    #self.auto._set_cal_kit(self.__cal_kit)
                    #self.port._set_cal_kit(self.__cal_kit)

        class Frequency():
            """The frequency menu of commands is inclusive of the following:
                * center
                * data?
                * frequency
                * span
                * start
                * stop
            """
            def __init__(self, instrobj):
                self.__instr_obj = instrobj
                self.__channel = None
                self.__trace = None
                self.__marker = None
                self.__port = None
                self.__parameter = None
                self.__standard = None
                self.__cal_kit = None

            def _set_channel(self, channel):
                self.__channel = channel

            def _set_trace(self, trace):
                self.__trace = trace

            def _set_marker(self, marker):
                self.__marker = marker
            
            def _set_port(self, port):
                self.__port = port
            
            def _set_parameter(self, parameter):
                self.__parameter = parameter
            
            def _set_standard(self, standard):
                self.__standard = standard
            
            def _set_cal_kit(self, kit):
                self.__cal_kit = kit

            @property
            def frequency(self):
                """Reads out the fixed frequency value when the power sweep type selected.

                Returns:
                    float: The frequency value within the frequency limits of the analyzer.
                """
                return float(self.__instr_obj.query(f"SENS{self.__channel}:FREQ?").rstrip())
            
            @frequency.setter
            def frequency(self, value:float):
                """Sets the fixed frequency value when the power sweep type selected.

                Args:
                    value (float): The frequency value within the frequency limits of the analyzer.
                """
                self.__instr_obj.write(f"SENS{self.__channel}:FREQ {value}")
            
            @property
            def data(self) -> list[int]:
                """ Reads out the frequency array of the measurement points.
                    The array size is N, where N is the number of measurement points.
                    For the n–th point, where n from 1 to N:
                    <numeric n> the frequency value at the n–th measurement point

                Returns:
                    list[int]: <numeric 1>, <numeric 2>, …<numeric N>
                """
                mystr = self.__instr_obj.query(f":SENS{self.__channel}:FREQ:DATA?").rstrip()
                my_list = mystr.split(',')
                return my_list
            
            @property
            def center(self) -> float:
                """Gets/Sets the center value of the sweep range of a select channel.

                Returns:
                    float: The center frequency in Hertz (Hz).
                """
                return float(self.__instr_obj.query(f":SENS{self.__channel}:FREQ:CENT?").rstrip())
            
            @center.setter
            def center(self, frequency:float):
                """Sets the center value of the sweep range of a select channel.

                Args:
                    frequency (float): The center frequency in Hertz (Hz).
                """
                self.__instr_obj.write(f":SENS{self.__channel}:FREQ:CENT {frequency}")

            @property
            def span(self) -> float:
                """Reads out the stimulus span value of the sweep range for linear or logarithmic sweep type.

                Returns:
                    float: The frequency span in Hertz (Hz).
                """
                return float(self.__instr_obj.query(f":SENS{self.__channel}:FREQ:SPAN?").rstrip())
            
            @span.setter
            def span(self, frequency:float):
                """Sets the stimulus span value of the sweep range for linear or logarithmic sweep type.

                Args:
                    frequency (float): The frequency span in Hertz (Hz).
                """
                self.__instr_obj.write(f"SENS{self.__channel}:FREQ:SPAN {frequency}")

            @property
            def start(self) -> float:
                """Gets the start value of the sweep range of a select channel.

                Returns:
                    float: The start frequency in Hertz (Hz).
                """
                return float(self.__instr_obj.query(f"SENS{self.__channel}:FREQ:STAR?").rstrip())
            
            @start.setter
            def start(self, frequency:float):
                """Sets the start value of the sweep range of a select channel.

                Args:
                    frequency (_type_): The start frequency in Hertz (Hz).
                """
                self.__instr_obj.write(f"SENS{self.__channel}:FREQ:STAR {frequency}")

            @property
            def stop(self) -> float:
                """Reads out the stimulus stop value of the sweep range for linear or logarithmic sweep type.

                Returns:
                    float: _description_
                """
                return float(self.__instr_obj.query(f"SENS{self.__channel}:FREQ:STOP?").rstrip())
            
            @stop.setter
            def stop(self, frequency:float):
                """Sets the stimulus stop value of the sweep range for linear or logarithmic sweep type.

                Args:
                    frequency (float): _description_
                """
                self.__instr_obj.write(f"SENS{self.__channel}:FREQ:STOP {frequency}")

        class Sweep():
            def __init__(self, instrobj):
                self.__instr_obj = instrobj
                self.__channel = None
                self.__trace = None
                self.__marker = None
                self.__port = None
                self.__parameter = None
                self.__standard = None
                self.__cal_kit = None

            def _set_channel(self, channel):
                self.__channel = channel

            def _set_trace(self, trace):
                self.__trace = trace

            def _set_marker(self, marker):
                self.__marker = marker
            
            def _set_port(self, port):
                self.__port = port
            
            def _set_parameter(self, parameter):
                self.__parameter = parameter
            
            def _set_standard(self, standard):
                self.__standard = standard
            
            def _set_cal_kit(self, kit):
                self.__cal_kit = kit 

            @property
            def points(self) -> int:
                """Reads out the number of measurement points.

                Returns:
                    int: Number of measurement points.
                """
                return int(self.__instr_obj.query(f":SENS{self.__channel}:SWE:POIN?").rstrip())

            @points.setter
            def points(self, count:int):
                """Sets the number of measurement points.

                Args:
                    count (int): Number of measurement points. 
                """
                self.__instr_obj.write(f":SENS{self.__channel}:SWE:POIN {count}")  

            @property
            def point_time(self) -> float:
                """Reads out the delay before measurement in each measurement point.

                Returns:
                    float: Time before each measurement point.
                """
                return float(self.__instr_obj.query(f"SENS{self.__channel}:SWE:POIN:TIME?").rstrip())

            @point_time.setter
            def point_time(self, time:float):
                """Sets the delay before measurement in each measurement point.

                Args:
                    time (float): Time before each measurement point.
                """
                self.__instr_obj.write(f"SENS{self.__channel}:SWE:POIN:TIME {time}")  

    class Service():
        def __init__(self, instrobj):
            self.__instr_obj = instrobj
            self.__channel = None
            self.__trace = None
            self.__marker = None
            self.__port = None
            self.__parameter = None
            self.__standard = None
            self.__cal_kit = None

        def _set_channel(self, channel):
            self.__channel = channel

        def _set_trace(self, trace):
            self.__trace = trace

        def _set_marker(self, marker):
            self.__marker = marker
        
        def _set_port(self, port):
            self.__port = port
        
        def _set_parameter(self, parameter):
            self.__parameter = parameter
        
        def _set_standard(self, standard):
            self.__standard = standard
        
        def _set_cal_kit(self, kit):
            self.__cal_kit = kit

    class Source():
        def __init__(self, instrobj):
            self.__instr_obj = instrobj
            self.__channel = None
            self.__trace = None
            self.__marker = None
            self.__port = None
            self.__parameter = None
            self.__standard = None
            self.__cal_kit = None

        def _set_channel(self, channel):
            self.__channel = channel

        def _set_trace(self, trace):
            self.__trace = trace    

        def _set_marker(self, marker):
            self.__marker = marker
        
        def _set_port(self, port):
            self.__port = port
        
        def _set_parameter(self, parameter):
            self.__parameter = parameter
        
        def _set_standard(self, standard):
            self.__standard = standard
        
        def _set_cal_kit(self, kit):
            self.__cal_kit = kit

    class Status():
        def __init__(self, instrobj):
            self.__instr_obj = instrobj
            self.__channel = None
            self.__trace = None
            self.__marker = None
            self.__port = None
            self.__parameter = None
            self.__standard = None
            self.__cal_kit = None

        def _set_channel(self, channel):
            self.__channel = channel

        def _set_trace(self, trace):
            self.__trace = trace 

        def _set_marker(self, marker):
            self.__marker = marker
        
        def _set_port(self, port):
            self.__port = port
        
        def _set_parameter(self, parameter):
            self.__parameter = parameter
        
        def _set_standard(self, standard):
            self.__standard = standard
        
        def _set_cal_kit(self, kit):
            self.__cal_kit = kit

    class System():
        def __init__(self, instrobj):
            self.__instr_obj = instrobj
            self.__channel = None
            self.__trace = None
            self.__marker = None
            self.__port = None
            self.__parameter = None
            self.__standard = None
            self.__cal_kit = None

        def _set_channel(self, channel):
            self.__channel = channel

        def _set_trace(self, trace):
            self.__trace = trace   

        def _set_marker(self, marker):
            self.__marker = marker
        
        def _set_port(self, port):
            self.__port = port
        
        def _set_parameter(self, parameter):
            self.__parameter = parameter
        
        def _set_standard(self, standard):
            self.__standard = standard
        
        def _set_cal_kit(self, kit):
            self.__cal_kit = kit

        def preset(self):
            """
            Resets the network analyzer to the factory settings.
            """
            self.__instr_obj.write("SYST:PRES\n")

    class Trigger():
        def __init__(self, instrobj):
            self.__instr_obj = instrobj
            self.__channel = None
            self.__trace = None
            self.__marker = None
            self.__port = None
            self.__parameter = None
            self.__standard = None
            self.__cal_kit = None

        def _set_channel(self, channel):
            self.__channel = channel

        def _set_trace(self, trace):
            self.__trace = trace  
        
        def _set_marker(self, marker):
            self.__marker = marker
        
        def _set_port(self, port):
            self.__port = port
        
        def _set_parameter(self, parameter):
            self.__parameter = parameter
        
        def _set_standard(self, standard):
            self.__standard = standard
        
        def _set_cal_kit(self, kit):
            self.__cal_kit = kit
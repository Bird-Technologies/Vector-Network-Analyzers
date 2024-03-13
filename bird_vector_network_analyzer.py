"""temp docstring"""
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
            self.fixturesimulate= self.FixtureSimulate(self.__instr_obj)
            self.function       = self.Function(self.__instr_obj)
            self.hold           = self.Hold(self, self.__instr_obj)
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
                self.electrical_delay._set_channel(self._set__channel)
            
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
        def format(self):
            return 0
        
        @format.setter
        def format(self, format):
            val = format

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

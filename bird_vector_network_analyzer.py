"""temp docstring"""
import pyvisa as visa


class BirdVectorNetworkAnalyzer():
    """
    This is a driver. 
    """
    def __init__(self):
        self.resource_manager = None
        self._instr_obj = None
        self._channel = None
        self._trace = None
        self._port = None
        self._marker = None
        self._parameter = None
        self._standard = None
        self._cal_kit = None

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
            if self.resource_manager is None:
                self.resource_manager = visa.ResourceManager()
        except visa.VisaIOError as visaerror:
            print(f"{visaerror}")
        except visa.VisaIOWarning as visawarning:
            print(f"{visawarning}")

    def initialize(self, instrument_resource_string, *args):
        """
        Temporary, provisional docstring
        """
        try:
            #self.instrument_object = self.resource_manager.open_resource(
                #instrument_resource_string)
            
            self.calculate = self.Calculate(self._instr_obj)
            self.display = self.Display(self._instr_obj)
            self.format = self.Format(self._instr_obj)
            self.hardcopy = self.HardCopy(self._instr_obj)
            self.mmemory = self.Mmemory(self._instr_obj)
            self.sense = self.Sense(self._instr_obj)
            self.service = self.Service(self._instr_obj)
            self.source = self.Source(self._instr_obj)
            self.status = self.Status(self._instr_obj)
            self.system = self.System(self._instr_obj)
            self.trigger = self.Trigger(self._instr_obj)

        except visa.VisaIOError as visaerr:
            print(f"{visaerr}")
        return

    def close(self):
        """
        Temporary, provisional docstring
        """
        try:
            self.instrument_object.close()
        except visa.VisaIOError as visaerr:
            print(f"{visaerr}")
        return

    def write(self, command:str=None):
        """
        Temporary, provisional docstring
        """
        try:
            self.instrument_object.write(command)
        except visa.VisaIOError as visaerr:
            print(f"{visaerr}")
        return

    def query(self, command):
        """
        Temporary, provisional docstring
        """
        response = ""
        try:
            response = self.instrument_object.query(command).rstrip()
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
        return self._cal_kit
    
    @cal_kit.setter
    def cal_kit(self, kit_number):
        self._cal_kit = kit_number
        self.calculate._set_cal_kit(self._cal_kit)
        self.display._set_cal_kit(self._cal_kit)
        self.format._set_cal_kit(self._cal_kit)
        self.hardcopy._set_cal_kit(self._cal_kit)
        self.mmemory._set_cal_kit(self._cal_kit)
        self.sense._set_cal_kit(self._cal_kit)
        self.service._set_cal_kit(self._cal_kit)
        self.source._set_cal_kit(self._cal_kit)
        self.status._set_cal_kit(self._cal_kit)
        self.system._set_cal_kit(self._cal_kit)
        self.trigger._set_cal_kit(self._cal_kit)

    @property
    def channel(self):
        return self._channel
    
    @channel.setter
    def channel(self, channel):
        self._channel = channel
        self.calculate._set_channel(self._channel)
        self.display._set_channel(self._channel)
        self.format._set_channel(self._channel)
        self.hardcopy._set_channel(self._channel)
        self.mmemory._set_channel(self._channel)
        self.sense._set_channel(self._channel)
        self.service._set_channel(self._channel)
        self.source._set_channel(self._channel)
        self.status._set_channel(self._channel)
        self.system._set_channel(self._channel)
        self.trigger._set_channel(self._channel)
    
    @property
    def marker(self):
        return self._marker
    
    @marker.setter
    def marker(self, marker):
        self._marker = marker
        self.calculate._set_marker(self._marker)
        self.display._set_marker(self._marker)
        self.format._set_marker(self._marker)
        self.hardcopy._set_marker(self._marker)
        self.mmemory._set_marker(self._marker)
        self.sense._set_marker(self._marker)
        self.service._set_marker(self._marker)
        self.source._set_marker(self._marker)
        self.status._set_marker(self._marker)
        self.system._set_marker(self._marker)
        self.trigger._set_marker(self._marker)

    @property
    def parameter(self):
        return self._parameter
    
    @parameter.setter
    def parameter(self, parameter):
        self._parameter = parameter
        self.calculate._set_parameter(self._parameter)
        self.display._set_parameter(self._parameter)
        self.format._set_parameter(self._parameter)
        self.hardcopy._set_parameter(self._parameter)
        self.mmemory._set_parameter(self._parameter)
        self.sense._set_parameter(self._parameter)
        self.service._set_parameter(self._parameter)
        self.source._set_parameter(self._parameter)
        self.status._set_parameter(self._parameter)
        self.system._set_parameter(self._parameter)
        self.trigger._set_parameter(self._parameter)

    @property
    def port(self):
        return self._port
    
    @port.setter
    def port(self, port):
        self._port = port
        self.calculate._set_port(self._port)
        self.display._set_port(self._port)
        self.format._set_port(self._port)
        self.hardcopy._set_port(self._port)
        self.mmemory._set_port(self._port)
        self.sense._set_port(self._port)
        self.service._set_port(self._port)
        self.source._set_port(self._port)
        self.status._set_port(self._port)
        self.system._set_port(self._port)
        self.trigger._set_port(self._port)
    
    @property
    def standard(self):
        return self._standard
    
    @standard.setter
    def standard(self, standard):
        self._standard = standard
        self.calculate._set_standard(self._standard)
        self.display._set_standard(self._standard)
        self.format._set_standard(self._standard)
        self.hardcopy._set_standard(self._standard)
        self.mmemory._set_standard(self._standard)
        self.sense._set_standard(self._standard)
        self.service._set_standard(self._standard)
        self.source._set_standard(self._standard)
        self.status._set_standard(self._standard)
        self.system._set_standard(self._standard)
        self.trigger._set_standard(self._standard)

    @property
    def trace(self):
        return self._trace 
    
    @trace.setter
    def trace(self, trace):
        self._trace = trace
        self.calculate._set_trace(self._trace)
        self.display._set_trace(self._trace)
        self.format._set_trace(self._trace)
        self.hardcopy._set_trace(self._trace)
        self.mmemory._set_trace(self._trace)
        self.sense._set_trace(self._trace)
        self.service._set_trace(self._trace)
        self.source._set_trace(self._trace)
        self.status._set_trace(self._trace)
        self.system._set_trace(self._trace)
        self.trigger._set_trace(self._trace)

    class Calculate():
        def __init__(self, instrobj):
            self._instr_obj = instrobj
            self._channel = None
            self._trace = None
            self._marker = None
            self._port = None
            self._parameter = None
            self._standard = None
            self._cal_kit = None

            self.conversion     = self.Conversion(self._instr_obj)
            self.data           = self.Data(self._instr_obj)
            self.fixturesimulate= self.FixtureSimulate(self._instr_obj)
            self.function       = self.Function(self._instr_obj)
            self.hold           = self.Hold(self, self._instr_obj)
            self.limit          = self.Limit(self._instr_obj)
            self.marker         = self.Marker(self._instr_obj)
            self.math           = self.Math(self._instr_obj)
            self.mathstatistics = self.MathStatistics(self._instr_obj)
            self.parameter      = self.Parameter(self._instr_obj)
            self.ripplelimit    = self.RippleLimit(self._instr_obj)
            self.smoothing      = self.Smoothing(self._instr_obj)
            self.transform      = self.Transform(self._instr_obj)

        def _set_channel(self, channel):
            self._channel = channel
            self.conversion._set_channel(self._channel)
            self.data._set_channel(self._channel)
            self.fixturesimulate._set_channel(self._channel)
            self.function._set_channel(self._channel)
            self.hold._set_channel(self._channel)
            self.limit._set_channel(self._channel)
            self.marker._set_channel(self._channel)
            self.math._set_channel(self._channel)
            self.mathstatistics._set_channel(self._channel)
            self.parameter._set_channel(self._channel)
            self.ripplelimit._set_channel(self._channel)
            self.smoothing._set_channel(self._channel)
            self.transform._set_channel(self._channel)

        def _set_trace(self, trace):
            self._trace = trace
            self.conversion._set_trace(self._trace)
            self.data._set_trace(self._trace)
            self.fixturesimulate._set_trace(self._trace)
            self.function._set_trace(self._trace)
            self.hold._set_trace(self._trace)
            self.limit._set_trace(self._trace)
            self.marker._set_trace(self._trace)
            self.math._set_trace(self._trace)
            self.mathstatistics._set_trace(self._trace)
            self.parameter._set_trace(self._trace)
            self.ripplelimit._set_trace(self._trace)
            self.smoothing._set_trace(self._trace)
            self.transform._set_trace(self._trace)

        def _set_marker(self, marker):
            self._marker = marker
            self.conversion._set_marker(self._set_marker)
        
        def _set_port(self, port):
            self._port = port
            self.conversion._set_port(self._port)

        def _set_parameter(self, parameter):
            self._parameter = parameter
            self.conversion._set_parameter(self._parameter)
        
        def _set_standard(self, standard):
            self._standard = standard
            self.conversion._set_standard(self._standard)
        
        def _set_cal_kit(self, kit):
            self._cal_kit = kit
            self.conversion._set_cal_kit(self._cal_kit)

        class Conversion():
            def __init__(self, instrobj):
                self._instr_obj = instrobj
                self._channel = None
                self._trace = None
                self._marker = None
                self._port = None
                self._parameter = None
                self._standard = None
                self._cal_kit = None

            def _set_channel(self, channel):
                self._channel = channel
            
            def _set_trace(self, trace):
                self._trace = trace

            def _set_marker(self, marker):
                self._marker = marker
            
            def _set_port(self, port):
                self._port = port
            
            def _set_parameter(self, parameter):
                self._parameter = parameter
            
            def _set_standard(self, standard):
                self._standard = standard
            
            def _set_cal_kit(self, kit):
                self._cal_kit = kit

            @property
            def conversion(self):
                return f"CALC{self._channel}:CONV?"
            
            @conversion.setter
            def conversion(self, state):
                val = f"CALC{self._channel}:CONV {state}"
                print(val)

            @property
            def function(self):
                return f"CALC{self._channel}:CONV:FUNC?"
            
            @function.setter
            def conversion_function(self, function):
                val = f"CALC{self._channel}:CONV:FUNC {function}"

            class ElectricalDelay():
                def __init__(self, instrobj):
                    self._instr_obj = instrobj
                    self._channel = None
                    self._trace = None
                    self._marker = None

                    self.distance = self.Distance(self._instr_obj)
                
                def _set_channel(self, channel):
                    self._channel = channel
                    self.distance._set_channel(self._channel)
                
                def _set_trace(self, trace):
                    self._trace = trace
                    self.distance._set_trace(self._trace)

                def _set_marker(self, marker):
                    self._marker = marker
                    self.distance._set_marker(self._marker)

                class Distance():
                    def __init(self, instrobj):
                        self._instr_obj = instrobj
                        self._channel = None
                        self._trace = None
                        self._marker = None
                    
                    def _set_channel(self, channel):
                        self._channel = channel
                    
                    def _set_trace(self, trace):
                        self._trace = trace

                    def _set_marker(self, marker):
                        self._marker = marker

                    @property
                    def distance(self):
                        """Reads out the value of the equivalent distance in the electrical delay function. 

                        Returns:
                            float: The distance value.
                        """
                        return float(self._instr_obj.query(f"CALC{self._channel}:TRAC{self._trace}:CORR:EDEL:DIST?").rstrip())
                    
                    @distance.setter
                    def distance(self, dist:float=0.1):
                        """Sets the value of the equivalent distance in the electrical delay function. 

                        Args:
                            dist (float): The distance value.
                        """
                        self._instr_obj.write(f"CALC{self._channel}:TRAC{self._trace}:CORR:EDEL:DIST {dist}")
                    
                    @property
                    def units(self):
                        return 1
                    
                    @units.setter
                    def units(self, units):
                        val = units
            
            class Offset():
                def __init__(self, instrobj):
                    self._instr_obj = instrobj
            
            @property
            def state(self):
                return f"CALC{self._channel}:CONV:FUNC?"
            
            @state.setter
            def state(self, state):
                val = state

        class Correction():
            def __init__(self, instrobj):
                self._instr_obj = instrobj
                self._channel = None
                self._trace = None
                self._marker = None
                self._port = None
                self._parameter = None
                self._standard = None
                self._cal_kit = None

                self.electrical_delay = self.ElectricalDelay(self._instr_obj)
                self.offset = self.Offset(self._instr_obj)

            def _set_channel(self, channel):
                self._channel = channel
                self.electrical_delay._set_channel(self._set_channel)
            
            def _set_trace(self, trace):
                self._trace = trace
                self.electrical_delay._set_trace(self._trace)
            
            def _set_marker(self, marker):
                self._marker = marker
            
            def _set_port(self, port):
                self._port = port
            
            def _set_parameter(self, parameter):
                self._parameter = parameter
            
            def _set_standard(self, standard):
                self._standard = standard
            
            def _set_cal_kit(self, kit):
                self._cal_kit = kit

            class ElectricalDelay():
                def __init__(self, instrobj):
                    self._instr_obj = instrobj
                    self._channel = None
                    self._trace = None
                    self._marker = None
                    self._port = None
                    self._parameter = None
                    self._standard = None
                    self._cal_kit = None

                def _set_channel(self, channel):
                    self._channel = channel
                
                def _set_trace(self, trace):
                    self._trace = trace

                def _set_marker(self, marker):
                    self._marker = marker
                
                def _set_port(self, port):
                    self._port = port
                
                def _set_parameter(self, parameter):
                    self._parameter = parameter
                
                def _set_standard(self, standard):
                    self._standard = standard
                
                def _set_cal_kit(self, kit):
                    self._cal_kit = kit
            
            class Offset():
                def __init__(self, instrobj):
                    self._instr_obj = instrobj
                    self._channel = None
                    self._trace = None
                    self._marker = None
                    self._port = None
                    self._parameter = None
                    self._standard = None
                    self._cal_kit = None

                def _set_channel(self, channel):
                    self._channel = channel
                
                def _set_trace(self, trace):
                    self._trace = trace

                def _set_marker(self, marker):
                    self._marker = marker
                
                def _set_port(self, port):
                    self._port = port
                
                def _set_parameter(self, parameter):
                    self._parameter = parameter
                
                def _set_standard(self, standard):
                    self._standard = standard
                
                def _set_cal_kit(self, kit):
                    self._cal_kit = kit

        class Data():
            def __init__(self, instrobj):
                self._instr_obj = instrobj
                self._channel = None
                self._trace = None
                self._marker = None
                self._port = None
                self._parameter = None
                self._standard = None
                self._cal_kit = None

            def _set_channel(self, channel):
                self._channel = channel
            
            def _set_trace(self, trace):
                self._trace = trace

            def _set_marker(self, marker):
                self._marker = marker
            
            def _set_port(self, port):
                self._port = port
            
            def _set_parameter(self, parameter):
                self._parameter = parameter
            
            def _set_standard(self, standard):
                self._standard = standard
            
            def _set_cal_kit(self, kit):
                self._cal_kit = kit

        class Filter():
            def __init__(self, instrobj):
                self._instr_obj = instrobj
                self._channel = None
                self._trace = None
                self._marker = None
                self._port = None
                self._parameter = None
                self._standard = None
                self._cal_kit = None

                self.time = self.Time(self._instr_obj)

            def _set_channel(self, channel):
                self._channel = channel
            
            def _set_trace(self, trace):
                self._trace = trace
            
            def _set_marker(self, marker):
                self._marker = marker
            
            def _set_port(self, port):
                self._port = port
            
            def _set_parameter(self, parameter):
                self._parameter = parameter
            
            def _set_standard(self, standard):
                self._standard = standard
            
            def _set_cal_kit(self, kit):
                self._cal_kit = kit

            class Time():
                def __init__(self, instrobj):
                    self._instr_obj = instrobj
                    self._channel = None
                    self._trace = None
                    self._marker = None
                    self._port = None
                    self._parameter = None
                    self._standard = None
                    self._cal_kit = None
                
                def _set_channel(self, channel):
                    self._channel = channel
                
                def _set_trace(self, trace):
                    self._trace = trace
                
                def _set_marker(self, marker):
                    self._marker = marker
                
                def _set_port(self, port):
                    self._port = port
                
                def _set_parameter(self, parameter):
                    self._parameter = parameter
                
                def _set_standard(self, standard):
                    self._standard = standard
                
                def _set_cal_kit(self, kit):
                    self._cal_kit = kit

        @property
        def format(self):
            return 0
        
        @format.setter
        def format(self, format):
            val = format

        class FixtureSimulate():
            def __init__(self, instrobj):
                self._instr_obj = instrobj
                self._channel = None
                self._trace = None
                self._marker = None
                self._port = None
                self._parameter = None
                self._standard = None
                self._cal_kit = None
                
                self.balance = self.Balance(self._instr_obj)
                self.embed = self.Embed(self._instr_obj)
                self.send = self.Send(self._instr_obj)

            def _set_channel(self, channel):
                self._channel = channel
            
            def _set_trace(self, trace):
                self._trace = trace
            
            def _set_marker(self, marker):
                self._marker = marker
            
            def _set_port(self, port):
                self._port = port
            
            def _set_parameter(self, parameter):
                self._parameter = parameter
            
            def _set_standard(self, standard):
                self._standard = standard
            
            def _set_cal_kit(self, kit):
                self._cal_kit = kit

            class Balance():
                def __init__(self, instrobj):
                    self._instr_obj = instrobj
                    self._channel = None
                    self._trace = None
                    self._marker = None
                    self._port = None
                    self._parameter = None
                    self._standard = None
                    self._cal_kit = None

                    self.czconversion = self.CZConversion(self._instr_obj)
                    self.diff_matching_circuit = self.DifferentialMatchingCircuit(self._instr_obj)
                    self.diffzconversion = self.DifferentialImpedanceConversion(self._instr_obj)
                    self.parameter = self.Parameter(self._instr_obj)
                    self.top = self.Top(self._instr_obj)

                def _set_channel(self, channel):
                    self._channel = channel
                
                def _set_trace(self, trace):
                    self._trace = trace
                
                def _set_marker(self, marker):
                    self._marker = marker
                
                def _set_port(self, port):
                    self._port = port
                
                def _set_parameter(self, parameter):
                    self._parameter = parameter
                
                def _set_standard(self, standard):
                    self._standard = standard
                
                def _set_cal_kit(self, kit):
                    self._cal_kit = kit

                class CZConversion():
                    def __init__(self, instrobj):
                        self._instr_obj = instrobj
                        self._channel = None
                        self._trace = None
                        self._marker = None
                        self._port = None
                        self._parameter = None
                        self._standard = None
                        self._cal_kit = None

                        self.balance_port = self.BalancePort(self._instr_obj)

                    def _set_channel(self, channel):
                        self._channel = channel
                    
                    def _set_trace(self, trace):
                        self._trace = trace

                    def _set_marker(self, marker):
                        self._marker = marker
                    
                    def _set_port(self, port):
                        self._port = port
                    
                    def _set_parameter(self, parameter):
                        self._parameter = parameter
                    
                    def _set_standard(self, standard):
                        self._standard = standard
                    
                    def _set_cal_kit(self, kit):
                        self._cal_kit = kit

                    class BalancePort():
                        def __init__(self, instrobj):
                            self._instr_obj = instrobj
                            self._channel = None
                            self._trace = None
                            self._marker = None
                            self._port = None
                            self._parameter = None
                            self._standard = None
                            self._cal_kit = None

                        def _set_channel(self, channel):
                            self._channel = channel
                        
                        def _set_trace(self, trace):
                            self._trace = trace

                        def _set_marker(self, marker):
                            self._marker = marker
                        
                        def _set_port(self, port):
                            self._port = port
                        
                        def _set_parameter(self, parameter):
                            self._parameter = parameter
                        
                        def _set_standard(self, standard):
                            self._standard = standard
                        
                        def _set_cal_kit(self, kit):
                            self._cal_kit = kit

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
                        self._instr_obj = instrobj
                        self._channel = None
                        self._trace = None
                    
                        self.balance_port = self.BalancePort(self._instr_obj)
                        self._marker = None
                        self._port = None
                        self._parameter = None
                        self._standard = None
                        self._cal_kit = None

                    def _set_channel(self, channel):
                        self._channel = channel
                    
                    def _set_trace(self, trace):
                        self._trace = trace

                    def _set_marker(self, marker):
                        self._marker = marker
                    
                    def _set_port(self, port):
                        self._port = port
                    
                    def _set_parameter(self, parameter):
                        self._parameter = parameter
                    
                    def _set_standard(self, standard):
                        self._standard = standard
                    
                    def _set_cal_kit(self, kit):
                        self._cal_kit = kit

                    class BalancePort():
                        def __init__(self, instrobj):
                            self._instr_obj = instrobj
                            self._channel = None
                            self._trace = None
                            self._marker = None
                            self._port = None
                            self._parameter = None
                            self._standard = None
                            self._cal_kit = None

                        def _set_channel(self, channel):
                            self._channel = channel
                        
                        def _set_trace(self, trace):
                            self._trace = trace

                        def _set_marker(self, marker):
                            self._marker = marker
                        
                        def _set_port(self, port):
                            self._port = port
                        
                        def _set_parameter(self, parameter):
                            self._parameter = parameter
                        
                        def _set_standard(self, standard):
                            self._standard = standard
                        
                        def _set_cal_kit(self, kit):
                            self._cal_kit = kit

                    @property
                    def state(self):
                        return 1
                    
                    @state.setter
                    def state(self, state):
                        v = state

                class DifferentialImpedanceConversion():
                    def __init__(self, instrobj):
                        self._instr_obj = instrobj
                        self._channel = None
                        self._trace = None
                        self._marker = None
                        self._port = None
                        self._parameter = None
                        self._standard = None
                        self._cal_kit = None

                        self.balance_port = self.BalancePort(self._instr_obj)

                    def _set_channel(self, channel):
                        self._channel = channel
                    
                    def _set_trace(self, trace):
                        self._trace = trace

                    def _set_marker(self, marker):
                        self._marker = marker
                    
                    def _set_port(self, port):
                        self._port = port
                    
                    def _set_parameter(self, parameter):
                        self._parameter = parameter
                    
                    def _set_standard(self, standard):
                        self._standard = standard
                    
                    def _set_cal_kit(self, kit):
                        self._cal_kit = kit

                    class BalancePort():
                        def __init__(self, instrobj):
                            self._instr_obj = instrobj
                            self._channel = None
                            self._trace = None
                            self._marker = None
                            self._port = None
                            self._parameter = None
                            self._standard = None
                            self._cal_kit = None

                        def _set_channel(self, channel):
                            self._channel = channel
                        
                        def _set_trace(self, trace):
                            self._trace = trace

                        def _set_marker(self, marker):
                            self._marker = marker
                        
                        def _set_port(self, port):
                            self._port = port
                        
                        def _set_parameter(self, parameter):
                            self._parameter = parameter
                        
                        def _set_standard(self, standard):
                            self._standard = standard
                        
                        def _set_cal_kit(self, kit):
                            self._cal_kit = kit

                    @property
                    def state(self):
                        return 1
                    
                    @state.setter
                    def state(self, state):
                        v = state

                class Parameter():
                    def __init__(self, instrobj):
                        self._instr_obj = instrobj
                        self._channel = None
                        self._trace = None
                        self._marker = None
                        self._port = None
                        self._parameter = None
                        self._standard = None
                        self._cal_kit = None

                    def _set_channel(self, channel):
                        self._channel = channel
                    
                    def _set_trace(self, trace):
                        self._trace = trace

                    def _set_marker(self, marker):
                        self._marker = marker
                    
                    def _set_port(self, port):
                        self._port = port
                    
                    def _set_parameter(self, parameter):
                        self._parameter = parameter
                    
                    def _set_standard(self, standard):
                        self._standard = standard
                    
                    def _set_cal_kit(self, kit):
                        self._cal_kit = kit

                class Top():
                    def __init__(self, instrobj):
                        self._instr_obj = instrobj
                        self._channel = None
                        self._trace = None
                        self._marker = None
                        self._port = None
                        self._parameter = None
                        self._standard = None
                        self._cal_kit = None

                    def _set_channel(self, channel):
                        self._channel = channel
                    
                    def _set_trace(self, trace):
                        self._trace = trace

                    def _set_marker(self, marker):
                        self._marker = marker
                    
                    def _set_port(self, port):
                        self._port = port
                    
                    def _set_parameter(self, parameter):
                        self._parameter = parameter
                    
                    def _set_standard(self, standard):
                        self._standard = standard
                    
                    def _set_cal_kit(self, kit):
                        self._cal_kit = kit

            class Embed():
                def __init__(self, instrobj):
                    self._instr_obj = instrobj
                    self._channel = None
                    self._trace = None
                    self._marker = None
                    self._port = None
                    self._parameter = None
                    self._standard = None
                    self._cal_kit = None

                    self.network = self.Network(self._instr_obj)
                    self.topology = self.Topology(self._instr_obj)

                def _set_channel(self, channel):
                    self._channel = channel
                
                def _set_trace(self, trace):
                    self._trace = trace

                def _set_marker(self, marker):
                    self._marker = marker
                
                def _set_port(self, port):
                    self._port = port
                
                def _set_parameter(self, parameter):
                    self._parameter = parameter
                
                def _set_standard(self, standard):
                    self._standard = standard
                
                def _set_cal_kit(self, kit):
                    self._cal_kit = kit

                class Network():
                    def __init__(self, instrobj):
                        self._instr_obj = instrobj
                        self._channel = None
                        self._trace = None
                        self._marker = None
                        self._port = None
                        self._parameter = None
                        self._standard = None
                        self._cal_kit = None

                    def _set_channel(self, channel):
                        self._channel = channel
                    
                    def _set_trace(self, trace):
                        self._trace = trace

                    def _set_marker(self, marker):
                        self._marker = marker
                    
                    def _set_port(self, port):
                        self._port = port
                    
                    def _set_parameter(self, parameter):
                        self._parameter = parameter
                    
                    def _set_standard(self, standard):
                        self._standard = standard
                    
                    def _set_cal_kit(self, kit):
                        self._cal_kit = kit

                @property
                def state(self):
                    return 1
                
                @state.setter
                def state(self, state):
                    val = state

                class Topology():
                    def __init__(self, instrobj):
                        self._instr_obj = instrobj
                        self._channel = None
                        self._trace = None
                        self._marker = None
                        self._port = None
                        self._parameter = None
                        self._standard = None
                        self._cal_kit = None

                    def _set_channel(self, channel):
                        self._channel = channel
                    
                    def _set_trace(self, trace):
                        self._trace = trace

                    def _set_marker(self, marker):
                        self._marker = marker
                    
                    def _set_port(self, port):
                        self._port = port
                    
                    def _set_parameter(self, parameter):
                        self._parameter = parameter
                    
                    def _set_standard(self, standard):
                        self._standard = standard
                    
                    def _set_cal_kit(self, kit):
                        self._cal_kit = kit

                @property
                def type(self):
                    return 1
                
                @type.setter
                def type(self, type):
                    val = 1

            class Send():
                def __init__(self, instrobj):
                    self._instr_obj = instrobj
                    self._channel = None
                    self._trace = None

                    self.deembed = self.Deembed(self._instr_obj)
                    self.port_match_ckt = self.PortMatchCircuit(self._instr_obj)
                    self.z_conversion = self.ZConversion(self._instr_obj)

                def _set_channel(self, channel):
                    self._channel = channel
                    self.deembed._set_channel(self._channel)
                    self.port_match_ckt._set_channel(self._channel)
                    self.z_conversion._set_channel(self._channel)
                
                def _set_trace(self, trace):
                    self._trace = trace
                    self.deembed._set_trace(self._trace)
                    self.port_match_ckt._set_trace(self._trace)
                    self.z_conversion._set_trace(self._trace)

                class Deembed():
                    def __init__(self, instrobj):
                        self._instr_obj = instrobj
                        self._channel = None
                        self._trace = None
                        self._marker = None
                        self._port = None
                        self._parameter = None
                        self._standard = None
                        self._cal_kit = None

                    def _set_channel(self, channel):
                        self._channel = channel
                    
                    def _set_trace(self, trace):
                        self._trace = trace

                    def _set_marker(self, marker):
                        self._marker = marker
                    
                    def _set_port(self, port):
                        self._port = port
                    
                    def _set_parameter(self, parameter):
                        self._parameter = parameter
                    
                    def _set_standard(self, standard):
                        self._standard = standard
                    
                    def _set_cal_kit(self, kit):
                        self._cal_kit = kit
                
                class PortMatchCircuit():
                    def __init__(self, instrobj):
                        self._instr_obj = instrobj
                        self._channel = None
                        self._trace = None
                        self._marker = None
                        self._port = None
                        self._parameter = None
                        self._standard = None
                        self._cal_kit = None

                    def _set_channel(self, channel):
                        self._channel = channel
                    
                    def _set_trace(self, trace):
                        self._trace = trace

                    def _set_marker(self, marker):
                        self._marker = marker
                    
                    def _set_port(self, port):
                        self._port = port
                    
                    def _set_parameter(self, parameter):
                        self._parameter = parameter
                    
                    def _set_standard(self, standard):
                        self._standard = standard
                    
                    def _set_cal_kit(self, kit):
                        self._cal_kit = kit

                class ZConversion():
                    def __init__(self, instrobj):
                        self._instr_obj = instrobj
                        self._channel = None
                        self._trace = None
                        self._marker = None
                        self._port = None
                        self._parameter = None
                        self._standard = None
                        self._cal_kit = None

                    def _set_channel(self, channel):
                        self._channel = channel
                    
                    def _set_trace(self, trace):
                        self._trace = trace

                    def _set_marker(self, marker):
                        self._marker = marker
                    
                    def _set_port(self, port):
                        self._port = port
                    
                    def _set_parameter(self, parameter):
                        self._parameter = parameter
                    
                    def _set_standard(self, standard):
                        self._standard = standard
                    
                    def _set_cal_kit(self, kit):
                        self._cal_kit = kit
            
            @property
            def state(self):
                return 1
            
            @state.setter
            def state(self, state):
                val = 1
        
        class Function():
            def __init__(self, instrobj):
                self._instr_obj = instrobj
                self._channel = None
                self._trace = None
                self._marker = None
                self._port = None
                self._parameter = None
                self._standard = None
                self._cal_kit = None

            def _set_channel(self, channel):
                self._channel = channel
            
            def _set_trace(self, trace):
                self._trace = trace

            def _set_marker(self, marker):
                self._marker = marker
            
            def _set_port(self, port):
                self._port = port
            
            def _set_parameter(self, parameter):
                self._parameter = parameter
            
            def _set_standard(self, standard):
                self._standard = standard
            
            def _set_cal_kit(self, kit):
                self._cal_kit = kit

        class Hold():
            def __init__(self, instrobj):
                self._instr_obj = instrobj
                self._channel = None
                self._trace = None
                self._marker = None
                self._port = None
                self._parameter = None
                self._standard = None
                self._cal_kit = None
            
            def _set_channel(self, channel):
                self._channel = channel
                self.report._set_channel = self._channel
            
            def _set_trace(self, trace):
                self._trace = trace

            def _set_marker(self, marker):
                self._marker = marker
            
            def _set_port(self, port):
                self._port = port
            
            def _set_parameter(self, parameter):
                self._parameter = parameter
            
            def _set_standard(self, standard):
                self._standard = standard
            
            def _set_cal_kit(self, kit):
                self._cal_kit = kit

        class Limit():
            def __init__(self, instrobj):
                self._instr_obj = instrobj
                self._channel = None
                self._trace = None
                self._marker = None
                self._port = None
                self._parameter = None
                self._standard = None
                self._cal_kit = None
                self.report = self.Report(self._instr_obj)
                self.offset = self.Offset(self._instr_obj)
            
            def _set_channel(self, channel):
                self._channel = channel
                self.report._set_channel = self._channel
            
            def _set_trace(self, trace):
                self._trace = trace

            def _set_marker(self, marker):
                self._marker = marker
            
            def _set_port(self, port):
                self._port = port
            
            def _set_parameter(self, parameter):
                self._parameter = parameter
            
            def _set_standard(self, standard):
                self._standard = standard
            
            def _set_cal_kit(self, kit):
                self._cal_kit = kit

            class Report():
                def __init__(self, instrobj):
                    self._instr_obj = instrobj
                    self._channel = None
                    self._trace = None
                    self._marker = None
                    self._port = None
                    self._parameter = None
                    self._standard = None
                    self._cal_kit = None

                def _set_channel(self, channel):
                    self._channel = channel
                
                def _set_trace(self, trace):
                    self._trace = trace

                def _set_marker(self, marker):
                    self._marker = marker
                
                def _set_port(self, port):
                    self._port = port
                
                def _set_parameter(self, parameter):
                    self._parameter = parameter
                
                def _set_standard(self, standard):
                    self._standard = standard
                
                def _set_cal_kit(self, kit):
                    self._cal_kit = kit
            
            class Offset():
                def __init__(self, instrobj):
                    self._instr_obj = instrobj
                    self._channel = None
                    self._trace = None
                    self._marker = None
                    self._port = None
                    self._parameter = None
                    self._standard = None
                    self._cal_kit = None

                def _set_channel(self, channel):
                    self._channel = channel
                
                def _set_trace(self, trace):
                    self._trace = trace

                def _set_marker(self, marker):
                    self._marker = marker
                
                def _set_port(self, port):
                    self._port = port
                
                def _set_parameter(self, parameter):
                    self._parameter = parameter
                
                def _set_standard(self, standard):
                    self._standard = standard
                
                def _set_cal_kit(self, kit):
                    self._cal_kit = kit

        class Marker():
            def __init__(self, instrobj):
                self._instr_obj = instrobj
                self._channel = None
                self._trace = None
                self._marker = None
                self._port = None
                self._parameter = None
                self._standard = None
                self._cal_kit = None

            def _set_channel(self, channel):
                self._channel = channel
            
            def _set_trace(self, trace):
                self._trace = trace

            def _set_marker(self, marker):
                self._marker = marker
            
            def _set_port(self, port):
                self._port = port
            
            def _set_parameter(self, parameter):
                self._parameter = parameter
            
            def _set_standard(self, standard):
                self._standard = standard
            
            def _set_cal_kit(self, kit):
                self._cal_kit = kit

        class Math():
            def __init__(self, instrobj):
                self._instr_obj = instrobj
                self._channel = None
                self._trace = None
                self._marker = None
                self._port = None
                self._parameter = None
                self._standard = None
                self._cal_kit = None

            def _set_channel(self, channel):
                self._channel = channel
            
            def _set_trace(self, trace):
                self._trace = trace

            def _set_marker(self, marker):
                self._marker = marker
            
            def _set_port(self, port):
                self._port = port
            
            def _set_parameter(self, parameter):
                self._parameter = parameter
            
            def _set_standard(self, standard):
                self._standard = standard
            
            def _set_cal_kit(self, kit):
                self._cal_kit = kit

        class MathStatistics():
            def __init__(self, instrobj):
                self._instr_obj = instrobj
                self._channel = None
                self._trace = None
                self._marker = None
                self._port = None
                self._parameter = None
                self._standard = None
                self._cal_kit = None

            def _set_channel(self, channel):
                self._channel = channel
            
            def _set_trace(self, trace):
                self._trace = trace
            
            def _set_marker(self, marker):
                self._marker = marker
            
            def _set_port(self, port):
                self._port = port
            
            def _set_parameter(self, parameter):
                self._parameter = parameter
            
            def _set_standard(self, standard):
                self._standard = standard
            
            def _set_cal_kit(self, kit):
                self._cal_kit = kit

        class Parameter():
            def __init__(self, instrobj):
                self._instr_obj = instrobj
                self._channel = None
                self._trace = None
                self._marker = None
                self._port = None
                self._parameter = None
                self._standard = None
                self._cal_kit = None

            def _set_channel(self, channel):
                self._channel = channel
            
            def _set_trace(self, trace):
                self._trace = trace
            
            def _set_marker(self, marker):
                self._marker = marker
            
            def _set_port(self, port):
                self._port = port
            
            def _set_parameter(self, parameter):
                self._parameter = parameter
            
            def _set_standard(self, standard):
                self._standard = standard
            
            def _set_cal_kit(self, kit):
                self._cal_kit = kit

        class RippleLimit():
            def __init__(self, instrobj):
                self._instr_obj = instrobj
                self._channel = None
                self._trace = None
                self._marker = None
                self._port = None
                self._parameter = None
                self._standard = None
                self._cal_kit = None

            def _set_channel(self, channel):
                self._channel = channel
                self.report._set_channel = self._channel
            
            def _set_trace(self, trace):
                self._trace = trace
            
            def _set_marker(self, marker):
                self._marker = marker
            
            def _set_port(self, port):
                self._port = port
            
            def _set_parameter(self, parameter):
                self._parameter = parameter
            
            def _set_standard(self, standard):
                self._standard = standard
            
            def _set_cal_kit(self, kit):
                self._cal_kit = kit

        class Smoothing():
            def __init__(self, instrobj):
                self._instr_obj = instrobj
                self._channel = None
                self._trace = None
                self._marker = None
                self._port = None
                self._parameter = None
                self._standard = None
                self._cal_kit = None

            def _set_channel(self, channel):
                self._channel = channel
            
            def _set_trace(self, trace):
                self._trace = trace

            def _set_marker(self, marker):
                self._marker = marker
            
            def _set_port(self, port):
                self._port = port
            
            def _set_parameter(self, parameter):
                self._parameter = parameter
            
            def _set_standard(self, standard):
                self._standard = standard
            
            def _set_cal_kit(self, kit):
                self._cal_kit = kit

        class Transform():
            def __init__(self, instrobj):
                self._instr_obj = instrobj
                self._channel = None
                self._trace = None
                self._marker = None
                self._port = None
                self._parameter = None
                self._standard = None
                self._cal_kit = None

            def _set_channel(self, channel):
                self._channel = channel
            
            def _set_trace(self, trace):
                self._trace = trace

            def _set_marker(self, marker):
                self._marker = marker
            
            def _set_port(self, port):
                self._port = port
            
            def _set_parameter(self, parameter):
                self._parameter = parameter
            
            def _set_standard(self, standard):
                self._standard = standard
            
            def _set_cal_kit(self, kit):
                self._cal_kit = kit

    class Display():
        def __init__(self, instrobj):
            self._instr_obj = instrobj
            self._channel = None
            self._trace = None
            self._marker = None
            self._port = None
            self._parameter = None
            self._standard = None
            self._cal_kit = None

        def _set_channel(self, channel):
            self._channel = channel

        def _set_trace(self, trace):
            self._trace = trace
        
        def _set_marker(self, marker):
            self._marker = marker
        
        def _set_port(self, port):
            self._port = port
        
        def _set_parameter(self, parameter):
            self._parameter = parameter
        
        def _set_standard(self, standard):
            self._standard = standard
        
        def _set_cal_kit(self, kit):
            self._cal_kit = kit
    
    class Format():
        def __init__(self, instrobj):
            self._instr_obj = instrobj
            self._channel = None
            self._trace = None
            self._marker = None
            self._port = None
            self._parameter = None
            self._standard = None
            self._cal_kit = None

        def _set_channel(self, channel):
            self._channel = channel

        def _set_trace(self, trace):
            self._trace = trace

        def _set_marker(self, marker):
            self._marker = marker
        
        def _set_port(self, port):
            self._port = port
        
        def _set_parameter(self, parameter):
            self._parameter = parameter
        
        def _set_standard(self, standard):
            self._standard = standard
        
        def _set_cal_kit(self, kit):
            self._cal_kit = kit

    class HardCopy():
        def __init__(self, instrobj):
            self._instr_obj = instrobj
            self._channel = None
            self._trace = None
            self._marker = None
            self._port = None
            self._parameter = None
            self._standard = None
            self._cal_kit = None

        def _set_channel(self, channel):
            self._channel = channel

        def _set_trace(self, trace):
            self._trace = trace
        
        def _set_marker(self, marker):
            self._marker = marker
        
        def _set_port(self, port):
            self._port = port
        
        def _set_parameter(self, parameter):
            self._parameter = parameter
        
        def _set_standard(self, standard):
            self._standard = standard
        
        def _set_cal_kit(self, kit):
            self._cal_kit = kit
    
    class Initiate():
        def __init__(self, instrobj):
            self._instr_obj = instrobj
            self._channel = None
            self._trace = None
            self._marker = None
            self._port = None
            self._parameter = None
            self._standard = None
            self._cal_kit = None

        def _set_channel(self, channel):
            self._channel = channel

        def _set_trace(self, trace):
            self._trace = trace

        def _set_marker(self, marker):
            self._marker = marker
        
        def _set_port(self, port):
            self._port = port
        
        def _set_parameter(self, parameter):
            self._parameter = parameter
        
        def _set_standard(self, standard):
            self._standard = standard
        
        def _set_cal_kit(self, kit):
            self._cal_kit = kit

    class Mmemory():
        def __init__(self, instrobj):
            self._instr_obj = instrobj
            self._channel = None
            self._trace = None
            self._marker = None
            self._port = None
            self._parameter = None
            self._standard = None
            self._cal_kit = None

        def _set_channel(self, channel):
            self._channel = channel

        def _set_trace(self, trace):
            self._trace = trace

        def _set_marker(self, marker):
            self._marker = marker
        
        def _set_port(self, port):
            self._port = port
        
        def _set_parameter(self, parameter):
            self._parameter = parameter
        
        def _set_standard(self, standard):
            self._standard = standard
        
        def _set_cal_kit(self, kit):
            self._cal_kit = kit
        
    @property
    def output(self):
        return "y"
    
    @output.setter
    def output(self, state):
        val = 1

    class Sense():
        def __init__(self, instrobj):
            self._instr_obj = instrobj
            self._channel = None
            self._trace = None
            self._marker = None
            self._port = None
            self._parameter = None
            self._standard = None
            self._cal_kit = None

        def _set_channel(self, channel):
            self._channel = channel

        def _set_trace(self, trace):
            self._trace = trace

        def _set_marker(self, marker):
            self._marker = marker
        
        def _set_port(self, port):
            self._port = port
        
        def _set_parameter(self, parameter):
            self._parameter = parameter
        
        def _set_standard(self, standard):
            self._standard = standard
        
        def _set_cal_kit(self, kit):
            self._cal_kit = kit
            
    class Service():
        def __init__(self, instrobj):
            self._instr_obj = instrobj
            self._channel = None
            self._trace = None
            self._marker = None
            self._port = None
            self._parameter = None
            self._standard = None
            self._cal_kit = None

        def _set_channel(self, channel):
            self._channel = channel

        def _set_trace(self, trace):
            self._trace = trace

        def _set_marker(self, marker):
            self._marker = marker
        
        def _set_port(self, port):
            self._port = port
        
        def _set_parameter(self, parameter):
            self._parameter = parameter
        
        def _set_standard(self, standard):
            self._standard = standard
        
        def _set_cal_kit(self, kit):
            self._cal_kit = kit

    class Source():
        def __init__(self, instrobj):
            self._instr_obj = instrobj
            self._channel = None
            self._trace = None
            self._marker = None
            self._port = None
            self._parameter = None
            self._standard = None
            self._cal_kit = None

        def _set_channel(self, channel):
            self._channel = channel

        def _set_trace(self, trace):
            self._trace = trace    

        def _set_marker(self, marker):
            self._marker = marker
        
        def _set_port(self, port):
            self._port = port
        
        def _set_parameter(self, parameter):
            self._parameter = parameter
        
        def _set_standard(self, standard):
            self._standard = standard
        
        def _set_cal_kit(self, kit):
            self._cal_kit = kit

    class Status():
        def __init__(self, instrobj):
            self._instr_obj = instrobj
            self._channel = None
            self._trace = None
            self._marker = None
            self._port = None
            self._parameter = None
            self._standard = None
            self._cal_kit = None

        def _set_channel(self, channel):
            self._channel = channel

        def _set_trace(self, trace):
            self._trace = trace 

        def _set_marker(self, marker):
            self._marker = marker
        
        def _set_port(self, port):
            self._port = port
        
        def _set_parameter(self, parameter):
            self._parameter = parameter
        
        def _set_standard(self, standard):
            self._standard = standard
        
        def _set_cal_kit(self, kit):
            self._cal_kit = kit

    class System():
        def __init__(self, instrobj):
            self._instr_obj = instrobj
            self._channel = None
            self._trace = None
            self._marker = None
            self._port = None
            self._parameter = None
            self._standard = None
            self._cal_kit = None

        def _set_channel(self, channel):
            self._channel = channel

        def _set_trace(self, trace):
            self._trace = trace   

        def _set_marker(self, marker):
            self._marker = marker
        
        def _set_port(self, port):
            self._port = port
        
        def _set_parameter(self, parameter):
            self._parameter = parameter
        
        def _set_standard(self, standard):
            self._standard = standard
        
        def _set_cal_kit(self, kit):
            self._cal_kit = kit

    class Trigger():
        def __init__(self, instrobj):
            self._instr_obj = instrobj
            self._channel = None
            self._trace = None
            self._marker = None
            self._port = None
            self._parameter = None
            self._standard = None
            self._cal_kit = None

        def _set_channel(self, channel):
            self._channel = channel

        def _set_trace(self, trace):
            self._trace = trace  
        
        def _set_marker(self, marker):
            self._marker = marker
        
        def _set_port(self, port):
            self._port = port
        
        def _set_parameter(self, parameter):
            self._parameter = parameter
        
        def _set_standard(self, standard):
            self._standard = standard
        
        def _set_cal_kit(self, kit):
            self._cal_kit = kit

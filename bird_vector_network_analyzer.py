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
    def trace(self):
        return self._trace 
    
    @trace.setter
    def trace(self, trace):
        self._trace = trace
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

        class Conversion():
            def __init__(self, instrobj):
                self._instr_obj = instrobj
                self._channel = None
                self._trace = None

            def _set_channel(self, channel):
                self._channel = channel
            
            def _set_trace(self, trace):
                self._trace = trace

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
        
        class Correction():
            def __init__(self, instrobj):
                self._instr_obj = instrobj
                self._channel = None
                self._trace = None

            def _set_channel(self, channel):
                self._channel = channel
            
            def _set_trace(self, trace):
                self._trace = trace

        class Data():
            def __init__(self, instrobj):
                self._instr_obj = instrobj
                self._channel = None
                self._trace = None

            def _set_channel(self, channel):
                self._channel = channel
            
            def _set_trace(self, trace):
                self._trace = trace
        
        class Filter():
            def __init__(self, instrobj):
                self._instr_obj = instrobj
                self._channel = None
                self._trace = None

            def _set_channel(self, channel):
                self._channel = channel
            
            def _set_trace(self, trace):
                self._trace = trace

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

            def _set_channel(self, channel):
                self._channel = channel
            
            def _set_trace(self, trace):
                self._trace = trace
        
        class Function():
            def __init__(self, instrobj):
                self._instr_obj = instrobj
                self._channel = None
                self._trace = None

            def _set_channel(self, channel):
                self._channel = channel
            
            def _set_trace(self, trace):
                self._trace = trace

        class Hold():
            def __init__(self, instrobj):
                self._instr_obj = instrobj
                self._channel = None
                self._trace = None
            
            def _set_channel(self, channel):
                self._channel = channel
                self.report._set_channel = self._channel
            
            def _set_trace(self, trace):
                self._trace = trace

        class Limit():
            def __init__(self, instrobj):
                self._instr_obj = instrobj
                self._channel = None
                self._trace = None
                self.report = self.Report(self._instr_obj)
                self.offset = self.Offset(self._instr_obj)
            
            def _set_channel(self, channel):
                self._channel = channel
                self.report._set_channel = self._channel
            
            def _set_trace(self, trace):
                self._trace = trace

            class Report():
                def __init__(self, instrobj):
                    self._instr_obj = instrobj
                    self._channel = None
                    self._trace = None
                
                def _set_channel(self, channel):
                    self._channel = channel
                
                def _set_trace(self, trace):
                    self._trace = trace
            
            class Offset():
                def __init__(self, instrobj):
                    self._instr_obj = instrobj
                    self._channel = None
                    self._trace = None
                
                def _set_channel(self, channel):
                    self._channel = channel

                def _set_trace(self, trace):
                    self._trace = trace

        class Marker():
            def __init__(self, instrobj):
                self._instr_obj = instrobj
                self._channel = None
                self._trace = None

            def _set_channel(self, channel):
                self._channel = channel
            
            def _set_trace(self, trace):
                self._trace = trace

        class Math():
            def __init__(self, instrobj):
                self._instr_obj = instrobj
                self._channel = None
                self._trace = None

            def _set_channel(self, channel):
                self._channel = channel
            
            def _set_trace(self, trace):
                self._trace = trace
        
        class MathStatistics():
            def __init__(self, instrobj):
                self._instr_obj = instrobj
                self._channel = None
                self._trace = None

            def _set_channel(self, channel):
                self._channel = channel
            
            def _set_trace(self, trace):
                self._trace = trace

        class Parameter():
            def __init__(self, instrobj):
                self._instr_obj = instrobj
                self._channel = None
                self._trace = None

            def _set_channel(self, channel):
                self._channel = channel
            
            def _set_trace(self, trace):
                self._trace = trace

        class RippleLimit():
            def __init__(self, instrobj):
                self._instr_obj = instrobj
                self._channel = None
                self._trace = None

            def _set_channel(self, channel):
                self._channel = channel
                self.report._set_channel = self._channel
            
            def _set_trace(self, trace):
                self._trace = trace

        class Smoothing():
            def __init__(self, instrobj):
                self._instr_obj = instrobj
                self._channel = None
                self._trace = None

            def _set_channel(self, channel):
                self._channel = channel
            
            def _set_trace(self, trace):
                self._trace = trace
        
        class Transform():
            def __init__(self, instrobj):
                self._instr_obj = instrobj
                self._channel = None
                self._trace = None

            def _set_channel(self, channel):
                self._channel = channel
            
            def _set_trace(self, trace):
                self._trace = trace

    class Display():
        def __init__(self, instrobj):
            self._instr_obj = instrobj

        def _set_channel(self, channel):
            self._channel = channel

        def _set_trace(self, trace):
            self._trace = trace
    
    class Format():
        def __init__(self, instrobj):
            self._instr_obj = instrobj

        def _set_channel(self, channel):
            self._channel = channel

        def _set_trace(self, trace):
            self._trace = trace
    
    class HardCopy():
        def __init__(self, instrobj):
            self._instr_obj = instrobj

        def _set_channel(self, channel):
            self._channel = channel

        def _set_trace(self, trace):
            self._trace = trace
    
    class Initiate():
        def __init__(self, instrobj):
            self._instr_obj = instrobj

        def _set_channel(self, channel):
            self._channel = channel

        def _set_trace(self, trace):
            self._trace = trace
    
    class Mmemory():
        def __init__(self, instrobj):
            self._instr_obj = instrobj

        def _set_channel(self, channel):
            self._channel = channel

        def _set_trace(self, trace):
            self._trace = trace
    
    @property
    def output(self):
        return "y"
    
    @output.setter
    def output(self, state):
        val = 1

    class Sense():
        def __init__(self, instrobj):
            self._instr_obj = instrobj

        def _set_channel(self, channel):
            self._channel = channel

        def _set_trace(self, trace):
            self._trace = trace
    
    class Service():
        def __init__(self, instrobj):
            self._instr_obj = instrobj

        def _set_channel(self, channel):
            self._channel = channel

        def _set_trace(self, trace):
            self._trace = trace

    class Source():
        def __init__(self, instrobj):
            self._instr_obj = instrobj

        def _set_channel(self, channel):
            self._channel = channel

        def _set_trace(self, trace):
            self._trace = trace    

    class Status():
        def __init__(self, instrobj):
            self._instr_obj = instrobj

        def _set_channel(self, channel):
            self._channel = channel

        def _set_trace(self, trace):
            self._trace = trace 

    class System():
        def __init__(self, instrobj):
            self._instr_obj = instrobj

        def _set_channel(self, channel):
            self._channel = channel

        def _set_trace(self, trace):
            self._trace = trace   

    class Trigger():
        def __init__(self, instrobj):
            self._instr_obj = instrobj

        def _set_channel(self, channel):
            self._channel = channel

        def _set_trace(self, trace):
            self._trace = trace  
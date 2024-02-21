"""temp docstring"""
import pyvisa as visa


class BirdVectorNetworkAnalyzer():
    """
    This is a driver. 
    """
    def __init__(self):
        self.resource_manager = None
        self.instr_obj = None

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
            self.instrument_object = self.resource_manager.open_resource(
                instrument_resource_string)
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

from bird_vector_network_analyzer import BirdVectorNetworkAnalyzer

bna1k = BirdVectorNetworkAnalyzer()

# Connect to the instrument and clear out any error conditions
bna1k.initialize("TCPIP0::127.0.0.1::inst0::INSTR")
bna1k.get_error_list()

bna1k.system.preset()
bna1k.channel = 1
bna1k.trace = 1

# Set the center frequency, span, and points
bna1k.sense.frequency.center = 433e6
bna1k.sense.frequency.span = 20e6
bna1k.sense.sweep.points = 1001

# Set the calibration kit to be used 
bna1k.sense.correction.collection.calkit.select = 1
input("Connect the OPEN standard then enter y to continue.")
bna1k.sense.correction.collection.calibrate_open(1)
input("Connect the SHORT standard then enter y to continue.")
bna1k.sense.correction.collection.calibrate_short(1)
input("Connect the LOAD standard then enter y to continue.")
bna1k.sense.correction.collection.calibrate_load(1)

bna1k.sense.correction.collection.calibrate_save()

bna1k.close()


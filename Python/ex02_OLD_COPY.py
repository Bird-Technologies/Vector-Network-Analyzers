from bird_vector_network_analyzer import BirdVectorNetworkAnalyzer

bna1k = BirdVectorNetworkAnalyzer()

# Connect to the instrument and clear out any error conditions
bna1k.initialize("TCPIP0::127.0.0.1::inst0::INSTR")
while True:
    err_str = bna1k.query("SYST:ERR?")
    if "No error" in err_str:
        break
    print(err_str)

bna1k.system.preset()
bna1k.channel = 1
bna1k.trace = 1

# Set the center frequency, span, and points
bna1k.sense.frequency.center = 433e6
bna1k.sense.frequency.span = 20e6
bna1k.sense.sweep.points = 1001

# Set the calibration kit to be used 
bna1k.sense.correction.collection.calkit.select = 1
print(bna1k.query("SYST:ERR?"))
input("Connect the OPEN standard then enter y to continue.")
bna1k.sense.correction.collection.calibrate_open(1)
print(bna1k.query("SYST:ERR?"))
input("Connect the SHORT standard then enter y to continue.")
bna1k.sense.correction.collection.calibrate_short(1)
print(bna1k.query("SYST:ERR?"))
input("Connect the LOAD standard then enter y to continue.")
bna1k.sense.correction.collection.calibrate_load(1)
print(bna1k.query("SYST:ERR?"))
bna1k.sense.correction.collection.calibrate_save()
print(bna1k.query("SYST:ERR?"))

print(bna1k.sense.frequency.frequency)
bna1k.sense.frequency.frequency = 1e6
print(bna1k.sense.frequency.center)
print(bna1k.sense.frequency.span)
print(bna1k.sense.frequency.start)
bna1k.sense.frequency.start = 400e6
print(bna1k.sense.frequency.stop)
bna1k.sense.frequency.stop = 800e6
print(bna1k.sense.sweep.points)

bna1k.calculate.conversion = 1
bna1k.calculate.correction.electrical_delay.media = "COAX"
bna1k.calculate.format.type = ""
print(bna1k.calculate.correction.electrical_delay.media)


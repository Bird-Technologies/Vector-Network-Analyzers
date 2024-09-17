## Directory

* **[bird_vector_network_analyzer.py](./bird_vector_network_analyzer.py)**  
An example of what the foundation driver code might look like contained in a single file format. This code can be imported and used in other examples. 
* **[ex01_single_port_calibration.py](./ex01_single_port_calibration.py)**  
This example shows how a user might perform a single port calibration (SOL) using one of the manual calibration standard options. Note that this example uses the bird_vector_network_analyzer.py driver code also featured in this location.
* **[ex02_two_port_calibration.py](./ex02_two_port_calibration.py)**  
This example shows how a user might perform a 2-port calibration (SOLT) using one of the manual calibration standard options. Note that this example uses the bird_vector_network_analyzer.py driver code also featured in this location.
* **[ex03_characterize_antenna.py](./ex03_characterize_antenna.py)**  
This example shows how a user can measure return loss, VSWR, and impedance values (via Smith Chart) to aid in characterizing an antenna. It is expected that the operator will have already performed at least a single port (SOL) measurement calibration, but the code also shows how port extensions might be used to account for connectors added after the cal. Note that this example uses the bird_vector_network_analyzer.py driver code also featured in this location. For more information on antenna characterization, see the application note featured on the [Vector Network Analyzers](https://birdrf.com/Products/Analyzers/VNA.aspx) landing page at birdrf.com that covers this topic.

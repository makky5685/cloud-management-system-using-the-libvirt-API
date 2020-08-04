cloud-management-system-using-the-libvirt-API

This is a Virtual Machine management project intended to automate the process of the spawning/shutting down a virtual machine when necessary conditions are met

The system was made in two phases
	
	Phase 1:
		- A simple load generator was made which was responsible for distributing load evenly on the existing Virutal machines(Load could be dynamically changed by the tester).
		- An autoscaler was made which was responsible for monitoring load and starting the Virutal machines as the load increased.
		- The virtual machines were equipped with Ubuntu server OS and were started automatically by the autoscaler when required.
		- The virtual machines were instances were created beforehand and installed with ComplexHTTPServer for load reception. 
		- All modules were written with python and libvirt API supported by python.


	Phase 2:
		- A new feature was added to the management system which enabled the autoscaler to monitor the Load on virtual machines and automatically shut down Virtual machines when required.
		- Again, the libvirt API was used to monitor the load.
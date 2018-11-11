# TraffiQ-Control
Intelligent Traffic Light Control Using Reinforcement Learning

DESCRIPTION - The proposed system aims to minimize waiting times for motorized vehicles in traffic junctions. The model takes Queue Lengths in different lanes corresponding to a junction as input and provides the traffic light configuration for the junction as output.  

SIMULATION - The simulation was done on SUMO (Simulation of Urban MObility) tool with TraCI (Traffic Control Interface) module for simulating a congestion scenario in 4 junctions in Kowdenahalli, Bengaluru. 

REWARD METRICS - METRIC 1: *AVERAGE SPEED OF ALL VEHICLES IN ALL LANES* - This metric will try to maximize the average speed of vehicles in system so that there are as many vehicles in movement as possible (i.e. less stagnation or congestion in junctions) - RESULT 1: Even though this metric managed to increase the average speed of vehicles and increased movement. It ended up increasing the queue lengths of lanes in congestion. 

METRIC 2: *QUEUE LENGTHS IN DIFFERENT LANES OF A JUNCTION* - This metric tries to minimize the variance for queue lengths in all lanes correponding to a junction. This way all the lane queue lengths are as close to the mean value as possible and thus a good reduction in queue lengths was observed.

*Look at plots in the visualizations directory for further understanding*


INSTALLATION and SETUP

*Install Sumo*
**sudo apt-get install sumo sumo-tools sumo-doc**

*Clone Repo*
**git clone https://github.com/strangest-quark/TraffiQ-Control.git**

*Create virtual environment*
**virtualenv traffic**

*Activate environment*
**source traffic/bin/activate**

*Install requirements*
**pip install -r setup/requirements.txt**

*Set Sumo Home Environment Variable in .bashrc*
**vi ~/.bashrc**
add the following export in the file and save and exit
**export SUMO_HOME=/usr/share/sumo** 
*Source .bashrc*
**source ~/.bashrc**

TESTING 

*Change file paths to "resultsOfDetectors.xml" in the file bangalore.det.xml*
**set absolute path based on your repo location accordingly**


*Run q-learning model with edge density based rewards*
**python EdgeDensityReward.py**
#results in results/EdgeDensityResults.txt

*Run q-learning model with average speed of vehicles based rewards*
**python MeanSpeedReward.py**
#results in results/MeanSpeedResults.txt

*Get Visualizations*
**python ConsolidatedResults.py**







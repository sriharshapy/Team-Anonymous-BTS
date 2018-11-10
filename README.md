# TraffiQ-Control
Intelligent Traffic Light Control Using Reinforcement Learning

INSTALLATION

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

*Run q-learning model with edge density based rewards*
**python EdgeDensityReward.py**
#results in ResultsOfSimulation.txt

*Run q-learning model with average speed of vehicles based rewards*
**python MeanSpeedReward.py**
#results in ResultsOfSimulation1.txt







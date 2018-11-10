# TraffiQ-Control
Intelligent Traffic Light Control Using Reinforcement Learning

TODO : ADD MORE DESCRIPTION
TODO : ADD LOGIC BEHIND REWARD CALCULATIONS

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
#results in ResultsOfSimulation.txt

*Run q-learning model with average speed of vehicles based rewards*
**python MeanSpeedReward.py**
#results in ResultsOfSimulation1.txt







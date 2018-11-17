# TraffiQ-Control

*Intelligent Traffic Light Control Using Reinforcement Learning*

## Overview
The proposed system aims to minimize waiting times for motorized vehicles in traffic junctions. The model takes *Queue Lengths and Average Speeds of vehicles* in different lanes corresponding to a junction as input and provides the *traffic light* configuration for the junction as output.

The following explains the reward metrics used to train the Deep-Q-Learning Model.

### Metric 1 - Mean Speed of Vehicles
This metric will try to maximize the average speed of vehicles in system so that there are as many vehicles in movement as possible (i.e. less stagnation or congestion in junctions). Preliminary results from the results show a *68% increase in mean speed* of vehicles after training.

### Metric 2 - Variance in Queue Lengths
This metric tries to minimize the variance for queue lengths in all lanes correponding to a junction. This way all the lane queue lengths are as close to the mean value as possible. A *48% reduction in queue lengths* was observed.

_Look at plots in the visualizations directory for further understanding_

## Simulation
The simulation was done on *SUMO (Simulation of Urban MObility)* tool with *TraCI (Traffic Control Interface)* module for simulating a congestion scenario in 4 junctions in *Kowdenahalli, Bengaluru.*

## Installation and Setup

 1. Install Sumo
  `sudo apt-get install sumo sumo-tools sumo-doc`
  2. Clone Repo 
  `git clone https://github.com/strangest-quark/TraffiQ-Control.git`
  3. Create virtual environment
  `virtualenv traffic`
  4. Activate environment
  `source traffic/bin/activate`
  5. Install requirements
  `pip install -r setup/requirements.txt`
  6. Set Sumo Home Environment Variable
  `vi ~/.bashrc`
  Add path to sumo
  `SUMO_HOME=/usr/share/sumo`
 Source ~/.bashrc
`source ~/.bashrc`

## Testing
Change file paths to *resultsOfDetectors.xml* in the file *bangalore.det.xml* set absolute path based on your repo location accordingly

**Run q-learning model with edge density based rewards** 

    python EdgeDensityReward.py 

*Results in results/EdgeDensityResults.txt*

**Run q-learning model with average speed of vehicles based rewards** 

    python MeanSpeedReward.py

*Results in results/MeanSpeedResults.txt*

**Get Visualizations** 

    python ConsolidatedResults.py

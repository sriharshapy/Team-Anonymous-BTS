import numpy as np
import matplotlib.pyplot as plt


def getRewards(filename):
	lines = [line.rstrip('\n') for line in open(filename)]
	rewards = []
	for line in lines:
		line = line.split()
		rewards.append(float(line[8]))
	return rewards

def getQlengths(filename):
	lines = [line.rstrip('\n') for line in open(filename)]
	qlengths = []
	for line in lines:
		line = line.split()
		qlengths.append(int(line[2].replace("[","").replace(",","")))
	return qlengths

def plotLengths(len1, len2):
	plt.xlabel('Epochs')
	plt.ylabel('Queue Lengths')
	plt.plot(len1, label="EdgeDensityRewardMetric")
	plt.plot(len2, label="MeanSpeedRewardMetric")
	plt.legend()
	plt.savefig('Visualizations/QueueLengthComparisonPlot.png')
	plt.clf()
	plt.xlabel('Epochs')
	plt.ylabel('Queue Lengths')
	plt.plot(len1, label="EdgeDensityRewardMetric")
	plt.savefig('Visualizations/EdgeDensityQueueLengthPlot.png')
	plt.clf()
	plt.xlabel('Epochs')
	plt.ylabel('Queue Lengths')
	plt.plot(len2, label="EdgeDensityRewardMetric")
	plt.savefig('Visualizations/MeanSpeedQueueLengthPlot.png')
	plt.clf()

def plotRewards(rew1, rew2):
	plt.xlabel('Epochs')
	plt.ylabel('Rewards')
	plt.plot(rew1)
	plt.savefig('Visualizations/EdgeDensityRewardPlot.png')
	plt.clf()
	plt.xlabel('Epochs')
	plt.ylabel('Rewards')
	plt.plot(rew2)
	plt.savefig('Visualizations/MeanSpeedRewardPlot.png')
	plt.clf()


def main():
	lengths1=np.asarray(getQlengths('results/EdgeDensityResults.txt'))
	rewards1=np.asarray(getRewards('results/EdgeDensityResults.txt'))
	lengths2=np.asarray(getQlengths('results/MeanSpeedResults.txt'))
	rewards2=np.asarray(getRewards('results/MeanSpeedResults.txt'))

	plotLengths(lengths1,lengths2)
	plotRewards(rewards1,rewards2)



if __name__ == '__main__':
    main()

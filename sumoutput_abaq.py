# execfile('PATH/sumoutput_abaq.py')
from odbAccess import *
from abaqusConstants import *
from odbMaterial import *
from odbSection import *
from array import *

MYFILENAME = 'path/odbName.odb'
MYINSTANCENAME = 'partname'
MYNODESET1 = 'setName'
MYNODESET2 = 'setName'
myodb = session.odbs[MYFILENAME]
# myodb = openOdb(path=MYFILENAME)
# numFrame=myodb.steps['Step-1'].frames[-1] #-1 means last frame
FrameValues=myodb.steps['Step-1'].frames
regS1 = myodb.rootAssembly.instances[MYINSTANCENAME].nodeSets[MYNODESET1].nodes
regS2 = myodb.rootAssembly.instances[MYINSTANCENAME].nodeSets[MYNODESET2].nodes
i = 0 # Count how many frames in the odb
iRF1TOP=[]
iRF2TOP=[]
for f in FrameValues:
# RForce=numFrame.fieldOutputs['RF'] #RF are the reaction forces
#FX = RForce.getSubset(region=regS1).values[0].data[0] #change the .values[0] to .values[1] or higher to change the node
#FY = RForce.getSubset(region=regS1).values[0].data[1]
	#RFValues1 = RForce.getSubset(region=regS1).values
	RForce=f.fieldOutputs['RF'] #RF are the reaction forces
# print 'RF at Frame --', i
	ii = 1 # Count how many nodes for the node set
	RF1TOP = 0
	RF2TOP = 0
	#for v in RFValues1:
	for v in regS1:
	#print v.nodeLabel, v.data 
		RFvalues1 = RForce.getSubset(region=v).values[0]
		RF1TOP = RF1TOP+RFvalues1.data[0]
		RF2TOP = RF2TOP+RFvalues1.data[1]
	#	RF1TOP = RF1TOP+v.data[0]
	#	RF2TOP = RF2TOP+v.data[1]
		ii = ii+1
	# RFValues2 = RForce.getSubset(region=regS2).values
	jj = 1 # Count how many nodes for the node set
	RF1BOT = 0
	RF2BOT = 0
	for w in regS2:
	#print v.nodeLabel, v.data 
		RFvalues2 = RForce.getSubset(region=w).values[0]
		RF1BOT = RF1BOT+RFvalues2.data[0]
		RF2BOT = RF2BOT+RFvalues2.data[1]
	#	RF1TOP = RF1TOP+v.data[0]
	#	RF2TOP = RF2TOP+v.data[1]
		jj = jj+1 
	# print 'Number of Nodes in BOTTOM set of which RF has been summed:', jj
	# print 'RF1 and RF2 at TOP:', RF1TOP, RF2TOP
	i = i+1
	iRF1TOP.append(RF1TOP)
	iRF2TOP.append(RF2TOP)
	iRF1BOT.append(RF1BOT)
	iRF2TOP.append(RF2BOT)
	print 'RF1 and RF2 at TOP', RF1TOP, RF2TOP

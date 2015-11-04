# execfile('path/plotxy.py')
from odbAccess import *
from abaqusConstants import *
from odbMaterial import *
from odbSection import *
from array import *

MYFILENAME = 'path/odbName.odb'
myodb = session.odbs[MYFILENAME]

myXYDataRF1TOP = session.xyDataListFromField(odb=myodb, outputPosition=NODAL, variable=(('RF', 
	NODAL, ((COMPONENT, 'RF1'), )), ), nodeSets=('PART-1-1.TOP', ))
sum(myXYDataRF1TOP)
session.xyDataObjects['_temp_1'].save()
session.xyDataObjects.changeKey(fromName='XYData-1', toName='RF1TOP')

myXYDataRF2TOP = session.xyDataListFromField(odb=myodb, outputPosition=NODAL, variable=(('RF', 
	NODAL, ((COMPONENT, 'RF2'), )), ), nodeSets=('PART-1-1.TOP', ))
sum(myXYDataRF2TOP)
session.xyDataObjects['_temp_1'].save()
session.xyDataObjects.changeKey(fromName='XYData-1', toName='RF2TOP')

myXYDataRF1BOT = session.xyDataListFromField(odb=myodb, outputPosition=NODAL, variable=(('RF', 
	NODAL, ((COMPONENT, 'RF1'), )), ), nodeSets=('PART-1-1.BOTTOM', ))
sum(myXYDataRF1BOT)
session.xyDataObjects['_temp_1'].save()
session.xyDataObjects.changeKey(fromName='XYData-1', toName='RF1BOT')

myXYDataRF2TOP = session.xyDataListFromField(odb=myodb, outputPosition=NODAL, variable=(('RF', 
	NODAL, ((COMPONENT, 'RF2'), )), ), nodeSets=('PART-1-1.BOTTOM', ))
sum(myXYDataRF2TOP)
session.xyDataObjects['_temp_1'].save()
session.xyDataObjects.changeKey(fromName='XYData-1', toName='RF2BOT')

# python
import lx
import time


##########


t = lx.Monitor()
totalLoops = lx.eval("user.value zReStep_replayRestep ?")
t.init(totalLoops*1)


for i in range (1, (totalLoops+1)) :
	t.step(1)
	lx.eval("@z_reStep_RandomizeFields.py")
	lx.eval("@z_rstep2_2_working.py")
	
	
	
	
	'''
	
	for i in range (1, (lx.eval("user.value zReStep_replayRestep ?")+1)) :
	lx.eval("@z_rstep2_2_working.py")
	lx.eval("@z_reStep_RandomizeFields.py")
	
	'''
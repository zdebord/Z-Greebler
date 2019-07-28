# python
import lx


##########


m = lx.Monitor()
totalLoops = lx.eval("user.value zReStep_replayRestep ?")
m.init(totalLoops*1+2)


for i in range (1, (totalLoops+1)) :
	m.step(1)
	lx.eval("@z_rstep2_2_working.py")

# python
import lx
import math
import random

##########

# myDensity = lx.eval("user.value zReStep_density ?")
# myAmp = lx.eval("user.value zReStep_minAmplitude ?") 
# myShift = lx.eval("user.value zReStep_shiftDistance ?") 
# myInset = lx.eval("user.value zReStep_insetRate ?")


#def getRanNum (num1,num2):
#	return random.sample(num1,num2)

lx.eval("select.drop polygon") 
myNewPolySelect = str(random.randrange(1, 15))
myNewPolySelect = str("user.value zReStep_polygonsSelected ") + myNewPolySelect
myNewfractalCount = str(random.randrange(1, 4))
myNewfractalCount = str("user.value zReStep_fractalCount ") + myNewfractalCount
myNewfractalStack = str(random.randrange(1, 2))
myNewfractalStack = str("user.value zReStep_fractalStackNum ") + myNewfractalStack
myNewColors = str(random.randrange(1, 19))
myNewColors = str("user.value zReStep_totalColors ") + myNewColors
myNewDensity = str(random.randrange(1, 85)*.01)
myNewDensity = str("user.value zReStep_density ") + myNewDensity
myNewAmp =  str(random.randrange(1, 20))
myNewAmp = str("user.value zReStep_minAmplitude ") + myNewAmp
myNewShift = str(random.randrange(2, 200))
myNewShift = str("user.value zReStep_shiftDistance ") + myNewShift
myNewInset = str(random.randrange(20, 80))
myNewInset = str("user.value zReStep_insetRate ") + myNewInset


lx.eval(myNewPolySelect)
lx.eval(myNewfractalCount)
lx.eval(myNewfractalStack)
lx.eval(myNewColors)
lx.eval(myNewDensity)
lx.eval(myNewAmp)
lx.eval(myNewShift)
lx.eval(myNewInset)


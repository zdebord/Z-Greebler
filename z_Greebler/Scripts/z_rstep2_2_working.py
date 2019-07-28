# python
import lx
import math
import random
from multiprocessing import Process
from multiprocessing import Pool

class Random :
	def __init__(self):
		self.l = 3141592641
		self.u= 72389504171
		
#### SEE if any polygons are selected, if not, select random plygons based on user input value	 
		if lx.eval("query layerservice polys ? selected") < 1:
			RandomSelectPolygons()
	
		
		if lx.eval("query scriptsysservice userValue.isDefined ? random.X") :
			self.x = lx.eval("user.value random.X ?")
		else :
			lx.command("user.defNew", name = "random.X"  , type = "float" , life = "config")
			self.x = int(time.time())
		self.x = (self.l*self.x+self.u)%1000000000
		lx.command("user.value" , name = "random.X" , value=self.x)
		
	def getValue(self) :
#		x = lx.eval("user.value random.X ?")
		self.x = (self.l*self.x+self.u)%1000000000
		self.x = (self.l*self.x+self.u)%1000000000
		return self.x/1000000000.0
	def __del__(self):
		lx.command("user.value" , name = "random.X" , value=self.x)

# distance between p1 and p2
def pdistance(p1,p2):
	return math.sqrt((p2[0]-p1[0])**2+(p2[1]-p1[1])**2+(p2[2]-p1[2])**2)

def ddistance(p):
	return math.sqrt(p[0]**2+p[1]**2+p[2]**2)

def idistance(p1,p2):
	pos1 = getVPos(p1)
	pos2 = getVPos(p2)
	return math.sqrt((pos2[0]-pos1[0])**2+(pos2[1]-pos1[1])**2+(pos2[2]-pos1[2])**2)

def createPoint(p):
	lx.command("vert.new", x=p[0] , y=p[1] , z=p[2])
	return lx.eval("query layerservice vert.index ? last")

def selectPoint(vid,lid):
	lx.command("select.element",layer=lid,type="vertex",mode="add",index=vid)

def getVPos(id):
	return lx.eval("query layerservice vert.pos ? %(id)s" % vars())

def createMovePoint(l,n,pid):
	pos=getVPos(pid)
	dist = [n[0] * l + pos[0] , n[1] * l + pos[1], n[2] * l + pos[2]]
	return createPoint(dist)

def getEVector(p1,p2):
	dist = [(p2[0]-p1[0]),(p2[1]-p1[1]),(p2[2]-p1[2])]
	l = ddistance(dist)
	return [dist[0]/l,dist[1]/l,dist[2]/l]
	
def vector(v1,v2,dev):
	return [(v2[0]-v1[0])/dev,(v2[1]-v1[1])/dev,(v2[2]-v1[2])/dev]

def outer(v1,v2):
	return [ v1[1]*v2[2]-v1[2]*v2[1],-(v1[0]*v2[2]-v1[2]*v2[0]),v1[0]*v2[1]-v1[1]*v2[0] ]

def inner(v1,v2):
	return v1[0] * v2[0] + v1[1] * v2[1] + v1[2] * v2[2] 

def getPNormal(id):
	return lx.eval("query layerservice poly.normal ? %(id)s" % vars())

def getPVList(id):
	return lx.eval("query layerservice poly.vertList ? %(id)s" % vars())

def flip(pid,lid):
	lx.eval("select.type polygon")
	lx.command("select.element",layer=lid,type="polygon",mode="set",index=pid)
	lx.eval("poly.flip")
	
def createSqure(vid1,vid2,vid3,vid4,lid):
	lx.eval("select.type vertex") 
	lx.eval("select.drop vertex") 
	selectPoint(vid1,lid)
	selectPoint(vid2,lid)
	selectPoint(vid3,lid)
	selectPoint(vid4,lid)
	lx.command("poly.makeFace")
	
	AddRandomColor()

	
	return lx.eval("query layerservice poly.index ? last")
	
	


# ADDING COLOR	
def AddRandomColor():
	lx.eval("select.type polygon")
	#lx.command("select.element",layer=main,type="polygon")
	ranNum = random.randint(1,100)
	
	totalColors = lx.eval("user.value zReStep_totalColors ?")
	pctChanceMatch = 100/(totalColors*1)
	
	if ranNum >= 1:
		lx.eval("@dark.LXM")
	if ranNum > pctChanceMatch:
		lx.eval("@default.LXM")
	if ranNum > pctChanceMatch*2:
		lx.eval("@yellow.LXM")
	if ranNum > pctChanceMatch*3:
		lx.eval("@blue.LXM")
	if ranNum > pctChanceMatch*4:
		lx.eval("@emerald.LXM")
	if ranNum > pctChanceMatch*5:
		lx.eval("@cyan.LXM")
	if ranNum > pctChanceMatch*6:
		lx.eval("@lime.LXM")
	if ranNum > pctChanceMatch*7:
		lx.eval("@red.LXM")
	if ranNum > pctChanceMatch*8:
		lx.eval("@green.LXM")
	if ranNum > pctChanceMatch*9:
		lx.eval("@orange.LXM")
	if ranNum > pctChanceMatch*10:
		lx.eval("@soft.LXM")
	if ranNum > pctChanceMatch*11:
		lx.eval("@yellowstrong.LXM")
	if ranNum > pctChanceMatch*12:
		lx.eval("@bluestrong.LXM")
	if ranNum > pctChanceMatch*13:
		lx.eval("@emeraldstrong.LXM")
	if ranNum > pctChanceMatch*14:
		lx.eval("@cyanstrong.LXM")
	if ranNum > pctChanceMatch*15:
		lx.eval("@limestrong.LXM")
	if ranNum > pctChanceMatch*16:
		lx.eval("@redstrong.LXM")
	if ranNum > pctChanceMatch*17:
		lx.eval("@greenstrong.LXM")
	if ranNum > pctChanceMatch*18:
		lx.eval("@orangestrong.LXM")
		



# ADDING Random select Polygons

def RandomSelectPolygons():
	
	myPolygons = lx.eval("user.value zReStep_polygonsSelected ?") 

	lx.eval('select.type polygon')
	lx.eval('select.polygon add 0 subdiv 0')
	
	layer = lx.eval('query layerservice layer.index ? main')
	disco_polys = lx.eval('query layerservice polys ? selected')
	disco_polysN = lx.eval('query layerservice poly.N ? selected')
	lx.out('polys:',disco_polys,'count:',disco_polysN)

	Rand_Polys = random.sample(disco_polys, myPolygons)
	lx.out('Rand_Polys:',Rand_Polys)

	lx.eval('select.drop polygon')

	for p in Rand_Polys:
		lx.eval('select.typeFrom polygon')
		lx.eval('select.element %s polygon add %s' % (layer,p))
	

	
	

#Polygon center
def PCenter(vid1,vid2,vid3,vid4):
	pos1 = getVPos(vid1)
	pos2 = getVPos(vid2)
	pos3 = getVPos(vid3)
	pos4 = getVPos(vid4)
	return [(pos1[0]+pos2[0]+pos3[0]+pos4[0])/4,(pos1[1]+pos2[1]+pos3[1]+pos4[1])/4,(pos1[2]+pos2[2]+pos3[2]+pos4[2])/4]

def createWall(vid1,vid2,vid3,vid4,lid,normal,check):
	p = createSqure(vid1,vid2,vid3,vid4,lid)
	if check :
		pn = getPNormal(p)
		v = getEVector(getVPos(vid1),getVPos(vid2))
		n = outer(normal,v)
		if inner(n,pn)<0:flip(p,lid)
	return

def rize(pid1,pid2,pid3,pid4,lid,normal,height,check):
	c1=createMovePoint(height,normal,pid1)
	c2=createMovePoint(height,normal,pid2)
	c3=createMovePoint(height,normal,pid3)
	c4=createMovePoint(height,normal,pid4)
	createWall(pid2,pid1,c1,c2,lid,normal,check)
	createWall(pid3,pid2,c2,c3,lid,normal,check)
	createWall(pid4,pid3,c3,c4,lid,normal,check)
	createWall(pid1,pid4,c4,c1,lid,normal,check)
	return [c1,c2,c3,c4]

def shift(vid1,vid2,vid3,vid4,lid,normal,height,check,cap):
	topvl = rize(vid1,vid2,vid3,vid4,lid,normal,height,check)
	if cap :
		createSqure(topvl[0],topvl[1],topvl[2],topvl[3],lid)
		return None
	else :
		per = int(r.getValue()*ri)
		return inset(topvl,lid,per)

def inset(pvl,lid,per):
	center = PCenter(pvl[0],pvl[1],pvl[2],pvl[3])
	ev1 = getVPos(pvl[0])
	ev2 = getVPos(pvl[1])
	ev3 = getVPos(pvl[2])
	ev4 = getVPos(pvl[3])
	v=getEVector(ev1,center)
	t = pdistance(ev1,center)*per / 100
	c1=createMovePoint(t,v,pvl[0])
	v=getEVector(ev2,center)
	t = pdistance(ev2,center)*per / 100
	c2=createMovePoint(t,v,pvl[1])
	v=getEVector(ev3,center)
	t = pdistance(ev3,center)*per / 100
	c3=createMovePoint(t,v,pvl[2])
	v=getEVector(ev4,center)
	t = pdistance(ev4,center)*per / 100
	c4=createMovePoint(t,v,pvl[3])
	createSqure(pvl[0],pvl[1],c2,c1,lid)
	createSqure(pvl[1],pvl[2],c3,c2,lid)
	createSqure(pvl[2],pvl[3],c4,c3,lid)
	createSqure(pvl[3],pvl[0],c1,c4,lid)
	return [c1,c2,c3,c4]

def divide(vid1,vid2,vid3,vid4,du,dv):
	pos1 = getVPos(vid1)
	pos2 = getVPos(vid2)
	pos3 = getVPos(vid3)
	pos4 = getVPos(vid4)
	vu1 = vector(pos1,pos2,du)
	vu2 = vector(pos4,pos3,du)
	col = []
	for u in range(du+1):
		stv = [vu1[0] * u + pos1[0],vu1[1] * u + pos1[1],vu1[2] * u + pos1[2]]
		edv = [vu2[0] * u + pos4[0],vu2[1] * u + pos4[1],vu2[2] * u + pos4[2]]
		vv = vector(stv,edv,dv)
		raw = []
		for v in range(dv+1):
			v = [vv[0] * v + stv[0],vv[1] * v + stv[1],vv[2] * v + stv[2]]
			if u == 0 and v == 0 :
				raw.append(vid1)
			elif u == du and v == 0 :
				raw.append(vid2)
			elif u == 0  and v == dv :
				raw.append(vid4)
			elif u == du and v == dv :
				raw.append(vid3)
			else :  
				raw.append(createPoint([v[0],v[1],v[2]]))
		col.append(raw)
	return col

def process(vid,lid,normal,limit,rh,limitw):
    minSize = lx.eval("user.value zReStep_minSize ?") #min poly size to create
    limit = limit -1
    du = int(r.getValue()*limit)+1
    dv = int(r.getValue()*limit)+1
    width1 = idistance(vid[0],vid[1])
    width2 = idistance(vid[1],vid[2])
    if (du>dv and width2>width1) or (du<dv and width2<width1) :
        dummy = du
        du = dv
        dv = dummy
    if width1 > 2 * width2 :
        du = du * 2
    if 2 * width1 <  width2 :
        dv = dv * 2
    width=(width1/du+width2/dv)/2
    mesh = divide(vid[0],vid[1],vid[2],vid[3],du,dv)
    for i in range(len(mesh)-1):
        for j in range(len(mesh[0])-1):
            height = r.getValue() * rh      
            if r.getValue() <= r1 and limit>0 and width > limitw:
				vid = shift(mesh[i][j],mesh[i+1][j],mesh[i+1][j+1],mesh[i][j+1],lid,normal,height,True,False)
				if limitw > minSize and normal > 0 and limit > 0:
					process(vid,lid,normal,limit,rh,limitw)
            else :
            	if limitw > minSize and normal > 0:
                	vid = shift(mesh[i][j],mesh[i+1][j],mesh[i+1][j+1],mesh[i][j+1],lid,normal,height,True,True)
	lx.eval("select.drop polygon")

# Z code
#lx.command("user.defNew", name = "myZReStep_density"  , type = "float" , life = "Transient")
#if lx.eval("query zReStep_density userValue.isDefined ?") :
#	myZReStep_density = lx.eval("user.value zReStep_density ?")
#else :
#	myZReStep_density = 0.85


r1 = lx.eval("user.value zReStep_density ?") #percent from center diagonal to start of next polygon
dw = lx.eval("user.value zReStep_minAmplitude ?") #Minimum amplitude - Ratio of minimum width of generated polygon to the initially selected polygon (%) (given as interger)
dh = lx.eval("user.value zReStep_shiftDistance ?") #Shift distance - Distance to shift out
ri = lx.eval("user.value zReStep_insetRate ?") #Inset rate - Distance to inset

r = Random()
main = lx.eval("query layerservice layers ? main")
poly=lx.eval("query layerservice polys ? selected")


#chunksize = 25

def doMainProcess() :
	main = lx.eval("query layerservice layers ? main")
	poly=lx.eval("query layerservice polys ? selected")
	r1 = lx.eval("user.value zReStep_density ?") #percent from center diagonal to start of next polygon
	r1 = int(r1)/100
	dw = lx.eval("user.value zReStep_minAmplitude ?") #Minimum amplitude - Ratio of minimum width of generated polygon to the initially selected polygon (%) (given as interger)
	dh = lx.eval("user.value zReStep_shiftDistance ?") #Shift distance - Distance to shift out
	ri = lx.eval("user.value zReStep_insetRate ?") #Inset rate - Distance to inset
	minSize = float(lx.eval("user.value zReStep_minSize ?")) #min poly size to create
	fracCnt = lx.eval("user.value zReStep_fractalCount ?")
	totalPolySelected = lx.eval("user.value zReStep_polygonsSelected ?")
	replayLoops = lx.eval("user.value  zReStep_replayRestep ?")
	chunkSize = (totalPolySelected*replayLoops)
	polChunks = 1
	
	if poly != None :
		if type(poly) == tuple :
			for pol in poly:
				polChunks+=1
				
	t = lx.Monitor()
	t.init(polChunks+1)
	
	if poly != None :
		limit = lx.eval("user.value zReStep_fractalCount ?")
		if type(poly) == tuple :
			lx.out("asdfasfasdfasf")
			for pol in poly:
				t.step(1)
				vid = getPVList(pol)
				if len(vid) != 4 : continue 
				long = idistance(vid[0],vid[2])
				limitw = long / dw 
				rh = long * dh / 100.0
				normal = getPNormal(pol)
				if limitw > minSize and normal > 0:
					process(vid,main,normal,limit,rh,limitw)
			poly = list(poly)
			poly.sort()
			poly.reverse()
		else :
			lx.out("hiyayayayayayaya")
			vid = getPVList(poly)
			if len(vid) == 4 :
				long = idistance(vid[0],vid[2])
				limitw = long / dw 
				rh = long * dh / 100.0
				normal = getPNormal(poly)
				if limitw > minSize and normal > 0:
					process(vid,main,normal,limit,rh,limitw)
		lx.eval("select.drop polygon")
	
	
	
	
	'''
	if poly != None :
		lx.out("sdfsdfsfsdfsdfsdfsd")
	# loop for how many times to fracaltize, higher takes longer to calculate
		limit = lx.eval("user.value zReStep_fractalCount ?")
		if type(poly) == tuple :
			for pol in poly:
				vid = getPVList(pol)
				if len(vid) != 4 : continue
				t.step(1)
				for i in range (1, ((lx.eval("user.value zReStep_fractalStackNum ?")*1)+1)) :
					mylong = idistance(vid[0],vid[2])
					limitw = mylong / dw
					rh = mylong * dh / 100.0
					normal = getPNormal(pol)
					if (limitw > minSize):
						process(vid,main,normal,limit,rh,limitw)
				poly = list(poly)
				poly.sort()
				poly.reverse()
		else :
			lx.out("hiyayayayayayaya")
			vid = getPVList(poly)
        	if len(vid) == 4 :
		#	m.step(chunkSize)
				for i in range (1, (lx.eval("user.value zReStep_fractalStackNum ?")+1)) :
					mylong = idistance(vid[0],vid[2])
					limitw = mylong / dw 
					rh = mylong * dh / 100.0
					poly=lx.eval("query layerservice polys ? selected")
					normal = getPNormal(poly)
					if limitw > minSize :
						process(vid,main,normal,limit,rh,limitw)
						lx.eval("select.drop polygon")
			

'''
doMainProcess()
lx.eval("select.drop polygon")

'''
if poly != None :
	limit = lx.eval("user.value zReStep_fractalCount ?")
	if type(poly) == tuple :
		for pol in poly:
			vid = getPVList(pol)
			if len(vid) != limit+1 : continue 
			long = idistance(vid[0],vid[2])
			limitw = long / dw 
			rh = long * dh / 100.0
			normal = getPNormal(pol)
			process(vid,main,normal,limit)
		poly = list(poly)
		poly.sort()
		poly.reverse()
	#	for pol in poly:
	#		lx.eval("select.type polygon")
	#		lx.command("select.element",layer=main,type="polygon",mode="set",index=pol)
	#		lx.eval("poly.remove")
	else :
		vid = getPVList(poly)
		if len(vid) == (limit-1) or limit :
			long = idistance(vid[0],vid[2])
			limitw = long / dw 
			rh = long * dh / 100.0
			normal = getPNormal(poly)
			process(vid,main,normal,limit)
	#		lx.eval("select.type polygon")
	#		lx.command("select.element",layer=main,type="polygon",mode="set",index=poly)
	#		lx.eval("poly.remove")	
'''


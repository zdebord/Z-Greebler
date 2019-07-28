# python
import lx
from multiprocessing import Process
from multiprocessing import Pool
from threading import Thread as worker
from multiprocessing import Pool as cpu_count


##########

def runReStepper():
#	lx.eval("select.drop polygon")
	lx.eval("@z_rstep2_2_working.py")

if __name__ == '__main__':
	import multiprocessing as mp
	n_cores = mp.cpu_count()
	runReStep = lx.eval("@z_rstep2_2_working.py")
	runReplayReStep = lx.eval("@z_reStep_ReplayReStepScript.py")
	dropPoly = lx.eval("select.drop polygon")
	myList = [1]

	pool = Pool(processes=n_cores)
	pool.map(runReStep, myList, chunksize=1)
	
	
'''
if __name__ == '__main__':
	import multiprocessing as mp
	n_cores = mp.cpu_count()
	p = mp.Pool(n_cores)
	p.map(runReplayReStep, range(n_cores))
        
     
#    pool.map(runReStep, myList)
#	pool = Pool(processes=7)
#    p = Process(target=runReStep, args=('bob','2','3'))
#    p.start()
#    p.join()
    
#    for num in range(5):
  #      Process(target=runReStep).start()
#	pool = Pool(processes=4)
#	pool.map(runReStep, myList)


#	pool.apply_async(runReStep, ()) for i in range(4)]
    # launching multiple evaluations asynchronously *may* use more processes
    







#if __name__ == '__main__':
pool = Pool(8)
	
myList = [1,2,3,4,5]

for i in range (1, (lx.eval("user.value zReStep_replayRestep ?")+1)) :
	#pool.map(runReStep, myList)
#	lx.eval("@z_reStep_RandomizeFields.py")

#for i in range (1, (lx.eval("user.value zReStep_replayRestep ?")+1)) :
#pool.map(runReStep, myList)
#pool.close()
#pool.join()
'''







'''
if __name__ == '__main__':
    p = Process(target=f, args=('bob',))
    p.start()
    p.join()
    
   


'''
'''
def run_MultiPros(function, variables):
    """<function, variables> Execute a process on multiple processors.
    INPUTS:
    function(required) Name of the function to be executed.
    variables(required) Variable to be passed to function.
    Description: This function will run the given fuction on to multiprocesser. Total number of jobs is equal to number of variables.        
    """
    
    pool.map(function, variables)
    pool.close()
    pool.join()



run_MultiPros(runReStep,myList)

#pool = Pool(8)

#for i in range (1, (lx.eval("user.value zReStep_replayRestep ?")+1)) :
#	lx.eval("@z_rstep2_2_working.py")


def info(title):
    print(title)
    print('module name:', __name__)
    print('parent process:', os.getppid())
    print('process id:', os.getpid())

def f(name):
    info('function f')
    print('hello', name)

if __name__ == '__main__':
    info('main line')
    p = Process(target=f, args=('bob')
    p.start()
    p.join()
    
'''
import os
import imp
import time
import sys
from traceback import print_exc

def appendIfEuler(problemList, p):
    if p.isdigit():
	problemList.append('euler' + p + '.py')
    elif p[:5] == 'euler' and p[5:].isdigit():
	problemList.append(p + '.py')
    elif p[:5] == 'euler' and p[5:-3].isdigit() and p[-3:] == '.py':
	problemList.append(p)

exitCommands = ['e', 'exit', 'q', 'quit']
displayCommands = ['d', 'display', 'show']
solveCommands = ['s', 'solve']
timeCommands = ['t', 'time']
helpCommands = ['h', 'help']
allCommands = displayCommands + solveCommands + timeCommands

helpMessage = \
'Available commands:\n' + \
'\texit - close the Euler shell\n' + \
'\tdisplay [#]+ - show the problem text for the specified problem(s)\n' + \
'\tsolve [#]+ - solve and print the answer for the specified problem(s)\n' + \
'\ttime [#]+ - time the computations for the specified solution(s)\n'

print
print '************************************************************************'
print 'Welcome to the interactive dynamic shell for my Project Euler solutions.'
print '  I eagerly await your input.'
print '************************************************************************'

cont = True
while cont:
    action = ''
    problem = []
    command = raw_input('$> ').lower().split(None)
    if len(command) > 0:
        if command[0] in exitCommands:
	    cont = False
    	elif command[0] in helpCommands:
	    print helpMessage
    	elif command[0] in allCommands:
	    for n in command[1:]:
	        appendIfEuler(problem, n)
	    action = command[0]
        else:
	    for n in command:
	        appendIfEuler(problem, n)
	    if len(problem) > 0:
	        action = solveCommands[0]

        for p in problem:
	    try:
	        # load the desired solution.  If it's already been loaded,
	        #   reload it!
	        mod = sys.modules.get('solutions.' + p[:-3], None)
	        if mod == None:
	            __import__('solutions.' + p[:-3])
	            mod = sys.modules['solutions.' + p[:-3]]
	        else:
		    reload(mod)
	    except ImportError:
	        print '  File ' + p + ' could not be loaded.'
	    else:
	        try:
 		    if action in displayCommands:
		        print mod.display(None)
	            elif action in solveCommands:
		        print '  ' + str(mod.solve(None))
	            elif action in timeCommands:
		        startTime = time.clock()
		        result = mod.solve(None)
		        t = '{0:.3f}'.format(time.clock() - startTime)
		        print '  ' + str(result) + '  (' + t + ' seconds)'
                except Exception, e:
		    print 'An exception was raised during execution:'
		    print_exc()
	        except SyntaxError, e:
		    print 'A syntax issue was discovered during execution:'
		    print_exc()

    
print "Thank you for using the Euler Shell.  Have a splendid day."


# Class definition:
#   ExperimentFactory
#   This class is used to generate Experiment class objects corresponding to a given "experiment"
#   Based the on Factory Design Pattern
#   Note: not compatible with Singleton Design Pattern due to the subclassing

from types import TypeType
from RunJobMain import RunJobMain
from RunJobEvent import RunJobEvent
from RunJobHPC import RunJobHPC
from RunJobTitan import RunJobTitan

class RunJobFactory(object):

    def newRunJob(self, type="generic"):
        """ Generate a new site information object """

        # get all classes
        runJobClasses = [j for (i,j) in globals().iteritems() if isinstance(j, TypeType) and issubclass(j, RunJobMain)]

        # loop over all subclasses
        for runJobClass in runJobClasses:
            si = runJobClass()

            # return the matching RunJob class
            if si.getRunJob() == type:
                return runJobClass

        # if no class was found, raise an error
        raise ValueError('RunJobFactory: No such class: "%s"' % (type))

if __name__ == "__main__":

    factory = RunJobFactory()

    types = ['Normal', 'EventService', 'HPC', 'Titan', 'Dummy']

    for t in types:
        print "\nAttempting to get class for type", t
        try:
            runJobClass = factory.newRunJob(t)
        except Exception, e:
            print e
        else:
            rJ = runJobClass()
            print 'got runJob:',rJ.getRunJob()
            print 'file name:', rJ.getRunJobFileName()
            del runJobClass


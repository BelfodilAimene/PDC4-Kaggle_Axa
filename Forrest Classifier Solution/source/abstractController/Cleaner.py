from abc import ABCMeta, abstractmethod

class Cleaner(object) :

    __metaclass__ = ABCMeta

    @abstractmethod
    def clean(self,trace) :
        """
        input :
            trace : list of event
        output :
            cleanedTrace : list of event cleaned
        """
        pass

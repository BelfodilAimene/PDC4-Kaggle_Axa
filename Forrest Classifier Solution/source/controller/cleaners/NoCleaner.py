from ...abstractController.Cleaner import Cleaner

class NoCleaner(Cleaner) :
    def clean(self,trace) :
        return trace

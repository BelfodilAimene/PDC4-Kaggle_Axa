class Event :
    def __init__(self,t,x,y) :
        self.t=t
        self.x=x
        self.y=y

    def distance(self,other,p=2) :
        """
        return the p-minkowski distance between the two points
        """
        return ((self.x-other.x)**p+(self.y-other.y)**p)**(1./p)

    def delai(self,other) :
        return abs(self.t-other.t) 
    
    def __str__(self) :
        return "({0} : {1},{2})".format(self.t,self.x,self.y)
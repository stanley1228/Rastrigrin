#
# Individual.py
#
#

import math

#integer vecotr Individual class
class Individual:
    """
    Individual
    """
    minSigma=1e-100
    maxSigma=1
    learningRate=1
    minLimit=None
    maxLimit=None
    uniprng=None
    normprng=None
    fitFunc=None
    dimension=None#stanley
   
    

    def __init__(self):

        #vector of integer stanley
        self.x=[]
        for i in range(self.dimension):
            self.x.append(self.uniprng.uniform(self.minLimit,self.maxLimit))
            
        self.fit=self.__class__.fitFunc(self.x,self.dimension)
        self.sigma=self.uniprng.uniform(0.9,0.1) #use "normalized" sigma
    
    #multiply integer to vector
    #def mul_c_2_arr(self,c,arr): 
    #    for i in range(len(arr)):
    #        arr[i]=round(c*arr[i])#remove the float
    #        if arr[i] > self.maxLimit:
    #            arr[i]=self.maxLimit        
    #    return arr

    #multiply float to vector
    def mul_c_2_arr(self,c,arr): 
        for i in range(len(arr)):
            arr[i]=c*arr[i]
            if arr[i] > self.maxLimit:
                arr[i]=self.maxLimit    
            elif arr[i] < self.minLimit:    
                arr[i]=self.minLimit     
        return arr
    
    def add_vec(self,vec_a,vec_b):
        vec_ans=[]
        for i in range(len(vec_a)):
            vec_ans.append(vec_a[i]+vec_b[i])
        return vec_ans           

    def crossover(self, other):
        #perform crossover "in-place"
        alpha=self.uniprng.random()
        
        #stanley
        vec_a=self.mul_c_2_arr(alpha,self.x)
        vec_b=self.mul_c_2_arr((1-alpha),other.x)
        self.x=self.add_vec(vec_a,vec_b)

        vec_a=self.mul_c_2_arr(1-alpha,self.x)
        vec_b=self.mul_c_2_arr(alpha,other.x)
        other.x=self.add_vec(vec_a,vec_b)
        
        #original
        #self.x=self.x*alpha+other.x*(1-alpha)
        #other.x=self.x*(1-alpha)+other.x*alpha
        self.fit=None
        other.fit=None
    
    
    def mutate(self):
        self.sigma=self.sigma*math.exp(self.learningRate*self.normprng.normalvariate(0,1))
        if self.sigma < self.minSigma: self.sigma=self.minSigma
        if self.sigma > self.maxSigma: self.sigma=self.maxSigma

        #stanley
        ####for float####
        for i in range(self.dimension):          
            self.x[i]=self.x[i]+(self.maxLimit-self.minLimit)*self.sigma*self.normprng.normalvariate(0,1);
            if self.x[i]>self.maxLimit: self.x[i]=self.maxLimit
            elif self.x[i]<self.minLimit: self.x[i]=self.minLimit

        #stanley
        ####for integer####
        #for i in range(self.latticeLength):          
        #    self.x[i]=self.x[i]+(self.maxLimit-self.minLimit)*self.sigma*self.normprng.normalvariate(0,1);
        #    self.x[i]=round(self.x[i])#remove the float
        #    if self.x[i] < 0: #prevent negtive
        #        self.x[i]=-self.x[i]       
        #    if self.x[i]>self.maxLimit: self.x[i]=self.maxLimit
        
        #original
        #self.x=self.x+(self.maxLimit-self.minLimit)*self.sigma*self.normprng.normalvariate(0,1)  
        self.fit=None
    
    def evaluateFitness(self):
        #stanley
        if self.fit == None: self.fit=self.__class__.fitFunc(self.x,self.dimension)
        
    def __str__(self):
        #original
        #return '%0.8e'%self.x+'\t'+'%0.8e'%self.fit+'\t'+'%0.8e'%self.sigma

        str='['
        for i in range(self.dimension):
            if i!=(self.dimension-1):
                str=str+'%12.8f,'%self.x[i]
            else:
                str=str+'%12.8f'%self.x[i]
        str=str+']'+'\t'
        str=str+'%12.8f'%self.fit+'%10.2f'%self.sigma

        return str

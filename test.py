import numpy as np
import pylab as plt
import bspline as bsp
    
flag_bspline = False
type_ = 4
if flag_bspline:
    """
B-splines
    """
    #[1] Finite Element Methods with exact geometry representation
    #    IsoGeometric Analysis, NURBS Enhanced Finite Element Method
    #       and AnisoGeometric Analysis
    #   Dennis Ernens
    
    #[2] ISOGEOMETRIC ANALYSIS TOWARD INTEGRATION OF CAD AND FEA
    #   J. Austin Cottrell, Thomas J. R. Hughes, Yuri Bazilevs
    
    if type_ == 0:
        # [1] figure 2.5
        Px = np.array([1,0,1,2,3,3,1,0])
        Py = np.array([0,1,2,1,1,2,3,2])
        knots = np.array([0,0,0,1,2,3,4,4,5,5,5],dtype = float)
        p = 2
    elif type_ == 1:
        # [1] figure 2.7
        Px = np.array([ 2.0, 3.0, 5.0, 4.0 , 2.0, 2.0, 0.0])
        Py = np.array([-1.0,-2.0, 0.0, 2.0 , 2.0, 0.0, 0.0])
        knots = np.array([0,0,0,0,1,2,3,4,4,4,4],dtype = float)
        p = 3
    elif type_ == 2:
        # [1] figure 2.7
        Px = np.array([ 2.0, 3.0, 4.5, 4.5, 3.5, 2.0, 2.0, 0.0])
        Py = np.array([-1.0,-2.0,-0.5, 1.0, 2.0, 2.0, 0.0, 0.0])
        knots = np.array([0,0,0,0,1,2,2.5,3,4,4,4,4],dtype = float)
        p = 3
    elif type_ == 3:
        # [2] 2.19
        Px = np.array([0.0,0.5,1.0])
        Py = np.array([0.0,1.0,0.0])
        knots = np.array([0,0,0,1,1,1],dtype = float)
        p = 2    
    elif type_ == 4:
        # [2] 2.191
        Px = np.array([0.00,0.25,0.75,1.00])
        Py = np.array([0.00,0.50,0.50,0.00])
        knots = np.array([0,0,0,0.5,1,1,1],dtype = float)
        p = 2    
        
        
    plt.clf()
    plt.subplot(2,1,1)
    plt.axis('equal')
    x = np.linspace(knots[0],knots[-1],401)
    for i in range(Px.shape[0]):
        NN = np.zeros(x.shape[0])
        for ii in range(x.shape[0]):
            NN[ii] = bsp.N_i_p(knots,i,p,x[ii])
        plt.plot(x[1::],NN[1::])    
        if i == 0:
            X = NN * Px[i]
            Y = NN * Py[i]
        else:
            X += NN * Px[i]
            Y += NN * Py[i]        
    plt.subplot(2,1,2)
    plt.plot(X[1::],Y[1::])
    plt.plot(Px,Py,'--o')
    plt.axis('equal')
    plt.show()    
else:
    """
    NURBS
    """
    sqr2 = np.sqrt(2.)*0.5
    Px = np.array([ 1.0, 1.0, 0.0,-1.0,-1.0,-1.0, 0.0, 1.0, 1.0])
    Py = np.array([ 0.0,-1.0,-1.0,-1.0, 0.0, 1.0, 1.0, 1.0, 0.0])
    w  = np.array([ 1.0,sqr2, 1.0,sqr2, 1.0,sqr2, 1.0,sqr2, 1.0])
    knots = np.array([0,0,0,1,1,2,2,3,3,4,4,4],dtype = float)
    p = 2
       
    plt.clf()
    plt.subplot(2,1,1)
    plt.axis('equal')
    x = np.linspace(knots[0],knots[-1],301)
    for i in range(Px.shape[0]):
        NN = np.zeros(x.shape[0])
        for ii in range(x.shape[0]):    
            sum0 = 0.0
            for i2 in range(Px.shape[0]):
                sum0 += bsp.N_i_p(knots,i2,p,x[ii]) * w[i2]
            NN[ii] = bsp.N_i_p(knots,i,p,x[ii]) * w[i] / sum0
        plt.plot(x[1::],NN[1::])    
        if i == 0:
            X = NN * Px[i]
            Y = NN * Py[i]
        else:
            X += NN * Px[i]
            Y += NN * Py[i]      
    plt.subplot(2,1,2)
    plt.plot(X[1::],Y[1::])
    plt.plot(Px,Py,'--o')
    plt.axis('equal')
    plt.show()    




import numpy as np
from scipy.linalg import expm

def skew_sym(om,v): #returns the skew symmetric form of the matrix given the omega and v vectors
	skew_mat = np.array([[0,-om[2],om[1],v[0]],
				[om[2],0,-om[0],v[1]],
				[-om[1],om[0],0,v[2]],
				[0,0,0,0]])
	return skew_mat

def Get_T():
	theta = [0,0,90*np.pi/180,0,-90*np.pi/180,0] # joint angles for desired configuration
	beta = .1125/120 #conversion factor from mm of robot to units in CoppeliaSim
	M = np.array([[0, 0, 1, -192*beta - .05],
		[0, -1, 0, 0],
		[1, 0, 0, 692*beta],
		[0, 0, 0, 1]])

	## JOINT 1 ##
	om1 = np.array([0, 0,1])
	q1 = np.array([0,0,0])
	v1 = np.cross(-om1,q1)
	s1 = skew_sym(om1,v1)

	## JOINT 2 ##
	om2 = np.array([-1,0,0])
	q2 = np.array([-120*beta,0,152*beta])
	v2 = np.cross(-om2,q2)
	s2 = skew_sym(om2,v2)

	## JOINT 3 ##
	om3 = np.array([-1,0,0])
	q3 = np.array([-120*beta,0,396*beta])
	v3 = np.cross(-om3,q3)
	s3 = skew_sym(om3,v3)

	## JOINT 4 ##
	om4 = np.array([-1,0,0])
	q4 = np.array([-27*beta,0,609*beta])
	v4 = np.cross(-om4,q4)
	s4 = skew_sym(om4,v4)

	## JOINT 5 ##
	om5 = np.array([0,0,1])
	q5 = np.array([-110*beta,0,609*beta])
	v5 = np.cross(-om5,q5)
	s5 = skew_sym(om5,v5)

	## JOINT 6 ##
	om6 = np.array([-1,0,0])
	q6 = np.array([-110*beta,0,692*beta])
	v6 = np.cross(-om6,q6)
	s6 = skew_sym(om6,v6)

	T = expm(s1*theta[0]).dot(expm(s2*theta[1])).dot(expm(s3*theta[2])).dot(expm(s4*theta[3])).dot(expm(s5*theta[4])).dot(expm(s6*theta[5])).dot(M)
	print(T)
	return T

Get_T()
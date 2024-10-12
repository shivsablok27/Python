# Writing a dictionary in binary mode.
import pickle

ob=open("F23.dat","wb")

d={'Rajat' : {'Physics':89,'Chemistry':85,'Math':84},
   'Jatin' : {'Physics':81,'Chemistry':91,'Math':92},
   'Amreek': {'Physics':85,'Chemistry':95,'Math':91}}

pickle.dump(d,ob)
ob.close()
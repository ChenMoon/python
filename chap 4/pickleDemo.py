import pickle


with open( 'mydata.pickle','wb' ) as mysavedata:
    pickle.dump( ['1','2','Three'],mysavedata )
with open( 'mydata.pickle','rb' ) as myrestoredata:
    the_list = pickle.load( myrestoredata )
print( the_list )
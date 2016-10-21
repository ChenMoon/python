
movies = [ "The Holy Grail",1975,"Terry Jones & Terry Gilliam",91,
           [ "Graham Chapman",[ "Michael Palin","John Cleese","Terry Gilliam","Eric Idle","Terry Jones" ]]]
#print( movies )

'''
for each_item in movies:
    print( each_item )
'''

for each_item in movies:
    if isinstance( each_item,list ):
        for inner_item in each_item:
            if isinstance( inner_item,list ):
                for deeper_item in inner_item:
                    print( deeper_item )
            else:
                print( inner_item )
    else:
        print( each_item )
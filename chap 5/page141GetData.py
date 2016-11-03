
def sanitize( time_string ):
    if '-' in time_string:
        splitter = '-'
    elif ':' in time_string:
        splitter = ':'
    else:
        return( time_string )
    ( mins,secs ) = time_string.split(splitter)
    return( mins+'.'+secs )

def sort_list( time_string):
    new_time_string = []
    for each in time_string:
        new_time_string.append( sanitize( each ) )
    return ( sorted( new_time_string ) )

def sort_list2( time_string ):
    new_time_string = [ sanitize( each ) for each in time_string ]
    return ( sorted( new_time_string ) )

def unique_list( time_string ):
    unique_string = [  ]
    for t in time_string:
        if t not in unique_string:
            unique_string.append( t )
    return( unique_string )


with open( 'james.txt' ) as jamesData, open( 'julie.txt' ) as julieData, open( 'mikey.txt' ) as mikeyData, open( 'sarah.txt' ) as sarahData:
    jamesScore = jamesData.readline()
    julieScore = julieData.readline()
    mikeyScore = mikeyData.readline()
    sarahScore = sarahData.readline()

james = jamesScore.strip().split( ',' )
julie = julieScore.strip().split(',')
mikey = mikeyScore.strip().split(',')
sarah = sarahScore.strip().split(',')

print( unique_list( sort_list( james ) )[ 0:3 ] )
print( unique_list( sort_list( julie ) )[ 0:3 ] )
print( unique_list( sort_list( mikey ) )[ 0:3 ] )
print( unique_list( sort_list( sarah ) )[ 0:3 ] )

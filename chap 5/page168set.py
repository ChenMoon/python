def sanitize( time_string ):
    if '-' in time_string:
        splitter = '-'
    elif ':' in time_string:
        splitter = ':'
    else:
        return( time_string )
    ( mins,secs ) = time_string.split(splitter)
    return( mins+'.'+secs )

def with_fun( file ):
    try:
        with open( file ) as fl:
            file_data = fl.readline()
        return( file_data.strip().split( ',' ) )
    except IOError as err:
        print( 'IOError: '+str() )
        return None

with open( 'james.txt' ) as jamesData, open( 'julie.txt' ) as julieData, open( 'mikey.txt' ) as mikeyData, open( 'sarah.txt' ) as sarahData:
    jamesScore = jamesData.readline()
    julieScore = julieData.readline()
    mikeyScore = mikeyData.readline()
    sarahScore = sarahData.readline()

james = jamesScore.strip().split( ',' )
julie = julieScore.strip().split(',')
mikey = mikeyScore.strip().split(',')
sarah = sarahScore.strip().split(',')

print( sorted( set( [ sanitize( t ) for t in james ] ) ) [ 0:3 ] )
print( sorted( set( [ sanitize( t ) for t in julie ] ) ) [ 0:3 ] )
print( sorted( set( [ sanitize( t ) for t in mikey ] ) ) [ 0:3 ] )
print( sorted( set( [ sanitize( t ) for t in sarah ] ) ) [ 0:3 ] )

print( '***this is another function***' )

print( sorted( set( [ sanitize( t ) for t in with_fun( 'james.txt' ) ] ) ) [ 0:3 ] )
print( sorted( set( [ sanitize( t ) for t in with_fun( 'julie.txt' ) ] ) ) [ 0:3 ] )
print( sorted( set( [ sanitize( t ) for t in with_fun( 'mikey.txt' ) ] ) ) [ 0:3 ] )
print( sorted( set( [ sanitize( t ) for t in with_fun( 'sarah.txt' ) ] ) ) [ 0:3 ] )
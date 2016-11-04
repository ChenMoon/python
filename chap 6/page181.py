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

sarah = with_fun( 'sarah2.txt' )
sarah_dict = dict( )
( sarah_dict['name'],sarah_dict['dob'] ) = sarah.pop( 0 ),sarah.pop( 0 )
sarah_dict['time'] = sarah
print( sarah_dict['name'] + 's fastest time are: ' + str( sorted( set( [ sanitize( t ) for t in sarah_dict['time'] ] ) )[0:3] ) )

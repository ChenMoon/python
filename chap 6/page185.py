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
        file_data_dict = dict()
        file_data_dict['name'] = file_data.strip().split( ',' ).pop( 0 )
        #print( file_data_dict['name'] )
        file_data_dict['birthday'] = file_data.strip().split( ',' ).pop( 1 )
        #print(file_data_dict['birthday'])
        file_data_dict['times'] = file_data.strip().split( ',' )[2:]
        #print(file_data_dict['times'])
        file_data_dict['bestTimes'] = sorted( set( [ sanitize( t ) for t in file_data_dict['times'] ] ) )[0:3]
        return( file_data_dict )
    except IOError as err:
        print( 'IOError: '+str() )
        return None

sarah = with_fun( 'sarah2.txt' )
#print( sarah['times'] )
print( sarah['name'] + 's fastest time are: ' + str( sarah['bestTimes'] ) )
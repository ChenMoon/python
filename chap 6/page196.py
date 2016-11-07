def sanitize( time_string ):
    if '-' in time_string:
        splitter = '-'
    elif ':' in time_string:
        splitter = ':'
    else:
        return( time_string )
    ( mins,secs ) = time_string.split(splitter)
    return( mins+'.'+secs )

class Athlete:
    def __init__( self,a_name, a_birthday = None, a_times = [] ):
        self.name = a_name
        self.birthday = a_birthday
        self.times = a_times
    def top3(self):
        return ( sorted( set( [ sanitize( t ) for t in self.times ] ) )[0:3] )
    def add_time( self , add_timestring = '' ):
        self.times.append( add_timestring )
    def add_times( self , add_timestring = [] ):
        self.times.extend( add_timestring )

def with_fun( file ):
    try:
        with open( file ) as fl:
            file_data = fl.readline()
        athlete = Athlete('')
        athlete.name = file_data.strip().split( ',' ).pop( 0 )
        #print( file_data_dict['name'] )
        athlete.birthday = file_data.strip().split( ',' ).pop( 1 )
        #print(file_data_dict['birthday'])
        athlete.times = file_data.strip().split( ',' )[2:]
        #print(file_data_dict['times'])
        return( athlete )
    except IOError as err:
        print( 'IOError: '+str() )
        return None



sarah = with_fun( 'sarah2.txt' )
print( sarah.name + 's fastest time are: ' + str( sarah.top3() ) )
sarah.add_time( '0:13' )
sarah.add_times( ['0-11','0.12'] )
print( str( sarah.top3() ) )
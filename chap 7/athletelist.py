def sanitize( time_string ):
    if '-' in time_string:
        splitter = '-'
    elif ':' in time_string:
        splitter = ':'
    else:
        return( time_string )
    ( mins,secs ) = time_string.split(splitter)
    print( '执行sanitize' )
    return( mins+'.'+secs )

class AthleteList( list ):
    def __init__( self,a_name = '', a_birthday = '', a_times = [] ):
        list.__init__([])
        self.name = a_name
        self.birthday = a_birthday
        self.extend( a_times )
    def top3(self):
        print('执行top3')
        return ( sorted( set( [ sanitize( t ) for t in self ] ) )[0:3] )
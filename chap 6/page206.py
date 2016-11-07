def sanitize( time_string ):
    if '-' in time_string:
        splitter = '-'
    elif ':' in time_string:
        splitter = ':'
    else:
        return( time_string )
    ( mins,secs ) = time_string.split(splitter)
    return( mins+'.'+secs )
class Athlete(list):
    def __init__( self,a_name, a_birthday = None, a_times = [] ):
        list.__init__([])
        self.name = a_name
        self.birthday = a_birthday
        self.extend( a_times )
    def top3(self):
        return ( sorted( set( [ sanitize( t ) for t in self ] ) )[0:3] )

vera = Athlete('vera vi')
vera.append('1.31')
print(vera.top3())
vera.extend(['2.22','1-21','2:23'])
print(vera.top3())
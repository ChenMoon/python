import pickle
from athletelist import AthleteList

def with_fun( file ):
    try:
        with open( file ) as fl:
            file_data = fl.readline()
        athlete = AthleteList('')
        tempAthlete = file_data.strip().split( ',' )
        #print( 'tempAthlete' + str(tempAthlete) )
        athlete.name = tempAthlete.pop( 0 )
        #print( athlete.name )
        athlete.birthday = tempAthlete.pop( 0 )
        #print( athlete.birthday )
        athlete.times = tempAthlete
        #print( athlete.times )
        #print('执行with_fun')
        #print( 'athletes '+ str(athlete) )
        return( athlete )
    except IOError as err:
        print( 'IOError: '+str() )
        return None

def put_to_store( files_list ):
    all_athlete = { }
    for each_file in files_list:
        ath = with_fun( each_file )
        all_athlete[ ath.name ] = ath
        print( ath.name )
    #print('执行put_to_store:with_fun')
    try:
        with open( 'athletes.pickle','rb' ) as athf:
            print('执行put_to_store:写入pickle')
            pickle.dump( all_athlete , athf )
    except IOError as ioerr:
        print( 'File error(put_and_store):'+ str( ioerr ) )

def get_from_store( ):
    all_athletes = { }
    try:
        with open( 'athletes.pickle','wb' ) as athf:
            all_athletes = pickle.load( athf )
    except IOError as ioerr:
        print( 'File error(get_from_store):'+ str( ioerr ) )
    return ( all_athletes )

the_files = [ 'sarah2.txt','james2.txt','mikey2.txt','julie2.txt' ]
data = put_to_store(the_files)
print( str(data) )
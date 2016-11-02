import nester
import pickle

man = []
other = []
new_man = []
try:
    the_file = open( '..//chap 3//sketch.txt' )
    for each_line in the_file:
        try:
            if each_line.find( ':' )>= 1:
                ( role,line_spoken ) = each_line.split( ':',1  )
                line_spoken = line_spoken.strip()
                if role == 'Man':
                    man.append( line_spoken )
                elif role == 'Other Man':
                    other.append( line_spoken )
        except ValueError:
            pass
    the_file.close()
except IOError as err0:
    print( 'Error'+str(err0) )

try:
    with open( 'man_data.pickle',"wb" ) as man_file:
        pickle.dump( man,man_file )
    with open( 'other_data.pickle','wb' ) as other_file:
        pickle.dump( other,other_file )

except IOError as err:
    print( 'file error '+str(err) )

except pickle.PickleError as perr:
    print( 'pickle error: '+str(perr) )

with open( 'man_data.pickle',"rb" ) as man_file_read:
    man_list = pickle.load( man_file_read )
with open( 'other_data.pickle',"rb" ) as other_file_read:
    other_list = pickle.load(other_file_read)
nester.print_lol( man_list )
print( '--------------' )
nester.print_lol( other_list )
import nester

man = []
other = []
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
    with open( 'man_data.txt',"w" ) as man_file:
        nester.print_lol( man,output=man_file )
    with open( 'other_data.txt','w' ) as other_file:
        nester.print_lol( other,output=other_file )
except IOError as err:
    print( 'file error '+str(err) )
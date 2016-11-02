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
except IOError:
    print( 'the data file may be missing' )

try:
    man_out = open('..//chap 3//man_data.txt', 'w')
    other_out = open('..//chap 3//other_data.txt', 'w')
    print( man,file=man_out )
    print( other,file=other_out )
except IOError:
    print( 'sth is wrong!')
finally:
    man_out.close()
    other_out.close()

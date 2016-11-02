

the_file = open( 'sketch.txt' )
for each_line in the_file:
    if each_line.find( ':' )>= 1:
        ( role,line_spoken ) = each_line.split( ':',1  )
        print( role,end='' )
        print( ' said:',end='' )
        print( line_spoken,end='' )
    else:
        print( each_line,end='' )
the_file.close()
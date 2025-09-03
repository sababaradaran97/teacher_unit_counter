teacher_names = []
teacher_unit_info = []

lesson_list = [ { "lesson_name" : "python" , "unit" : "3" , "teacher" : "ali" } ,
                { "lesson_name" : "c++" , "unit" : "5" , "teacher" : "reza" } ,
                { "lesson_name" : "java" , "unit" : "6" , "teacher" : "ali" } , 
                { "lesson_name" : "python" , "unit" : "3" , "teacher" : "mohsen" }
              ]


for i in range( lesson_list ) : 

    if ["teacher"] in teacher_unit_info :
        teacher_unit_info[ i ][ "teacher_units" ] = teacher_unit_info[ i ][ "teacher_units" ] + lesson_list[ i ][ "unit" ]

    else :
        teacher_unit_info.append ( { "teacher_name" : lesson_list[ i ][ "teacher" ] , "teacher_units" : lesson_list[ i ][ "unit" ] } )

teacher_unit_info = sorted ( teacher_unit_info[ "teacher_name "] )

for i in range( teacher_unit_info ) :
    print ( teacher_unit_info[ i ][ "teacher_name" ] , ":" , teacher_unit_info[ i ][ "teacher_units" ] )


for number in range(101):print( " hop-weez" if not  number % 15 else " hop" if not number % 3 else " weez" if not number % 5 else str( number))
#                                                    {              ^                   }                  {     ^^     }                   {   ^^   }
#                                           ( vojoode ya adame vojoode mazrabe 3,5 ra baresi mikonad)      ( vojood mazrabe 3 ya adame )     ( mazrabe 5 vojood ya adame )








#  hop-weez ba range neveshte shode 
#  PYTHONIC tarin ravesh 
for number in range(101):                                 
  print(" hop-weez" if number in range (15, 101, 15) else " hop" if number in range( 3, 101,3) else" weez"  if number in range(5 , 101,5) else str(number))

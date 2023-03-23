# Import a variable to count the generation
i = 1
print ("Generation ",i)
# Import a variable that carries the number of rabbits
j = 2
print (j)

# Use a while-loop to achieve the output of every generation
while 1==1:
 i += 1
 print ("Generation ",i)
 # The number of rabbits in every generation is the two times of the previous one.
 j = j*2
 print (j)
 if j*2 > 100:
  break
print ("At the",i+1,"th generation over 100 rabbits have been born.")

min_age_at_school = 5
sara_age = input("how old is sara? ")
sara_age =int(sara_age)

# question: can sara go to school?
if (sara_age == min_age_at_school):
    print ("yes, he can go to school")  #indent block


elif(sara_age>=7):
    print("he must go to higher school")

elif(sara_age<=3):
    print("no one should be allowed in his age group!")
else:
    print("No, he can't go to school")    
    
min_age_for_css_exam = 35
ali_age = input("how old are sidra?")
sidra_age = 30

if (sidra_age<35):
   print ("sidra is eligible for css exam")
elif(sidra_age==35):
   print ("it is to be sur she is eligible")
   
else :
    print ("sidra is not eligible")
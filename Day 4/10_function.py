# defining a function
def print_fixstech():
    print ("we are learning python with fixstech")

print_fixstech()
print_fixstech()


#2
# def print_fixstech():
text = "we are learning python with fixstech"
print(text)
print(text)
print(text)

#3

# def print_fixstech(text):
print(text)
print(text)
print(text)


# defining a function with decision capibilities

# def school_calculator(age):
age=5
if ( age == 5):
   print("yes, he can go to school")  #indent block


sana_age = 20
max_age_for_academy =25
sana_age = input ("how old is sana?")

if (sana<=25):
    print ("sana get addmission in academy")
elif(sana==25):
    print ("she get addmission in academy")
else:
    print ("she not get addmission ")
   
#Future prediction

def future_age(age):
    age = age + 10
    return age


#print(future_age(4))
print(future_age(int(input("enter age? "))))
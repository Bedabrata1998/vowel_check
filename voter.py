print('* * * Check your age for Voter ID * * *')
name=input("Enter your fullname-")
age=int(input("Enter age-"))
if age>=18:
    print(name,'You are eligble for voter id')
else:
    print(name,'You are not eligble for voter id')
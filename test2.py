from faker import Faker
faker=Faker()
for i in range(1):
    phno=faker.phone_number()
    print(phno)
    email=faker.email()
    print(email)
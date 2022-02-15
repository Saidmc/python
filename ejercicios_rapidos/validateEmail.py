from validate_email import validate_email
from verify_email import verify_email

print(validate_email("saidmc@gmail.com"))
print(validate_email("saidomc@gmail.com"))
print(validate_email("saidmc@msn.com"))
print(validate_email("saidmc2@gmail.com"))
print(validate_email("saidmc9@gmail.com"))
print(validate_email("saidmc909yuijpk@gmail.com"))

print(verify_email("abczyx@gmail.com"))
print(verify_email("abczyx090998@gmail.com"))
print(verify_email("saidmc2@gmail.com"))
print(verify_email("saidmc909yuijpk@gmail.com"))
print(verify_email("saidomc9@gmail.com"))

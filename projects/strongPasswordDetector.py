import re

password = "1234heLlo heLlo123 yelLo12 yello123 yelloyel yelloYel"


passwordValidation = re.compile(r'^(?=.*[A-Z])(?=.*\d).{8,}$') 

# Split the password string into individual words
passwords = password.split()

# Apply the regex pattern to each password
valid_passwords = [passs for passs in passwords if passwordValidation.match(passs)]

# Print valid passwords
print(valid_passwords)
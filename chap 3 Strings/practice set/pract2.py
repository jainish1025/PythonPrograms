letter = '''Dear <|NAME|>,
Greeting from Code Academy you are selected for over course
Thank you so much for particepement in over cources
Thanks and Regard
Date <|DATE|>'''

name = input("Enter your name\n")
date = input("Enter Date\n")
letter = letter.replace("<|NAME|>", name)
letter = letter.replace("<|DATE|>", date)
print(letter)

"""
1. Dictionaries are mutable
2. Use 'get' to get the value

Set
1. Unorderd list of unique

"""

country_codes = {'usa': 'united states', 'ind': 'India'}

# -------------- Checking if Dictionary is empty --------------------
if country_codes:
    print("country_codes is not empty")
else:
    print("country_codes is empty")

# -------------- Deleting the Dictionary --------------------
country_codes.clear()

country_codes = {'usa': 'united states', 'ind': 'India'}


# -------------- Getting values --------------------
for code, name in country_codes.items():
        print("code ", code, " name ", name)

print(country_codes['usa'])  # This will throw error if key will be missing use get instead
print(country_codes.get('qa'))  # get and return None if missing
print(country_codes.get('usa'), 'Country code is missing')  # get or else


# -------------- To add or update the values --------------------
country_codes['cd'] = 'canada'
country_codes.update({'Brazil': 'br'})  # using update
country_codes.update(Australia='ar')


# -------------- Delete the key value pair --------------------
del country_codes['cd']
country_codes.pop('usa')

country_codes['cd'] = 'canada'
country_codes['usa'] = 'united states'

# -------------- Converting to List ----------------
cntry_code_list = list(sorted(country_codes.items()))
print(cntry_code_list)  # [('cd', 'canada'), ('ind', 'India'), ('usa', 'united states')]






# -------------- Example for the use of Dictionary -------------------------------
# ----- Finding the average temperature of state and country for a week ----------

state_temperature = {
    'Maryland': [18, 16, 19, 20, 21, 23, 21],
    'Virginia': [18, 19, 20, 20, 22, 23, 21],
    'West Virginia': [18, 19, 19, 20, 20, 23, 21]
}
total_count = 0
total_sum = 0

for state, temp in state_temperature.items():
    sum_temp = sum(temp)
    len_temp = len(temp)
    average_temperature_state = sum(temp)/len(temp)
    print ('Average for ', state, ' :', average_temperature_state)
    total_sum += sum_temp
    total_count += len_temp

print('Country average :', total_sum/total_count)





# -------------------------------------------------------------------------------------
# ------------- Word count example --------------------------
text = """
this is text used as a sample for testing word count
count word is sample for python
"""
word_count = {}
for word in text.split():
    if word in word_count:
        word_count[word] += 1  # Add
    else:
        word_count[word] = 1  # Insert

print(word_count)


# -------------------------------------------------------------------------------------
# -----------------------------SETS--------------------------------------------------------
# -------------------------------------------------------------------------------------
"""
SET OPERATORS
|=  Update
&=  intersection update
-=  difference update
^=  symmetric_difference_update
"""

# Checking if subset
print({1, 3, 5}.issubset({3, 5, 1}))  # Output True
print({1, 3, 5} > {3, 5, 1})  # Output False
print ({1, 3, 5} & { 2, 3, 7 })  # Output 3
print ({1, 3, 5} | { 2, 3, 7 })  # {1, 2, 3, 5, 7}

numbers = [1, 2, 3, 4, 5, 5, 6, 7]
even_number = {item for item in numbers if item % 2 == 0 }


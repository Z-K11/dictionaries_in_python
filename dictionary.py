# Create a dictionary in python by
dictionary = {"key1":1,"key2":1,"key3":3,"key4":[2,3,4],5:23,(0,1):[5,4]}
# Acessing the dictionary using string key
print(dictionary["key4"])
# Accessing the dictionary using tuple key
print(dictionary[(0,1)])
# Create a sample dictionary

release_year_dict = {"Thriller": "1982", "Back in Black": "1980", 
                    "The Dark Side of the Moon": "1973", "The Bodyguard": "1992", 
                    "Bat Out of Hell": "1977", "Their Greatest Hits (1971-1975)": "1976", 
                    "Saturday Night Fever": "1977", "Rumours": "1977"}
# Access the value of dictionary by key
print(release_year_dict["Bat Out of Hell"])
# Printing the keys of the dictionary using .keys() function
print(release_year_dict.keys())
# Accessing the values of the dictionary using .values() function
print(release_year_dict.values())
#
import json

#
data1 = {

    'name': 'OJ Simpson',
    'age': 30,
    'city': 'New York, NY',
    'interests': ['Traveling','Football','Golf','Running','Videogames','History'],
    'is_student':False

}


#
with open('data1.json','w') as json_file:

    #Dump the Data Dictionary into the JSON file.
    json.dump(data1,json_file,indent=4)

print("You have successfully written to data1.json")

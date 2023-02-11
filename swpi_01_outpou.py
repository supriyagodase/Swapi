import requests
home_url = "https://swapi.dev"
relative = "/api/films/1/"
absolute_url = home_url + relative
name = requests.get(absolute_url)
new_name=name.json()

print(new_name)

with open("output.txt",'w') as file_obj:
    print("write in data into file")
    file_obj.write(str(new_name))

char_url=new_name['characters']
# print(char_url)
char_list=[]
for i in char_url:
    char_result = requests.get(i)
    char_res=char_result.json()
    # print(char_res)
    char_list.append(char_res['name'])

print(f"char in swapi",char_list)

planet_name=new_name['planets']
planet_url = []
for i in planet_name:
    planet_data = requests.get(i)
    planet_data_2 = planet_data.json()
    planet_url.append(planet_data_2['name'])
print(f"planet in swapi",planet_url)




vehicle_url= new_name['vehicles']
# print(vehicle_url)
vehicle_name = []
for i in vehicle_url:
    vehicle_data = requests.get(i)
    vehical_data2 =vehicle_data.json()
    # print(vehical_data2)
    vehicle_name.append(vehical_data2['name'])

print(f"vehicle in swapi",vehicle_name)




    # char_list.append(char_res[])
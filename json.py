import json 

# WORKING WITH A JSON FILE

def Suman(file):
    with open(file, 'r') as file:
        data = json.load(file)
        for i in data:
            if(i['state']=='BIHAR'):
                print(i['office_name'])
                print(i['pincode'])
                
# WORKING WITH A JSON FILE

def Guvi(file):
    file=open(file, 'r')
    data = json.load(file)
    for i in data:
        if(i['taluk']=='Phulwari'):
            print(i['office_name'])
            print(i['pincode'])

Guvi('india.json')

Notes  = {
    "Juan" : 2.5,
    "Emmanuel" : 5.0,
    "Oscar" : 4.2,
    "Felipe" : 0.2,
    "Pedro" : 3.0

}

new_dicci = {}

for i in Notes.items():
    if i[1] >= 3.0:
        new_dicci.update({i[0] : i[1]})
    
print(new_dicci)
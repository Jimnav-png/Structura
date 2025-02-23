import json


with open("terrain_texture.json") as file:
    oldData=json.load(file)
with open("terrain_texture_18.json") as file:
    newData=json.load(file)

oldKeys=list(oldData["texture_data"].keys())
newKeys=list(newData["texture_data"].keys())

newBlocks = list(filter(lambda i: i not in oldKeys, newKeys))
for key in newBlocks:
    oldData["texture_data"][key]=newData["texture_data"][key]

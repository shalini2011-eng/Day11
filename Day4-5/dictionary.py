mydict = {
    "brand" : "Ford",
    "model" : "Mustang",
    "year": 1964
}

# mydict2= mydict.copy()
mydict2 = dict(mydict)
mydict["color"] = "red"
print("mydict values are ", mydict)
print ("mydict2 values are", mydict2)

# print(len(mydict))
# mydict ["color" ]= "red"
#mydict.pop("brand")
# del mydict["Mustang"]
# mydict.clear()
# print(mydict)
# print( " model values are:", mydict["model"])
# print("year value is :",mydict.get("year"))
#
# mydict["year"] = 2020
# print(mydict["year"])

# for dict in mydict.values():
#     print(dict)

# for keys,values in mydict.items():
#     print(keys, ":",values)

# if "model" in mydict:
#     print("model available")
#A dictionary can contain dictionaries, this is called nested dictionaries.
myfamily={
      "child1":{
            "name":"Akash",
            "age":25,
            "number":101
      },
      "child2":{
            "name":"Meghla",
            "age":15,
            "number":102
      },
      "child3":{
            "name":"Ritu",
            "age":25,
            "number":103
      },
}

# print("Nested Dictionary:",myfamily)
#Accessing Items from Nested Dictionary
# print("Name of Child 2:",myfamily["child2"]["name"])
# print("Age of Child 3:",myfamily["child3"]["age"])

#You can loop through a dictionary by using the items() method like this:
for child_num,child_info in myfamily.items():
      print(child_num)
      for key in child_info:
            print("\t",key,":",child_info[key])


#Different way to make nested dictionary
child1={
      "name":"Akash",
      "age":25,
      "number":101
}
child2={
      "name":"Meghla",
      "age":15,
      "number":102
}
child3={
      "name":"Ritu",
      "age":25,
      "number":103
}
myfamily2={
      "child1":child1,
      "child2":child2,
      "child3":child3
}

# print("Nested Dictionary 2:",myfamily2)

for child_num,child_info in myfamily.items():
      print("\n*******",child_num,"*******")
      for key in child_info:
            print("\t",key,":",child_info[key])
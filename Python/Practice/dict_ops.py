d={"Name":"Manoj","Age":24,"City":"Hyd"}
print(d)
d["motherName"]="Rama"
d.update({"FatherName":"Pururshotham"})
print(d)

if "Name" in d:
    if "Age" in d.keys():
        if "Rama" in d.values():
            print("ALL")

myData = {
    "Calibration curve" : [[2,4],[5,7.2]],
    "Constant" : 8,
    "Input parameters" : {
        "param1" : 5,
        "param2" : 6,
        "param3" : 7,
        4135059582 : "mike strain" # you can actually define a number as a key, but it just makes things confusing...
    }
}

print(myData["Calibration curve"][0][0])

print(myData["Input parameters"])

myData["Input parameters"].pop("param3")

print(myData["Input parameters"])

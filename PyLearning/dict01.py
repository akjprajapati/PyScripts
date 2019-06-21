name_for_id = {
    100: "OpsZero",
    101: "OpsOne",
    102: "OpsTechie",
}

def greeting(id):
    return "Hi %s!" % name_for_id.get(id, "there, this ID doesn't exist.")



print (greeting(100))
print (greeting(101))
print (greeting(102))
print (greeting(103))


#Ask for value
#create list of devices
dev_list=["device1", "device2","device3","device4"]

dev_list_1={"device_name":"switch", "os_type":"ios 15.x"}

# #loop over dev_list an dprint result
# for device in dev_list:
#     print("this is device:{}".format(device))
#     #check if device1 is in this list
#     if "device1" in device:
#         print("We found device1")
#     else:
#         print("Device1 was not found")

# for k, v in dev_list_1.items():
#     print(k,v)
#     if "ios" in v:
#         print("we found the ios")
#     else:
#         print(":(")

for value in dev_list_1["os_type"]:
    if "ios" in value:
        print("This is the ios")
    else:
        print(":(")


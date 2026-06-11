name = "Bharath"
age = 30
marks=87.9
is_Active = True

print(name)
print(type(age))

#quote = input("Provide a quote:")
#print(quote)

role="Senior SRE"
print(role.upper())
print(role.lower())

print(len(role))
print(role.split())
print(role.replace("SRE","DevOps"))

servers = ["web1","web2","web3"]

print(servers[0])

servers.append("web4")
servers.remove("web2")

print(servers)

for server in servers:
    print(server)

regions = ("us-east-1",2)

print(regions[1])

#Dictionary
employee = {
    "name":"Bharath",
    "role":"SRE"
}

print(employee["role"])

employee["salary"]=100000

for key,value in employee.items():
    print(key,value)

 #Set   
users={"john","alice"}
print(users)

#If-Else
cpu = 80
if cpu > 80:
    print("CPU is critical")
elif cpu > 70:
    print("CPU is warning")
else:
    print("CPU is healthy")

#for loop
print("For Loop:")
for i in range(5):
    print(i)

#While Loop
count = 0
print("While Loop:")
while count<7:
    print(count)
    count+=1




laser_security = []
laser_security_end = []
max_num = 0

laser_security = open("input.txt", "r").read().split("\n")

for line in range(len(laser_security)):
  laser_security[line] = laser_security[line].split(": ")    
  laser_security[line] = [int(laser_security[line][0]),[False]+[True]*(int(laser_security[line][1])-1)]
  max_num = int(laser_security[line][0])

laser_security_end = [[[True],0]]*(max_num+1)

for line in laser_security:
  laser_security_end[line[0]] = [list(line[1]),0]

laser_security = list(laser_security_end)

respuesta = [[]]*len(laser_security)

index_mayor = 0
for play in range(2000000000):
  print(play)
  resi = True
  for res in range(len(respuesta)):
    respuesta[res] = respuesta[res] + [laser_security[res][0][0]]
  if len(respuesta[0]) > len(laser_security):
    for i in range(len(respuesta)):
      respuesta[i].pop(0)
  for line in range(len(laser_security)): 
    if laser_security[line][0][0] == False:
      laser_security[line][1] = 0  
    if laser_security[line][0][-1] == False:
      laser_security[line][1] = 1 
    if laser_security[line][1] == 0:
      laser_security[line][0].insert(0,laser_security[line][0].pop())
    else:
      laser_security[line][0].append(laser_security[line][0].pop(0))
  if(len(respuesta) == len(respuesta[len(respuesta)-1])):
    for i in range(len(respuesta)):
      resi = resi & respuesta[i][i]
    if resi:
      print("I have the solution: "+str(1+index_mayor-len(laser_security)))
      break
  index_mayor += 1

#for res in respuesta:
  #print(res)


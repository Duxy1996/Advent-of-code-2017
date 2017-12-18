
laser_security = []
laser_security_end = []

File.open("input2.txt", "r") do |f|
  f.each_line do |line|
    aux_array = line.split(": ")  
    max = aux_array[0].to_i     
    laser_security.push([aux_array[0].to_i,Array.new((aux_array[1].to_i-1), true).unshift(false)])
  end
end

laser_security_end = Array.new(laser_security.last[0], [[true],0])

for laser in laser_security
  laser_security_end[laser[0]] = [laser[1],0]
end

laser_security = laser_security_end

respuesta = Array.new(laser_security.length,[])


for play in 0..6
  for res in 0..(laser_security.length-1)        
    respuesta[res] = respuesta[res].push(laser_security[res][0][0])    
  end
  for laser in laser_security    
    if laser[0].first == false
      laser[1] = 0  
    end
    if laser[0].last == false
      laser[1] = 1 
    end
    if laser[1] == 0
      laser[0].unshift(laser[0].pop())
    else
      laser[0].push(laser[0].shift())
    end
  end   
end
for i in 0..6
  for j in 0..7
    print respuesta[i][j]
    print "  "
  end
  print "\n"
end

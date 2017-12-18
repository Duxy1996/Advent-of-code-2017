
laser_security = []
score = 0
max = 0
File.open("input.txt", "r") do |f|
  f.each_line do |line|
    aux_array = line.split(": ")  
    max = aux_array[0].to_i     
    laser_security.push([aux_array[0].to_i,Array.new((aux_array[1].to_i-1), true).unshift(false),0])
  end
end 

dex = 0
for i in 0..max
  #puts "Picosecond ".concat(i.to_s)
  if i == laser_security[dex][0]
    puts laser_security[dex][1][0]
    if laser_security[dex][1][0] == false
      score = score + i*laser_security[dex][1].length
    end
    dex = dex + 1
  
  end

  for laser in laser_security

    if laser[1].first == false
      laser[2] = 0  
    end
    if laser[1].last == false
      laser[2] = 1 
    end
    if laser[2] == 0
      laser[1].unshift(laser[1].pop())
    else
      laser[1].push(laser[1].shift())
    end


  end
end

puts score
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

state = []
state.push(laser_security)

state_index = 0
for jj in 0..2000000000
  puts ("vuelta "+jj.to_s)
  respuesta = true  
  state_index += 1
  dex = 0
  laser_security = state[jj].dup
  for i in 0..max
    if dex < 0
      dex = dex + 1
    else
      if i == laser_security[dex][0]
        #puts laser_security[dex][1][0]
        respuesta = respuesta & laser_security[dex][1][0]
        if laser_security[dex][1][0] == false
          score = score + i*laser_security[dex][1].length
        end
        dex = dex + 1
      end    
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
    if state_index + i >= state.length      
      state.push(laser_security.dup)
    end  
  end  
  if respuesta
    puts ("vuelta "+jj.to_s)
    break
  end
end

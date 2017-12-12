coordsfull = open("input.txt", "r").read().split(",")
max_dist = []
for ii in range(len(coordsfull)):
  coords = coordsfull[0:(ii+1)] 
  n_count = 0
  s_count = 0
  ne_count = 0
  sw_count = 0
  nw_count = 0
  se_cpunt = 0

  for coord in coords:
    if("n" == coord):
      n_count += 1
    elif("s" == coord):
      s_count += 1
    elif("ne" == coord):
      ne_count += 1
    elif("se" == coord):
      se_cpunt += 1
    elif("nw" == coord):
      nw_count += 1
    elif("sw" == coord):
      sw_count += 1

  #print(n_count,s_count,sw_count,nw_count,ne_count,se_cpunt)

  if (n_count > s_count):
    n_count = n_count - s_count
    s_count = 0
  else:
    s_count = s_count - n_count
    n_count = 0

  if (sw_count > ne_count):
    sw_count = sw_count - ne_count
    ne_count = 0
  else:
    ne_count = ne_count - sw_count
    sw_count = 0

  if (se_cpunt > nw_count):
    se_cpunt = se_cpunt - nw_count
    nw_count = 0
  else:
    nw_count = nw_count - se_cpunt
    se_cpunt = 0


  #print(n_count,s_count,sw_count,nw_count,ne_count,se_cpunt)

  for i in range(1):
    if (ne_count > s_count):
      se_cpunt = s_count + se_cpunt
      ne_count = ne_count - s_count
      s_count = 0
    else:
      se_cpunt = ne_count + se_cpunt
      s_count = s_count - ne_count
      ne_count = 0

    if (se_cpunt > n_count):
      ne_count = n_count + ne_count
      se_cpunt = se_cpunt - n_count
      n_count = 0
    else:
      ne_count = se_cpunt + ne_count
      n_count = n_count - se_cpunt
      se_cpunt = 0

    if (nw_count > s_count):
      sw_count = s_count + sw_count
      nw_count = nw_count - s_count
      s_count = 0
    else:
      sw_count = nw_count + sw_count
      s_count = s_count - nw_count
      nw_count = 0

    if (sw_count > n_count):
      nw_count = n_count + nw_count
      sw_count = sw_count - n_count
      n_count = 0
    else:
      nw_count = sw_count + nw_count
      n_count = n_count - sw_count
      sw_count = 0

    if (sw_count > se_cpunt):
      s_count = se_cpunt + s_count
      sw_count = sw_count - se_cpunt
      se_cpunt = 0
    else:
      s_count = sw_count + s_count
      se_cpunt = se_cpunt - sw_count
      sw_count = 0

    if (nw_count > ne_count):
      n_count = ne_count + n_count
      nw_count = nw_count - ne_count
      ne_count = 0
    else:
      n_count = nw_count + n_count
      ne_count = ne_count - nw_count
      nw_count = 0

  #print(n_count,s_count,sw_count,nw_count,ne_count,se_cpunt)
  addition = n_count + s_count + sw_count + ne_count + se_cpunt + nw_count
  #print(addition)
  max_dist.append(addition)

print(max(max_dist))
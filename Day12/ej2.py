
def problem_two_algo(pipes): 
  grupos = 0;
  big_group = []
  for pipe in pipes:
    big_group.append(pipe[0])
  
  while(len(big_group)> 0):
    came_from = [big_group[0]]
    len_ant = 0;
    while(len_ant != len(came_from)):
      len_ant = len(came_from)
      for pipe in pipes:
        if pipe[0] in came_from:
          came_from = came_from + pipe[1]
      came_from = list(set(came_from))
    big_group = list(set(big_group)-set(came_from))
    grupos += 1
  return grupos

def problem_input():
  pipes = open("input.txt", "r").read().split("\n")
  for pipe_index in range(len(pipes)):
    pipes[pipe_index] = pipes[pipe_index].split("<->")
    pipes[pipe_index][1] = pipes[pipe_index][1].split(",")
    pipes[pipe_index][0] = int(pipes[pipe_index][0])
    for sub_ind in range(len(pipes[pipe_index][1])):
      pipes[pipe_index][1][sub_ind] = int(pipes[pipe_index][1][sub_ind])
  return pipes

def problem_two():
  input_file = problem_input()
  return problem_two_algo(input_file)

print(problem_two())
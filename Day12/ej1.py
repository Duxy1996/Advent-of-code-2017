
def problem_one_algo(pipes): 
  came_from = [0]
  len_ant = 0;
  while(len_ant != len(came_from)):
    len_ant = len(came_from)
    for pipe in pipes:
      if pipe[0] in came_from:
        came_from = came_from + pipe[1]
    came_from = list(set(came_from))
  return len(set(came_from))

def problem_input():
  pipes = open("input.txt", "r").read().split("\n")
  for pipe_index in range(len(pipes)):
    pipes[pipe_index] = pipes[pipe_index].split("<->")
    pipes[pipe_index][1] = pipes[pipe_index][1].split(",")
    pipes[pipe_index][0] = int(pipes[pipe_index][0])
    for sub_ind in range(len(pipes[pipe_index][1])):
      pipes[pipe_index][1][sub_ind] = int(pipes[pipe_index][1][sub_ind])
  return pipes

def problem_one():
  input_file = problem_input()
  return problem_one_algo(input_file)


print(problem_one())
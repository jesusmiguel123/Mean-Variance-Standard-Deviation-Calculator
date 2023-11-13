import numpy as np

def calculate(list):
   if len(list) < 9:
      raise ValueError("List must contain nine numbers.")
   
   functions = {
      'mean': lambda a, ax: np.mean(a, axis=ax).tolist(),
      'variance': lambda a, ax: np.var(a, axis=ax).tolist(),
      'standard deviation': lambda a, ax: np.std(a, axis=ax).tolist(),
      'max': lambda a, ax: np.max(a, axis=ax).tolist(),
      'min': lambda a, ax: np.min(a, axis=ax).tolist(),
      'sum': lambda a, ax: np.sum(a, axis=ax).tolist()
   }

   matrix = np.array(list).reshape((3, 3))

   calculations = {}
   for v in functions:
      if v not in calculations:
         calculations[v] = []
      for ax in (0, 1, None):
         calculations[v].append(functions[v](matrix, ax=ax))
   return calculations
import math
from kaggle_environments.envs.orbit_wars.orbit_wars import Planet

def nearestplanetsniper(obs):
  player = obs.get("player", 0) if isinstance(obs, dict) else obs.player
  raw_planets = obs.get("planets", []) if isinstance(obs, dict) else obs.planets
  planets = [Planet(*p) for p in raw_planets]
  my_planets = [p for p in planets if p.owner == player]
  target_planets = [p for p in planets if p.owner != player]
  moves = []
  for mine in my_planets
    nearest = None
    for t in target_planets 
      dist = math.sqrt((mine.x - t.x)**2+(mine.y-t.y)**2)
      if dist < min_dist
        min_dist = dist
        nearest = t
    if nearest is None
        continue
    shipsneeded = nearest.ships + 1
    if mine.ships > nearest.ships
        angle = math.atan2(nearest.y - mine.y, nearest.x - mine.x)
        moves.append([mine.id, angle, ships_needed])
  return moves

        
        
if episodeSteps < 80
  

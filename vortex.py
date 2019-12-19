# particle vortex
import numpy as np
import pandas as pd

n = 200 # n particles to generate

origin = [0,0]

spread = 500


points = np.random.normal(origin,spread,(n,2))


df = pd.DataFrame(points)

out = pd.DataFrame()
out['x'] = df[0]
out['y'] = df[1]
out['m'] = 20
out['r'] = 100
out['vx'] = out.y.apply(lambda x: origin[1] - x)
out['vy'] = out.x.apply(lambda x: x - origin[0])

out[['m','r','x','y','vx','vy']].to_csv('vortex.csv',header=True, index=False)

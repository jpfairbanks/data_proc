import pandas as pd
import matplotlib.pyplot as plt
df  = pd.read_csv("stats.tsv", sep='\t',)
pframe = df.set_index([ 'cores','alg','filename',]).sort()['median'].unstack()
fig, axes = plt.subplots(nrows=3, ncols=1, figsize=(8, 15))
for col, ax in zip(pframe,axes):
  ser = pframe[col].unstack()
  ser.plot(ax=ax, subplots=False)
  ax.set_title('scalability '+ col)
plt.show()

sf = df.set_index(['cores','filename','alg']).sort()['median'].unstack()
rat = sf['segscan.out']/sf['sequential.out']
rat.unstack().plot()
plt.title('parallel slowdown of segscan to serial')
plt.ylabel('slowdown')
plt.show()

import matplotlib
matplotlib.use("Agg")
import numpy as np
import pylab as pl


xvals=np.arange(100)
yvals=np.cumsum(np.random.random(100))
yvals[-10:]=0
#yvals=np.log(yvals)
pl.close()

pl.plot(xvals,yvals)
pl.xlabel("X")
pl.ylabel("Y")
pl.title("Title")

pl.savefig("testgraph.png")
from appJar import gui
from mpl_toolkits.mplot3d import Axes3D

with gui() as app:
    fig = app.addPlotFig("p1")
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter([1,2],[1,2],[1,2])

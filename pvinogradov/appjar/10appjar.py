from appJar import gui

app = gui()
app.addPieChart('p1', {'apples':50, 'oranges':200,
                       'grapes':75, 'beef':300,
                       'turkey':150})
app.go()
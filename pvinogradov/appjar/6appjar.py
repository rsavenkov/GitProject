from appJar import gui


app = gui('iiixa', '800x800')

app.addCanvas('c1')
app.addCanvasOval('c1', 10, 10, 100, 100, fill='red', outline='blue', width=3)
app.addCanvasLine('c1', 0, 0, 255, 255, width=5)
app.addCanvasLine('c1', 0, 255, 255, 0, width=123)
app.addCa
app.go()
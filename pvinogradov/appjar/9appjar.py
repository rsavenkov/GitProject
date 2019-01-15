from appJar import gui

app = gui('Title')
app.addGoogleMap('m1')
app.setGoogleMapSize('m1', '300x300')
app.go()
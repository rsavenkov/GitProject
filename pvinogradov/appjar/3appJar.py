from appJar import gui



app = gui('title')
app.addSelectableLabel('title1', text='3333')
app.addLabel('11', 'Label 1')
app.addLabel('12', 'Label 2')
app.addLabel('13', 'Label 3')
app.addLabel('14', 'Label 4')

app.addMeter('progress')
app.setMeterFill('progress', 'blue')
app.setLabelBg('11', 'red')
app.setLabelBg('12', 'yellow')
app.setLabelBg('13', 'purple')
app.setLabelBg('14', 'orange')

app.clearLabel('11')
app.clearLabel('12')
app.clearLabel('13')
app.go()
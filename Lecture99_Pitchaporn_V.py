from tkinter import *

def compareBMI(bmi):
  if bmi > 30:
    return 'อ้วนมาก'
  elif bmi >= 25:
    return 'อ้วน'
  elif bmi >= 23:
    return 'น้ำหนักเกิน'
  elif bmi >= 18.6:
    return 'น้ำหนักปกติ เหมาะสม'
  else:
    return 'ผอมเกินไป'

def calBMI(event):
  print(f'Height : {textBoxHeight.get()} cm')
  print(f'Weight : {textBoxWeight.get()} Kg')
  bmi = float(textBoxWeight.get()) / ((float(textBoxHeight.get())/100)**2)
  print(f'BMI : {bmi}')

  labelBMI.configure(text=bmi)
  labelResult.configure(text=compareBMI(bmi))

MainWindow = Tk()

labelHeight = Label(MainWindow, text='ส่วนสูง (cm.)').grid(row=0, column=0)
textBoxHeight = Entry(MainWindow)
textBoxHeight.grid(row=0, column=1)
labelWeight = Label(MainWindow, text='น้ำหนัก (Kg.)').grid(row=1, column=0)
textBoxWeight = Entry(MainWindow)
textBoxWeight.grid(row=1, column=1)

calculateButton = Button(MainWindow, text='คำนวณ')
calculateButton.grid(row=2, column=0)

calculateButton.bind('<Button-1>', calBMI)

labelBMI = Label(MainWindow, text = 'ค่า BMI')
labelBMI.grid(row=2, column=1)
labelResult = Label(MainWindow, text='ผลลัพธ์')
labelResult.grid(row=3, column=1)

MainWindow.mainloop()
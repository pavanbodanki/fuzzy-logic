# Making necessary imports for the program
import numpy as np
import skfuzzy as fuzz
from tkinter.messagebox import showwarning,showinfo
import matplotlib.pyplot as plt
import PIL
from PIL import ImageTk
import PIL.Image
from tkinter import *
The helper functions in the program are listed below
# To open the frame widget, frame.tkraise() is used
def raise_frame(frame):
frame.tkraise()
# To close the tkinter window
def on_close():
root.quit()
# Returns the aggregated output of all rules, def aggr1(a, b, c):
max1 = np.fmax(a,b)
return np.fmax(max1,c)
# Returns the result of 'fuzzy and(minimum)' operator
def And1(a, b, c, d):
min1 = np.fmin(a, b)
min2 = np.fmin(c, d)
return np.fmin(min1,min2)
# Returns the result of 'fuzzy or(maximum)' operator
def Or(a, b, c, d, e, f):
min1 = np.fmax(a, b)
min2 = np.fmax(c, d)
min3 = np.fmax(e, f)
return np.fmax(min1, np.fmin(min2, min3))
# Returns the result of 'fuzzy and(minimum)' operator
def And(a, b, c, d, e, f):
min1 = np.fmin(a, b)
min2 = np.fmin(c, d)
min3 = np.fmin(e, f)
return np.fmin(min1, np.fmin(min2, min3))
# Returns the aggregated output of all rules
def aggr(l):
a = np.fmax(l[0], l[1])
s = (len(l) - 2) //2
for i in range(2, s + 1, 2):
m = np.fmax(a, np.fmax(l[i], l[i + 1]))
a = m
return a
# Returns 1 if marks are following descending pattern which will be used in calculating marks for next
semester
def decreasing(l):
m = []
n = len(l)
for i in range(1,n):
  if l[i]-l[i-1] < 0:
    m.append('-')
  else:
    m.append('+')
  if m.count('-') > m.count('+'):
    return 1
  else:
    return 0
# to visualize input and output plots of each module
def visualize(fig):
fig.show()
# Function to calculate Higher studies output
def eval_fut(a, b, c, d, e, f):
try:
# Converting string values to floating point values
a1, b1, c1, d1, e1, f1 = float(a), float(b), float(c), float(d), float(e), float(f)
# Assigning ranges to input parameters
# np.arange(start, stop, step) returns a NumPy array from start to stop with the given step
tech = np.arange(0, 101, 1)
math = np.arange(0, 101, 1)
engl = np.arange(0, 101, 1)
manag = np.arange(0, 101, 1)
gmat = np.arange(0, 801, 1)
gre = np.arange(0, 341, 1)
# Generate fuzzy membership functions(triangular, trapezoidal)
tech_low = fuzz.trimf(tech, [0, 0, 40]) # Triangular membership function
tech_med = fuzz.trapmf(tech, [40, 45, 55, 65]) # Trapezoidal membership function
tech_hi = fuzz.trimf(tech, [50, 65, 100])
math_low = fuzz.trimf(math, [0, 0, 40])
math_med = fuzz.trapmf(math, [40, 45, 55, 65])
math_hi = fuzz.trimf(math, [50, 65, 100])
engl_low = fuzz.trimf(engl, [0, 0, 40])
engl_med = fuzz.trapmf(engl, [40, 45, 55, 65])
engl_hi = fuzz.trimf(engl, [50, 65, 100])
manag_low = fuzz.trimf(manag, [0, 0, 40])
manag_med = fuzz.trapmf(manag, [40, 45, 55, 65])
manag_hi = fuzz.trimf(manag, [50, 65, 100])
gre_low = fuzz.trimf(gre,[0,0,300])
gre_med = fuzz.trimf(gre,[301,315,325])
gre_hi = fuzz.trapmf(gre,[325,330,340,340])
gmat_low = fuzz.trimf(gmat, [0,0,630])
gmat_med = fuzz.trapmf(gmat, [630,640,670,690])
gmat_hi = fuzz.trapmf(gmat, [680,700,800,800])
# Plotting graph for input ranges
fig, a = plt.subplots(nrows=3, ncols=2, figsize=(8, 8))
# Plotting technical skills
a[0][0].plot(tech, tech_low, 'b', linewidth=1.5, label='low')
a[0][0].plot(tech, tech_med, 'g', linewidth=1.5, label='medium')
a[0][0].plot(tech, tech_hi, 'r', linewidth=1.5, label='high')
a[0][0].legend()
a[0][0].set_title('technical skills')
# Plotting mathematical skills
a[0][1].plot(math, math_low, 'b', linewidth=1.5, label='low')
a[0][1].plot(math, math_med, 'g', linewidth=1.5, label='medium')
a[0][1].plot(math, math_hi, 'r', linewidth=1.5, label='high')
a[0][1].legend()
a[0][1].set_title('mathematical skills')
# Plotting english skills
a[1][0].plot(engl, engl_low, 'b', linewidth=1.5, label='low)
a[1][0].plot(engl, engl_med, 'g', linewidth=1.5, label='medium')
a[1][0].plot(engl, engl_hi, 'r', linewidth=1.5, label='high')
a[1][0].legend()
a[1][0].set_title('english skills')
# Plotting management skills
a[1][1].plot(manag, manag_low, 'b', linewidth=1.5, label='low')
a[1][1].plot(manag, manag_med, 'g', linewidth=1.5, label='medium')
a[1][1].plot(manag, manag_hi, 'r', linewidth=1.5, label='high')
a[1][1].legend()
a[1][1].set_title('management skills')
a[2][0].plot(gre, gre_low, 'b', linewidth=1.5, label='low')
a[2][0].plot(gre, gre_med, 'g', linewidth=1.5, label='medium')
a[2][0].plot(gre, gre_hi, 'r', linewidth=1.5, label='high')
a[2][0].legend()
a[2][0].set_title('gre score')
a[2][1].plot(gmat, gmat_low, 'b', linewidth=1.5, label='low')
a[2][1].plot(gmat, gmat_med, 'g', linewidth=1.5, label='medium')
a[2][1].plot(gmat, gmat_hi, 'r', linewidth=1.5, label='high')
a[2][1].legend()
a[2][1].set_title('gmat score')
# turning off right and top axes in the graph
for a in (a[0][0], a[0][1], a[1][0], a[1][1], a[2][0], a[2][1]):
a.spines['top'].set_visible(False)
a.spines['right'].set_visible(False)
a.get_xaxis().tick_bottom()
a.get_yaxis().tick_left()
plt.tight_layout()

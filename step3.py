# Aggregating all the gmat output membership functions together
gmat_aggregated = aggr(gmat_list)
# Calculating defuzzified result on fuzzy output to get crisp output(numeric value)
# mean of maxima is the defuzzication method used here to get the result
gmat_res = fuzz.defuzz(gmat, gmat_aggregated, 'mom')
gmatm = np.zeros_like(gmat)
gmatf = fuzz.interp_membership(gmat, gmat_aggregated, gmat_res)
# Printing result to output screen
myText = StringVar()
myText.set(gmat_res)
Label(fourth, text="GMAT score:", bg="antique white", font=('helvetica', 18)).grid(row=8, column=3)
Label(fourth, text="", textvariable=myText, bg='antique white', font=('helvetica',18)).grid(row=8, column=4)
# Calculating gre result
# Application of fuzzy if..then rules for gre score to get fuzzy output
rule1 = And1(tech_level_hi, math_level_hi, engl_level_hi, gre_level_hi)
gre_op_hi = np.fmin(rule1, gre_hi)
gre_list.append(gre_op_hi)
rule2 = And1(tech_level_low, math_level_low, engl_level_low, gre_level_low)
gre_op_low = np.fmin(rule2, gre_low)
gre_list.append(gre_op_low)
rule3 = And1(tech_level_med, math_level_med, engl_level_med, gre_level_med)
gre_op_med = np.fmin(rule3, gre_med)
gre_list.append(gre_op_med)
rule4 = And1(tech_level_hi, math_level_hi, engl_level_hi, gre_level_med)
gre_op_hi_1 = np.fmin(rule4, gre_hi)
gre_list.append(gre_op_hi_1)
# Aggregating all the gre output membership functions
gre_aggregated = aggr(gre_list)
# Calculating defuzzified result on fuzzy output to get crisp output(numeric value)
gre_res = fuzz.defuzz(gre, gre_aggregated, 'mom')
# Printing gre result to output screen
myText1 = StringVar()
myText1.set(gre_res)
Label(fourth, text="GRE score:", bg="antique white", font=('helvetica', 18)).grid(row=9, column=3)
Label(fourth, text="", textvariable=myText1, bg='antique white', font=('helvetica', 18)).grid(row=9, column=4)
gref = fuzz.interp_membership(gre, gre_aggregated, gre_res)
grem = np.zeros_like(gre)
# Plotting output membership activity and result
op_fig, bx0 = plt.subplots(figsize=(8, 3))
bx0.plot(gmat, gmat_low, 'b', linewidth=0.5, linestyle='--')
bx0.plot(gmat, gmat_med, 'r', linewidth=0.5, linestyle='--')
bx0.plot(gmat, gmat_hi, 'g', linewidth=0.5, linestyle='--')
bx0.fill_between(gmat, gmatm, gmat_aggregated, facecolor='orange', alpha=0.8)
bx0.plot([gmat_res, gmat_res], [0, gmatf], 'r', linewidth=1.5, alpha=0.8)
bx0.set_title('Output membership activity')
# Displaying buttons to visualize input and output plots
if gre_res:
btn1 = Button(fourth, text='visualize input', width=14, height=2, command=lambda:
visualize(fig))
btn1.grid(row=10, column=3)
btn2 = Button(fourth, text='visualize output', width=14, height=2, command=lambda:
visualize(op_fig))
btn2.grid(row=11, column=3)
except Exception as e:
print(e)
# Warning to be raised when user enters a incorrect value
showinfo("WARNING", "ENTER A VALID VALUE")
# Function to calculate placement module output
def fuzzif(a,b,c,d,e,f,g,h):
# Converting string values to floating point values
s1, s2, s3, s4, s5, s6, s7, s8 = float(a), float(b), float(c), float(d), float(e), float(f), float(g),int(h)
# Checking for eligibility criteria
if s1 < 60 or s2 <60 or s3 < 60 or s8 > 1:
myText = StringVar()
# Printing not eligible if student does not meet eligibility criteria
res = "NOT ELIGIBLE" myText.set(res)
Label(second, text="", textvariable=myText, bg='antique white').grid(row=6, column=4)
else:
# Assigning ranges to input parameters
mock = np.arange(0, 101, 1)
comm = np.arange(0, 101, 1)
apti = np.arange(0, 101, 1)
core = np.arange(0, 101, 1)
plac = np.arange(0, 101, 1)
# Generate fuzzy membership functions(triangular, trapezoidal)
mock_low = fuzz.trimf(mock, [0, 0, 40])
mock_med = fuzz.trimf(mock, [40, 40, 65])
mock_hi = fuzz.trimf(mock, [50, 65, 100])
comm_low = fuzz.trimf(comm, [0, 0, 40])
comm_med = fuzz.trimf(comm, [40, 40, 65])
comm_hi = fuzz.trimf(comm, [50, 65, 100])
apti_low = fuzz.trimf(apti, [0, 0, 40])
apti_med = fuzz.trimf(apti, [40, 40, 65])
apti_hi = fuzz.trimf(apti, [50, 65, 100])
core_low = fuzz.trimf(core, [0, 0, 40])
core_med = fuzz.trimf(core, [40, 40, 65])
core_hi = fuzz.trimf(core, [50, 65, 100])
plac_low = fuzz.trimf(plac, [0, 0, 40])
plac_med = fuzz.trimf(plac, [40, 40, 65])
plac_hi = fuzz.trimf(plac, [50, 65, 100])
# Plotting graph for input ranges using plot function
fig, a = plt.subplots(nrows=2, ncols=2, figsize=(10, 10))
a[0][0].plot(mock, mock_low, 'b', linewidth=1.5, label='low')
a[0][0].plot(mock, mock_med, 'g', linewidth=1.5, label='medium')
a[0][0].plot(mock, mock_hi, 'r', linewidth=1.5, label='high')
a[0][0].legend()
a[0][0].set_title('mock interview scores')
a[0][1].plot(comm, comm_low, 'b', linewidth=1.5, label='low')
a[0][1].plot(comm, comm_med, 'g', linewidth=1.5, label='medium')
a[0][1].plot(comm, comm_hi, 'r', linewidth=1.5, label='high')
a[0][1].legend()
a[0][1].set_title('communication skills')
a[1][0].plot(apti, apti_low, 'b', linewidth=1.5, label='low')
a[1][0].plot(apti, apti_med, 'g', linewidth=1.5, label='medium')
a[1][0].plot(apti, apti_hi, 'r', linewidth=1.5, label='high')
a[1][0].legend()
a[1][0].set_title('aptitude skills')
a[1][1].plot(core, core_low, 'b', linewidth=1.5, label='low')
a[1][1].plot(core, core_med, 'g', linewidth=1.5, label='medium')
a[1][1].plot(core, core_hi, 'r', linewidth=1.5, label='high')
a[1][1].legend()
a[1][1].set_title('core knowledge')
for a in (a[0][0], a[0][1], a[1][0], a[1][1]):
a.spines['top'].set_visible(False)
a.spines['right'].set_visible(False)
a.get_xaxis().tick_bottom()
a.get_yaxis().tick_left()
plt.tight_layout()
# Checking if all user entered data is in valid range or not
valid_range = [i for i in range(0,101)]
if s1 not in valid_range or s2 not in valid_range or s3 not in valid_range or s4 not in
valid_range or s5 not in valid_range or s6 not in valid range
# Prompting user to enter a valid input
showinfo("WARNING", "ENTER A VALUE BETWEEN 0 TO 100")
btn = Button(second, text='SUBMIT', width=10, height=2, command=lambda:
fuzzif(r1.get(), r2.get(), r3.get(), r4.get(), r5.get(), r6.get()))
Step 1 - Fuzzification . In this step, crisp(input) values are converted into fuzzy values. fuzz.interp_membership() is used for generating fuzzy values. else:
# Converting input values to fuzzy values
mock_level_low = fuzz.interp_membership(mock, mock_low, s4)
mock_level_med = fuzz.interp_membership(mock, mock_med, s4)
mock_level_hi = fuzz.interp_membership(mock, mock_hi, s4)
comm_level_low = fuzz.interp_membership(comm, comm_low, s5)
comm_level_med = fuzz.interp_membership(comm, comm_med, s5)
comm_level_hi = fuzz.interp_membership(comm, comm_hi, s5)
apti_level_low = fuzz.interp_membership(apti, apti_low, s6)
apti_level_med = fuzz.interp_membership(apti, apti_med, s6)
apti_level_hi = fuzz.interp_membership(apti, apti_hi, s6)
core_level_low = fuzz.interp_membership(core, core_low, s7)
core_level_med = fuzz.interp_membership(core, core_med, s7)
core_level_hi = fuzz.interp_membership(core, core_hi, s7)
Step 2 - Applying rules to the above fuzzy values
# Application of fuzzy if..then rules for placement result
l = []
rule1 = And1(mock_level_low, comm_level_low, apti_level_low, core_level_low)
plac_op_low = np.fmin(rule1, plac_low)
l.append(plac_op_low)
rule2 = And1(mock_level_hi, comm_level_hi, apti_level_hi, core_level_hi)
plac_op_hi = np.fmin(rule2, plac_hi) l.append(plac_op_hi)

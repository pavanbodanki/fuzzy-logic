gmat_list = []
gre_list = []
rule1 = And1(math_level_hi, engl_level_hi, manag_level_hi, gmat_level_hi)
gmat_op_hi = np.fmin(rule1, gmat_hi)
gmat_list.append(gmat_op_hi)
rule2 = And1(math_level_low, engl_level_low, manag_level_low, gmat_level_low)
gmat_op_low = np.fmin(rule2, gmat_low)
gmat_list.append(gmat_op_low)
rule3 = And1(math_level_med, engl_level_med, manag_level_med, gmat_level_med)
gmat_op_med = np.fmin(rule3, gmat_med)
gmat_list.append(gmat_op_med)
rule4 = And1(math_level_hi, engl_level_hi, manag_level_hi, gmat_level_med)
gmat_op_hi_1 = np.fmin(rule4, gmat_hi)
gmat_list.append(gmat_op_hi_1)

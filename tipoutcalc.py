def tipout_calc(emp_1_tips, emp_2_tips, emp_3_tips, emp_1_hours, emp_2_hours, emp_3_hours, total_tips, food_sales, bar_back, runner):
    total_hours = emp_1_hours + emp_2_hours + emp_3_hours
    if bar_back == 1:
      barback = round(total_tips * .15, 2)
    else:
      barback = 0
    print("Barback gets + $" + str(round(barback, 2)))
    print("Employee #1 tips barback $" + str(round(barback/total_hours * emp_1_hours, 2)))
    print("Employee #2 tips barback $" + str(round(barback/total_hours * emp_2_hours, 2)))
    print("Employee #3 tips barback $" + str(round(barback/total_hours * emp_3_hours, 2)))
   
    if runner == 1:
      food_runner = food_sales * .03
    else:
      food_runner = 0
    print("Food runner gets + $" + str(round(food_runner, 2)))
   
    total_after_tipout = total_tips - (barback + food_runner)
    total_hourly_rate = total_after_tipout / total_hours
    print("The total hourly rate is $" + str(round(total_hourly_rate, 2)))

    emp_1_hourly = total_hourly_rate * emp_1_hours
    emp_2_hourly = total_hourly_rate * emp_2_hours
    emp_3_hourly = total_hourly_rate * emp_3_hours
    print("Employee #1 gets $" + str(round(emp_1_hourly, 2))+ " in tips.")
    print("Employee #2 gets $" + str(round(emp_2_hourly, 2))+ " in tips.")
    print("Employee #3 gets $" + str(round(emp_3_hourly, 2))+ " in tips.")

    total_credit_tips = emp_1_tips + emp_2_tips + emp_3_tips
    credit_hourly_rate = total_credit_tips / total_hours
    print("The hourly rate for credit tips is $" +str(round(credit_hourly_rate, 2)))

    emp_1_credit_hourly = emp_1_hours * credit_hourly_rate
    emp_2_credit_hourly = emp_2_hours * credit_hourly_rate
    emp_3_credit_hourly = emp_3_hours * credit_hourly_rate
    print("Employee #1 gets $" + str(round(emp_1_credit_hourly, 2))+ " in credit tips.")
    print("Employee #2 gets $" + str(round(emp_2_credit_hourly, 2))+ " in credit tips.")
    print("Employee #3 gets $" + str(round(emp_3_credit_hourly, 2))+ " in credit tips.")
   
    if emp_1_tips >= emp_1_credit_hourly:
      print("Employee #1 tips out $" + str(round(emp_1_tips-emp_1_credit_hourly, 2)))
    else:
      print("Employee #1 recieves $" + str(round(emp_1_credit_hourly-emp_1_tips, 2)))
    if emp_2_tips >= emp_2_credit_hourly:
      print("Employee #2 tips out $" + str(round(emp_2_tips-emp_2_credit_hourly, 2)))
    else:
      print("Employee #2 recieves $" + str(round(emp_2_credit_hourly-emp_2_tips, 2)))
    if emp_3_tips >= emp_3_credit_hourly:
      print("Employee #3 tips out $" + str(round(emp_3_tips-emp_3_credit_hourly, 2)))
    else:
      print("Employee #3 recieves $" + str(round(emp_3_credit_hourly-emp_3_tips, 2)))

#tipout_calc(emp_1_tips, emp_2_tips, emp_3_tips, emp_1_hours, emp_2_hours, emp_3_hours, total_tips, food_sales, bar_back(enter 1 if present, 0 if no barback), runner(enter 1 if present, 0 if no runner))
tipout_calc(113.91, 265, 0, 8.5, 8,  0, 774, 47.5, 0, 0) 

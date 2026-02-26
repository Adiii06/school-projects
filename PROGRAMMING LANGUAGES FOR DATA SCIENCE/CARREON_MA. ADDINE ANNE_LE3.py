#!/usr/bin/env python
# coding: utf-8

# $\textbf{CS128-5L - PROGRAMMING LANGUAGES FOR DATA SCIENCE LABORATORY} \\ \texttt{2Q SY2324}$
# 
# NAME: MA. ADDINE ANNE T. CARREON
# 
# SECTION: A1

# ### Laboratory Exercise 3

# # <center> Saving with a Raise

# **Instructions:** 
# 
# In "Condo Unit Hunting" activity, assume that your salary didn’t change. But you are a Mapua graduate, and clearly you are going to be worth more to your company over time! So we are going to build on your solution by factoring in a raise every six months. 
# 
# Modify your program in "Condo Unit Hunting" to include the following:
# 
# 1. Have the user input a semi-annual salary raise **semi_annual_raise** (as a decimal percentage).
# 
# 2. After the 6th month, increase your salary by that percentage. Do the same after the 12th month, the 18th month, and so on. 
# 
# 
# Write a program to calculate how many months it will take you save up enough money for a down payment. Like before, assume that your investments earn a return of r = 0.04 (or 4%) and the required down payment percentage is 0.25 (or 25%). Have the user enter the following variables: 
# 
# 
# a.     The starting annual salary (annual_salary)
# 
# b.     The percentage of salary to be saved (portion_saved) 
# 
# c.     The cost of your dream home (total_cost) 
# 
# d.     The semiannual salary raise (semi_annual_raise) 
# 
# 
# **Hints** 
# 
# To help you get started, here is a rough outline of the stages you should probably follow in writing your code: 
# 
# ·      Retrieve user input. 
# 
# ·      Initialize some state variables. You should decide what information you need. Be sure to be careful about values that represent annual amounts and those that represent monthly amounts. 
# 
# ·      Be careful about when you increase your salary – this should only happen **after** the 6th, 12th, 18th month, and so on. 
# 
# 
# Try different inputs and see how quickly or slowly you can save enough for a down payment. **Please make your program print results in the format shown in the test cases below.** 

# In[3]:


annual_salary = float(input("Enter your starting annual salary: "))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
total_cost = float(input("Enter the cost of your dream home: "))
semi_annual_raise = float(input("Enter the semiannual raise, as a decimal: "))

required_dp = 0.25 
current_savings = 0.0
r = 0.04 
months = 0

monthly_salary = annual_salary / 12
monthly_saved = monthly_salary * portion_saved

dp = total_cost * required_dp

while current_savings < dp:
    current_savings += current_savings * (r / 12)
    current_savings += monthly_saved

    months += 1

    if months % 6 == 0:
        annual_salary += annual_salary * semi_annual_raise
        monthly_salary = annual_salary / 12
        monthly_saved = monthly_salary * portion_saved

print("Number of months:", months)


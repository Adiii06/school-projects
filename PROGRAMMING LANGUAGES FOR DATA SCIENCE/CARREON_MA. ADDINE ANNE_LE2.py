#!/usr/bin/env python
# coding: utf-8

# $\textbf{CS128-5L - PROGRAMMING LANGUAGES FOR DATA SCIENCE LABORATORY} \\ \texttt{2Q SY2324}$
# 
# NAME: MA. ADDINE ANNE T. CARREON
# 
# SECTION: A1

# ### Laboratory Exercise 2

# # <center> Condo Unit Hunting 

# **Instructions:** 
#     
# You have graduated from Mapua and now have a great job! You move to BGC and decide that you want to start saving to buy a condo unit. As condo unit prices are very high in the BGC, you realize you are going to have to save for several years before you can afford to make the down payment on a condo unit. Now, you are going to determine how long it will take you to save enough money to make the down payment given the following assumptions: 
# 
# 1. Call the cost of your condo unit as **total_cost**. 
# 
# 2. Call the portion of the cost needed for a down payment portion_down_payment. For simplicity, assume that **portion_down_payment** = 0.25 (25%). 
# 
# 3. Call the amount that you have saved thus far **current_savings**. You start with a current savings of Php0. 
# 
# 4. Assume that you invest your current savings wisely through Pag-IBIG MP2 Savings Program, with an annual return of r (in other words, at the end of each month, you receive an additional **current_savings*r/12** funds to put into your savings – the 12 is because r is an annual rate). Assume that your investments earn a return of r = 0.07 (7%). 
# 
# 5. Assume your annual salary is **annual_salary**. 
# 
# 6. Assume you are going to dedicate a certain amount of your salary each month to saving for the down payment. Call that **portion_saved**. This variable should be in decimal form (i.e. 0.1 for 10%). 
# 
# 7. At the end of each month, your savings will be increased by the return on your investment, plus a percentage of your **monthly salary** (annual salary / 12). 
# 
# Write a program (Python) to calculate how many months it will take you to save up enough money for a down payment. You will want your main variables to be floats, so you should cast user inputs to floats. 
# 
# 
# Your program should ask the user to enter the following variables: 
# 
# a.      The starting annual salary (annual_salary) 
# 
# b.      The portion of salary to be saved (portion_saved) 
# 
# c.      The cost of your dream home (total_cost) 
# 
# 
# 
# **Hints** 
# 
# 
# To help you get started, here is a rough outline of the stages you should probably follow in writing your code: 
# 
# ·      Retrieve user input. Look at input() if you need help with getting user input. For this problem set, you can assume that users will enter valid input (e.g. they won’t enter a string when you expect an int) 
# 
# ·      Initialize some state variables. You should decide what information you need. Be careful about values that represent annual amounts and those that represent monthly amounts. 
# 
# 

# In[1]:


annual_salary = float(input("Enter your annual salary: "))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
total_cost = float(input("Enter the cost of your dream home: "))

portion_down_payment = 0.25
current_savings = 0
r = 0.07  # 0.07 annual return on investment
monthly_salary = annual_salary / 12
months = 0

while current_savings < total_cost * portion_down_payment:
    current_savings += current_savings * r / 12  
    current_savings += monthly_salary * portion_saved  
    months += 1

print("Number of months:", months)


# In[2]:


annual_salary = float(input("Enter your annual salary: "))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
total_cost = float(input("Enter the cost of your dream home: "))

portion_down_payment = 0.25
current_savings = 0
r = 0.07  # 0.07 annual return on investment
monthly_salary = annual_salary / 12
months = 0

while current_savings < total_cost * portion_down_payment:
    current_savings += current_savings * r / 12  
    current_savings += monthly_salary * portion_saved  
    months += 1

print("Number of months:", months)


# In[3]:


annual_salary = float(input("Enter your annual salary: "))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
total_cost = float(input("Enter the cost of your dream home: "))

portion_down_payment = 0.25
current_savings = 0
r = 0.04  # 0.04 annual return on investment
monthly_salary = annual_salary / 12
months = 0

while current_savings < total_cost * portion_down_payment:
    current_savings += current_savings * r / 12  
    current_savings += monthly_salary * portion_saved  
    months += 1

print("Number of months:", months)


# In[4]:


annual_salary = float(input("Enter your annual salary: "))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
total_cost = float(input("Enter the cost of your dream home: "))

portion_down_payment = 0.25
current_savings = 0
r = 0.04  # 0.04 annual return on investment
monthly_salary = annual_salary / 12
months = 0

while current_savings < total_cost * portion_down_payment:
    current_savings += current_savings * r / 12  
    current_savings += monthly_salary * portion_saved  
    months += 1

print("Number of months:", months)


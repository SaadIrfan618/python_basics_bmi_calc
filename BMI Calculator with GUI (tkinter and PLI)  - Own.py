#!/usr/bin/env python
# coding: utf-8

# In[1]:


def calculate_bmi():

    # .get() fetches the value of a key in a dictionary. So user_feet_entry is key and input value will be its value
    user_feet = float(user_feet_entry.get())        
    user_inches = float(user_inches_entry.get())
    user_weight = float(user_weight_entry.get())
    
    try:
        # calculating BMI
        user_height = (user_feet)*0.3 + (user_inches)*0.02
        BMI = user_weight / user_height**2
        if BMI > 0:
            result_display.config(text=f"Your BMI: {BMI:.2f}")
    
    # to handle zero feet zero inches input
    except:
        result_display.config(text="Please enter valid inputs")
        insight_display.config(text="Please enter valid inputs")
        
    if BMI > 0:
        if BMI >= 40:
            insight = "You are obese"
        elif BMI >= 25 and BMI < 40:
            insight = "You are overweight"
        elif BMI >= 18.5 and BMI < 25:
            insight =  "You are normal weight"
        else:
            insight = "You are underweight"
    
    # to handle negative weight and zero weight
    else:
        result_display.config(text="Please enter valid inputs")
        insight = "Please enter valid inputs"
    
    insight_display.config(text=insight)
    
    # to handle negative feet or negative inches input
    if user_feet < 0 or user_inches < 0:
        result_display.config(text="Please enter valid inputs")
        insight_display.config(text="Please enter valid inputs")


# In[2]:


# importing tkinter library (GUI library)
import tkinter as tkinter
# importing ttk module (necessary for labels and entry and grid)
from tkinter import ttk
# importing modules from pillow(PIL) (image processing library)
from PIL import ImageTk, Image

# creating a window instance
window = tkinter.Tk()
window.title("BMI Calculator")
window.minsize(300,400)

# Defining all input labels, display labels, buttons, entrys
user_feet_label = ttk.Label(window, text="Enter your height (feet):")
user_inches_label = ttk.Label(window, text="Enter your height (inches):")
user_weight_label = ttk.Label(window, text="Enter your weight (kg):")
result_label = ttk.Label(window, text="Your BMI:")
insight_label = ttk.Label(window, text="Insight:")
guide_label = ttk.Label(window,text="Guide:")
user_feet_entry = ttk.Entry(window)
user_inches_entry = ttk.Entry(window)
user_weight_entry = ttk.Entry(window)

calculate_button = ttk.Button(window, text="Calculate")

result_display = ttk.Label(window, text="")
insight_display = ttk.Label(window, text="")

# creating grid structureSS
user_feet_label.grid(row=0, column=0, padx=10, pady=10)
user_feet_entry.grid(row=0, column=1, padx=10, pady=10)
user_inches_label.grid(row=1, column=0, padx=10, pady=10)
user_inches_entry.grid(row=1, column=1, padx=10, pady=10)
user_weight_label.grid(row=2, column=0, padx=10, pady=10)
user_weight_entry.grid(row=2, column=1, padx=10, pady=10)
calculate_button.grid(row=3, column=0, columnspan=2, sticky='we', padx=10, pady=10)
result_label.grid(row=4, column=0, padx=10, pady=10)
result_display.grid(row=4, column=1, padx=10, pady=10)
insight_label.grid(row=5, column=0, padx=10, pady=10)
insight_display.grid(row=5, column=1, padx=10, pady=10)
guide_label.grid(row=6, column=0, padx=10, pady=10)

# attaching calculate_bmi function to button
calculate_button.config(command=calculate_bmi)

# Create a photoimage object of the image in the path
# if picture not in notebook directory, then specify location as:   image = Image.open('Desktop\guide.png')
image = Image.open('guide.png')
photo = ImageTk.PhotoImage(image)

# saving PhotoImage into a variable
guide_pic = tkinter.Label(image=photo)
# especially refrencing to prevent removal(garbage collector may remove PhotoImage) and increase readability
guide_pic.image = photo

# Positioning image
guide_pic.place(x=130, y=250)

window.mainloop()


# In[ ]:





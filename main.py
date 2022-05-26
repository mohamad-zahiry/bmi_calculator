from tkinter import (
    Tk,
    # fill
    X,
    # side
    TOP,
    # widget
    Entry,
    OptionMenu,
    Label,
    Button,
    Frame,
    Radiobutton,
    # variable
    IntVar,
    StringVar,
)

# returns border options as a dictionary
def border(color, width):
    return {"highlightbackground": color, "highlightthickness": width}


root = Tk()
root.configure(background="#fff")
root.title("Quadratic Equation Solver | BMI Calculator")


# ================================= BMI Calculator ===============================
"""
"BMI Calculator" uses this formula:
    BMI = weight(kg) / (height(m) ** 2)

For the BMI range:
    BMI < 18.5: Underweight
    18.5 <= BMI < 25: Normal weight
    25 <= BMI < 30: Overweight
    BMI >= 30: Obese

To determine ideal weight use "Devine Formula":
    men "Ideal Weight" (kg) = 50 + 2.3 kg x (height - 60 (inches))
    women "Ideal Weight" (kg) = 45.5 + 2.3 kg x (height - 60 (inches))

    Resource: https://www.topendsports.com/testing/tests/devine-formula.htm
"""

# frame label
Label(root, text="BMI Calculator", pady=20, font=("Arial", 20, "bold"), bg="white").pack()

# border-frame
border_frame = Frame(root, **border("red", 3))
border_frame.pack(side=TOP, fill=X, expand=True, padx=10, pady=10)

# converts meter to inch
def meter_to_inch(height):
    return height * 39.36


# calculates bmi, weight: kg, height: m
def bmi_calculator(weight, height):
    return round(weight / (height ** 2), 1)


# calculates ideal weight, according to "Devine Formula"
def bmi_ideal_weight_calculator(height, gender):
    height = meter_to_inch(height)
    if gender.lower() == "male":
        return round(50 + 2.3 * (height - 60), 2)
    else:
        return round(45.5 + 2.3 * (height - 60), 2)


# BMI status
def bmi_status_color(bmi):
    if bmi < 18.5:
        return "Underweight", "red"
    elif 18.5 <= bmi < 25:
        return "Normal", "green"
    elif 25 <= bmi < 30:
        return "Overweight", "orange"
    elif bmi >= 30:
        return "Obese", "red"


# Calculate-button command
def bmi_calculate():
    bmi = bmi_calculator(float(bmi_weight.get()), float(bmi_height.get()))
    bmi_status, bmi_color = bmi_status_color(bmi)
    bmi_answer.set(f"BMI: {bmi}\n" f"{bmi_status}")
    bmi_answer_label.config(fg=bmi_color)
    ideal_weight = bmi_ideal_weight_calculator(float(bmi_height.get()), bmi_gender.get())
    bmi_ideal_weight.set(f"Ideal: {ideal_weight} kg")


# clears bmi entries
def bmi_clear():
    bmi_weight.set("0")
    bmi_height.set("0")
    bmi_answer.set("BMI: 0")
    bmi_ideal_weight.set("Ideal: 0")


# bmi part frame
bmi_frame = Frame(border_frame, padx=5, pady=5)

# weight entry
Label(bmi_frame, text="Weight(kg):").grid(row=0, column=0)
bmi_weight = StringVar(root)
Entry(bmi_frame, width=10, textvariable=bmi_weight, **border("red", 2)).grid(row=0, column=1)
bmi_weight.set("0")

# height entry
Label(bmi_frame, text="Height(m):").grid(row=0, column=2)
bmi_height = StringVar(root)
Entry(bmi_frame, width=10, textvariable=bmi_height, **border("red", 2)).grid(row=0, column=3)
bmi_height.set("0")

# age selector 18-45
Label(bmi_frame, text="Age:").grid(row=0, column=4)
valus = list(range(18, 45 + 1))
var = StringVar(bmi_frame)
OptionMenu(bmi_frame, var, *valus).grid(row=0, column=5)
var.set("18")

# gender selector
bmi_gender = StringVar(root)
Radiobutton(bmi_frame, text="Male", value="Male", variable=bmi_gender).grid(row=1, column=0, pady=15)
Radiobutton(bmi_frame, text="Female", value="Female", variable=bmi_gender).grid(row=1, column=1, pady=15)
bmi_gender.set("Male")

# bmi answer output
bmi_answer = StringVar(root)
bmi_answer_label = Label(bmi_frame, textvariable=bmi_answer, font=("Arial", 14, "bold"))
bmi_answer_label.grid(row=1, column=3)
bmi_answer.set("BMI: 0")

# ideal weight output
bmi_ideal_weight = StringVar(root)
Label(bmi_frame, textvariable=bmi_ideal_weight, font=("Arial", 14, "bold"), fg="#098f08", width=20).grid(row=1, column=4, columnspan=2, pady=5)
bmi_ideal_weight.set("Ideal: 0")

# clear-button
Button(bmi_frame, text="Clear", width=10, command=bmi_clear, **border("orange", 2), fg="orange", bg="white").grid(row=2, column=1, columnspan=2)
# calculate-button
Button(bmi_frame, text="Calculate", width=10, command=bmi_calculate, **border("#46b950", 2), fg="#46b950", bg="white").grid(row=2, column=3, columnspan=2)

bmi_frame.pack()

root.mainloop()

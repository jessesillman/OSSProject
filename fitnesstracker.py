import tkinter as tk
from tkinter import messagebox
import webbrowser

# Initialize the main window
root = tk.Tk()
root.title("Fitness Tracker Application")

# Set the window size and position
window_width = 400
window_height = 640
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width - window_width) // 2
y = (screen_height - window_height) // 2
root.geometry(f"{window_width}x{window_height}+{x}+{y}")

root.configure(bg="black")

# Helper function to set up title sections consistently
def setup_title_section(parent, title_text, subtitle_text):
    title_frame = tk.Frame(parent, bg="black", pady=20)
    title_frame.pack(fill="x")

    title_label = tk.Label(
        title_frame,
        text=title_text,
        font=("Helvetica", 26, "bold"),
        bg="black",
        fg="white"
    )
    title_label.pack()

    subtitle_label = tk.Label(
        title_frame,
        text=subtitle_text,
        font=("Helvetica", 12, "italic"),
        bg="black",
        fg="gold"
    )
    subtitle_label.pack()

    underline = tk.Frame(parent, bg="gold", height=5)
    underline.pack(fill="x")

# Add the main title section
setup_title_section(root, "Fitness Tracker Application", "An open source application to maintain your fitness")

# Function for BMI Calculator
def on_bmi_click():
    # Create the BMI Calculator window
    bmi_window = tk.Toplevel(root)
    bmi_window.title("BMI Calculator")
    bmi_window.geometry("400x640")  # Match the main window size
    bmi_window.configure(bg="black")

    setup_title_section(bmi_window, "BMI Calculator", "Calculate your Body Mass Index")

    input_frame = tk.Frame(bmi_window, bg="black")
    input_frame.pack(pady=20)

    # Height input
    tk.Label(
        input_frame,
        text="Height (cm):",
        font=("Helvetica", 14),
        bg="black",
        fg="white",
        anchor="w"
    ).grid(row=0, column=0, padx=10, pady=10, sticky="w")
    height_entry = tk.Entry(input_frame, font=("Helvetica", 14), width=10)
    height_entry.grid(row=0, column=1, padx=10, pady=10)

    # Weight input
    tk.Label(
        input_frame,
        text="Weight (kg):",
        font=("Helvetica", 14),
        bg="black",
        fg="white",
        anchor="w"
    ).grid(row=1, column=0, padx=10, pady=10, sticky="w")
    weight_entry = tk.Entry(input_frame, font=("Helvetica", 14), width=10)
    weight_entry.grid(row=1, column=1, padx=10, pady=10)

    # Result label for displaying BMI
    result_label = tk.Label(
        bmi_window,
        text="",
        font=("Helvetica", 14, "bold"),
        bg="black",
        fg="white",
        pady=10
    )
    result_label.pack()

    # Function to calculate BMI
    def calculate_bmi():
        try:
            height = float(height_entry.get()) / 100  # Convert to meters
            weight = float(weight_entry.get())
            bmi = weight / (height ** 2)
            if bmi < 18.5:
                bmi_status = "(Underweight)"
            elif 18.5 <= bmi < 24.9:
                bmi_status = "(Normal)"
            elif 25 <= bmi < 29.9:
                bmi_status = "(Overweight)"
            else:
                bmi_status = "(Obese)"
            result_label.config(text=f"BMI: {bmi:.2f} {bmi_status}")
        except ValueError:
            result_label.config(text="Error: Please enter valid numbers!")

    # Create a frame for buttons
    button_frame = tk.Frame(bmi_window, bg="black")
    button_frame.pack(pady=20)

    # Add Calculate Button
    tk.Button(
        button_frame,
        text="Calculate BMI",
        font=("Helvetica", 14, "bold"),
        bg="gold",
        fg="black",
        padx=20,
        pady=10,
        command=calculate_bmi
    ).grid(row=0, column=0, padx=10)

    # Add Close Button
    tk.Button(
        button_frame,
        text="Close",
        font=("Helvetica", 14, "bold"),
        bg="gold",
        fg="black",
        padx=20,
        pady=10,
        command=bmi_window.destroy
    ).grid(row=0, column=1, padx=10)

    # Add footer text at the bottom of the window
    footer_label = tk.Label(
        bmi_window,
        text="OSS, By: Jesse Sillman",
        font=("Helvetica", 10),
        bg="black",
        fg="white"
    )
    footer_label.pack(side="bottom", pady=10)


# Function for Calorie Calculator
def on_calorie_click():
    calorie_window = tk.Toplevel(root)
    calorie_window.title("Calorie Calculator")
    calorie_window.geometry("400x640")
    calorie_window.configure(bg="black")

    setup_title_section(calorie_window, "Calorie Calculator", "Calculate your daily calorie needs")

    input_frame = tk.Frame(calorie_window, bg="black")
    input_frame.pack(pady=20)

    # Input fields for age, gender, weight, height, and activity level
    fields = [
        {"label": "Age:", "type": "entry"},
        {"label": "Gender (M/F):", "type": "entry"},
        {"label": "Weight (kg):", "type": "entry"},
        {"label": "Height (cm):", "type": "entry"},
        {"label": "Activity Level (1-5):", "type": "entry"}
    ]

    entries = {} # Dictionary to store entry widgets

    for i, field in enumerate(fields):
        tk.Label(
            input_frame,
            text=field["label"],
            font=("Helvetica", 14),
            bg="black",
            fg="white",
            anchor="w"
        ).grid(row=i, column=0, padx=10, pady=10, sticky="w")
        entry = tk.Entry(input_frame, font=("Helvetica", 14), width=10)
        entry.grid(row=i, column=1, padx=10, pady=10)
        entries[field["label"]] = entry # Save the entry widget in the dictionary

    # Result label to display the calculated calories
    result_label = tk.Label(
        calorie_window,
        text="",
        font=("Helvetica", 14, "bold"),
        bg="black",
        fg="white",
        pady=10
    )
    result_label.pack()

    def calculate_calories():
        try:
            age = int(entries["Age:"].get())
            gender = entries["Gender (M/F):"].get().upper()
            weight = float(entries["Weight (kg):"].get())
            height = float(entries["Height (cm):"].get())
            activity_level = int(entries["Activity Level (1-5):"].get())

            # Check for valid gender and activity level
            if gender not in ['M', 'F']:
                raise ValueError("Gender must be 'M' or 'F'")
            if activity_level < 1 or activity_level > 5:
                raise ValueError("Activity level must be between 1 and 5.")

            # BMR Calculation
            if gender == 'M':
                bmr = 88.362 + (13.397 * weight) + (4.799 * height) - (5.677 * age)
            else:
                bmr = 447.593 + (9.247 * weight) + (3.098 * height) - (4.330 * age)

            # Activity factors
            activity_factors = {
                1: 1.2,
                2: 1.375,
                3: 1.55,
                4: 1.725,
                5: 1.9
            }
            daily_calories = bmr * activity_factors[activity_level]
            result_label.config(text=f"Daily Calorie Needs: {daily_calories:.2f} kcal")
        except ValueError as e:
            result_label.config(text=f"Error: {e}")

    # Create a frame for buttons
    button_frame = tk.Frame(calorie_window, bg="black")
    button_frame.pack(pady=20)

    # Add Calculate Button
    tk.Button(
        button_frame,
        text="Calculate Calories",
        font=("Helvetica", 10, "bold"),
        bg="gold",
        fg="black",
        padx=20,
        pady=10,
        command=calculate_calories
    ).grid(row=0, column=0, padx=10)

    # Add Close Button
    tk.Button(
        button_frame,
        text="Close",
        font=("Helvetica", 14, "bold"),
        bg="gold",
        fg="black",
        padx=20,
        pady=10,
        command=calorie_window.destroy
    ).grid(row=0, column=1, padx=10)

    # Add footer text at the bottom of the window
    footer_label = tk.Label(
        calorie_window,
        text="OSS, By: Jesse Sillman",
        font=("Helvetica", 10),
        bg="black",
        fg="white"
    )
    footer_label.pack(side="bottom", pady=10)

# Function for Diet Plan
def on_diet_plan_click():
    diet_window = tk.Toplevel(root)
    diet_window.title("Diet Plan")
    diet_window.geometry("400x640")  # Match the main window size
    diet_window.configure(bg="black")

    setup_title_section(diet_window, "Diet Plan", "Add your food items and calculate total calories")
    
    input_frame = tk.Frame(diet_window, bg="black")
    input_frame.pack(pady=20)

    # Predefined food items with calorie values per unit
    food_items = [
        {"name": "Egg (1 piece)", "calories": 78},
        {"name": "Cereal (1 serving)", "calories": 150},
        {"name": "Banana (1 medium)", "calories": 105},
        {"name": "Cup of Coffee (1 cup)", "calories": 2},
        {"name": "Rice (1 cup)", "calories": 200},
    ]

    # Create a frame for food items and scales
    items_frame = tk.Frame(diet_window, bg="black")
    items_frame.pack(pady=10, padx=20, fill="both", expand=True)

    # Scrollbar for the food list
    scrollbar = tk.Scrollbar(items_frame)
    scrollbar.pack(side="right", fill="y")

    # Canvas for the food list and scales
    canvas = tk.Canvas(items_frame, bg="black", yscrollcommand=scrollbar.set)
    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.config(command=canvas.yview)

    # Frame inside the canvas
    list_frame = tk.Frame(canvas, bg="black")
    canvas.create_window((0, 0), window=list_frame, anchor="nw")

    # Dictionary to store scales for each food item
    scales = {}

    # Function to add a food item to the list
    def add_food_item():
        try:
            name = food_name_entry.get()
            calories = int(food_calories_entry.get())
            if not name:
                raise ValueError("Food name cannot be empty.")
            # Add the new food item to the list
            row = len(scales)  # Get the next row index
            tk.Label(
                list_frame,
                text=f"{name} ({calories} cal):",
                font=("Helvetica", 12),
                bg="black",
                fg="white"
            ).grid(row=row, column=0, padx=10, pady=5, sticky="w")

            scale = tk.Scale(
                list_frame,
                from_=0,
                to=10,
                orient="horizontal",
                bg="black",
                fg="white",
                font=("Helvetica", 10),
                highlightthickness=0
            )
            scale.grid(row=row, column=1, padx=10, pady=5)
            scales[name] = {"scale": scale, "calories": calories}

            # Clear the input fields
            food_name_entry.delete(0, tk.END)
            food_calories_entry.delete(0, tk.END)

            # Update the scrollregion of the canvas
            list_frame.update_idletasks()
            canvas.config(scrollregion=canvas.bbox("all"))

        except ValueError as e:
            messagebox.showerror("Input Error", f"Error: {e}")

    # Function to calculate total calories
    def calculate_total_calories():
        total_calories = 0
        for food, details in scales.items():
            quantity = details["scale"].get()
            total_calories += quantity * details["calories"]
        result_label.config(text=f"Total Calories: {total_calories} kcal")

    # Add initial food items and scales
    for i, food in enumerate(food_items):
        tk.Label(
            list_frame,
            text=f"{food['name']} ({food['calories']} cal):",
            font=("Helvetica", 12),
            bg="black",
            fg="white"
        ).grid(row=i, column=0, padx=10, pady=5, sticky="w")

        scale = tk.Scale(
            list_frame,
            from_=0,
            to=10,
            orient="horizontal",
            bg="black",
            fg="white",
            font=("Helvetica", 10),
            highlightthickness=0
        )
        scale.grid(row=i, column=1, padx=10, pady=5)
        scales[food["name"]] = {"scale": scale, "calories": food["calories"]}

    # Update the scrollregion of the canvas
    list_frame.update_idletasks()
    canvas.config(scrollregion=canvas.bbox("all"))

    # Result label for total calories
    result_label = tk.Label(
        diet_window,
        text="",
        font=("Helvetica", 14, "bold"),
        bg="black",
        fg="white",
        pady=10
    )
    result_label.pack()

    # Create a frame for new food inputs
    new_food_frame = tk.Frame(diet_window, bg="black")
    new_food_frame.pack(pady=10)

    # Input for new food name
    tk.Label(
        new_food_frame,
        text="Food Name:",
        font=("Helvetica", 12),
        bg="black",
        fg="white",
        anchor="w"
    ).grid(row=0, column=0, padx=10, pady=5)
    food_name_entry = tk.Entry(new_food_frame, font=("Helvetica", 12), width=15)
    food_name_entry.grid(row=0, column=1, padx=10, pady=5)

    # Input for new food calories
    tk.Label(
        new_food_frame,
        text="Calories:",
        font=("Helvetica", 12),
        bg="black",
        fg="white",
        anchor="w"
    ).grid(row=1, column=0, padx=10, pady=5)
    food_calories_entry = tk.Entry(new_food_frame, font=("Helvetica", 12), width=15)
    food_calories_entry.grid(row=1, column=1, padx=10, pady=5)

    # Create a frame for buttons
    buttons_frame = tk.Frame(diet_window, bg="black")
    buttons_frame.pack(pady=20)

    # Add buttons for actions
    tk.Button(
        buttons_frame,
        text="Add Food",
        font=("Helvetica", 12, "bold"),
        bg="gold",
        fg="black",
        padx=10,
        pady=5,
        command=add_food_item
    ).grid(row=0, column=0, padx=5)

    tk.Button(
        buttons_frame,
        text="Calculate Total",
        font=("Helvetica", 12, "bold"),
        bg="gold",
        fg="black",
        padx=10,
        pady=5,
        command=calculate_total_calories
    ).grid(row=0, column=1, padx=5)

    tk.Button(
        buttons_frame,
        text="Close",
        font=("Helvetica", 12, "bold"),
        bg="gold",
        fg="black",
        padx=10,
        pady=5,
        command=diet_window.destroy
    ).grid(row=0, column=2, padx=5)

    # Add footer text at the bottom of the window
    footer_label = tk.Label(
        diet_window,
        text="OSS, By: Jesse Sillman",
        font=("Helvetica", 10),
        bg="black",
        fg="white"
    )
    footer_label.pack(side="bottom", pady=10)

# Function for Workouts
def on_workouts_click():
    # Create the Workouts window
    workouts_window = tk.Toplevel(root)
    workouts_window.title("Workouts")
    workouts_window.geometry("400x640")  # Match the main window size
    workouts_window.configure(bg="black")

    setup_title_section(workouts_window, "Workouts", "Add your workouts and track your progress")

    input_frame = tk.Frame(workouts_window, bg="black")
    input_frame.pack(pady=20)

    # Create a Listbox to display workouts
    workout_listbox = tk.Listbox(
        workouts_window,
        font=("Helvetica", 12),
        bg="black",
        fg="white",
        selectmode="single",
        height=15,
        width=35
    )
    workout_listbox.pack(pady=10, padx=20)

    # Create a frame for input fields
    input_frame = tk.Frame(workouts_window, bg="black")
    input_frame.pack(pady=20)

    # Workout Name input
    tk.Label(
        input_frame,
        text="Workout Name:",
        font=("Helvetica", 12),
        bg="black",
        fg="white",
        anchor="w"
    ).grid(row=0, column=0, padx=10, pady=5)
    workout_name_entry = tk.Entry(input_frame, font=("Helvetica", 12), width=15)
    workout_name_entry.grid(row=0, column=1, padx=10, pady=5)

    # Duration input
    tk.Label(
        input_frame,
        text="Duration (mins):",
        font=("Helvetica", 12),
        bg="black",
        fg="white",
        anchor="w"
    ).grid(row=1, column=0, padx=10, pady=5)
    duration_entry = tk.Entry(input_frame, font=("Helvetica", 12), width=15)
    duration_entry.grid(row=1, column=1, padx=10, pady=5)

    # Type input
    tk.Label(
        input_frame,
        text="Type:",
        font=("Helvetica", 12),
        bg="black",
        fg="white",
        anchor="w"
    ).grid(row=2, column=0, padx=10, pady=5)
    type_entry = tk.Entry(input_frame, font=("Helvetica", 12), width=15)
    type_entry.grid(row=2, column=1, padx=10, pady=5)

    # Function to add a workout to the list
    def add_workout():
        name = workout_name_entry.get()
        duration = duration_entry.get()
        type_ = type_entry.get()
        if name and duration and type_:
            workout = f"{name} - {duration} mins - {type_}"
            workout_listbox.insert(tk.END, workout)  # Add workout to Listbox
            workout_name_entry.delete(0, tk.END)
            duration_entry.delete(0, tk.END)
        else:
            messagebox.showerror("Input Error", "All fields are required!")

    # Function to delete the selected workout
    def delete_selected_workout():
        selected_index = workout_listbox.curselection()
        if selected_index:
            workout_listbox.delete(selected_index)  # Delete the selected workout
        else:
            messagebox.showinfo("Info", "No workout selected.")

    # Create a frame for buttons
    buttons_frame = tk.Frame(workouts_window, bg="black")
    buttons_frame.pack(pady=20)

    # Add buttons for actions
    tk.Button(
        buttons_frame,
        text="Add Workout",
        font=("Helvetica", 12, "bold"),
        bg="gold",
        fg="black",
        padx=10,
        pady=5,
        command=add_workout
    ).grid(row=0, column=0, padx=5)

    tk.Button(
        buttons_frame,
        text="Delete Selected",
        font=("Helvetica", 12, "bold"),
        bg="gold",
        fg="black",
        padx=10,
        pady=5,
        command=delete_selected_workout
    ).grid(row=0, column=1, padx=5)

    tk.Button(
        buttons_frame,
        text="Close",
        font=("Helvetica", 12, "bold"),
        bg="gold",
        fg="black",
        padx=10,
        pady=5,
        command=workouts_window.destroy
    ).grid(row=0, column=2, padx=5)

    # Add footer text at the bottom of the window
    footer_label = tk.Label(
        workouts_window,
        text="OSS, By: Jesse Sillman",
        font=("Helvetica", 10),
        bg="black",
        fg="white"
    )
    footer_label.pack(side="bottom", pady=10)

import tkinter as tk
import webbrowser

def on_tutorials_click():
    # Create the Tutorials window
    tutorials_window = tk.Toplevel(root)
    tutorials_window.title("Tutorials")
    tutorials_window.geometry("400x640")  # Match the main window size
    tutorials_window.configure(bg="black")

    setup_title_section(tutorials_window, "Tutorials", "Check out some workout tutorials")

    input_frame = tk.Frame(tutorials_window, bg="black")
    input_frame.pack(pady=20)

    # Function to open YouTube video
    def open_video(url):
        webbrowser.open(url)

    # Create a frame to hold the buttons
    buttons_frame = tk.Frame(tutorials_window, bg="black")
    buttons_frame.pack()

    # Define button texts and corresponding video URLs
    buttons_info = [
        ("Chest", "https://www.youtube.com/watch?v=chest_video"),
        ("Back", "https://www.youtube.com/watch?v=back_video"),
        ("Biceps", "https://www.youtube.com/watch?v=biceps_video"),
        ("Squat", "https://www.youtube.com/watch?v=squat_video"),
        ("Shoulder", "https://www.youtube.com/watch?v=shoulder_video"),
        ("Abs", "https://www.youtube.com/watch?v=abs_video")
    ]

    # Create buttons and place them in a grid
    for i, (text, url) in enumerate(buttons_info):
        button = tk.Button(
            buttons_frame,
            text=text,
            font=("Helvetica", 16, "bold"),
            bg="gold",
            fg="black",
            padx=10,
            pady=5,
            borderwidth=2,
            relief="raised",
            command=lambda url=url: open_video(url),
            width=14,  # Set all buttons to the same width
            height=2
        )
        button.grid(row=i//2, column=i%2, padx=10, pady=40)

    # Add footer label
    footer_label = tk.Label(
        tutorials_window,
        text="OSS, By: Jesse Sillman",
        font=("Helvetica", 10),
        bg="black",
        fg="white"
    )
    footer_label.pack(side="bottom", pady=10)

# Function to create a button with enhanced styling
def create_button(frame, text, command):
    button = tk.Button(
        frame,
        text=text,
        font=("Helvetica", 16, "bold"),
        bg="gold",
        fg="black",
        padx=20,
        pady=10,
        borderwidth=2,
        relief="raised",
        command=command,
        width=20 # Set all buttons to the same width
    )
    button.pack(pady=20)

# Create frames and buttons  for each section
bmi_frame = tk.Frame(root, bg="black")
bmi_frame.pack(pady=6)
create_button(bmi_frame, "BMI Calculator", on_bmi_click)

calorie_frame = tk.Frame(root, bg="black")
calorie_frame.pack(pady=6)
create_button(calorie_frame, "Calorie Calculator", on_calorie_click)

diet_plan_frame = tk.Frame(root, bg="black")
diet_plan_frame.pack(pady=6)
create_button(diet_plan_frame, "Diet Plan", on_diet_plan_click)

workouts_frame = tk.Frame(root, bg="black")
workouts_frame.pack(pady=6)
create_button(workouts_frame, "Workouts", on_workouts_click)

workouts_frame = tk.Frame(root, bg="black")
workouts_frame.pack(pady=6)
create_button(workouts_frame, "Tutorials", on_tutorials_click)

# Add footer text at the bottom of the window
footer_label = tk.Label(
    root,
    text="OSS, By: Jesse Sillman",
    font=("Helvetica", 10),
    bg="black",
    fg="white"
)
footer_label.pack(side="bottom", pady=10)

root.mainloop()
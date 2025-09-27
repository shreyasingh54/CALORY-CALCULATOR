import datetime
print("Welcome to the Calorie Tracker!")
print("This program helps you log meals and track calories.\n")

# ---------- Task 2: Input & Data Collection ----------
meals = []
calories = []

num_meals = int(input("How many meals do you want to enter? "))

for i in range(num_meals):
    meal_name = input(f"Enter meal {i+1} name: ")
    meal_cal = float(input(f"Enter calories for {meal_name}: "))
    meals.append(meal_name)
    calories.append(meal_cal)

# ---------- Task 3: Calorie Calculations ----------
total_cal = sum(calories)
avg_cal = total_cal / len(calories)

daily_limit = float(input("\nEnter your daily calorie limit: "))

# ---------- Task 4: Exceed Limit Warning System ----------
if total_cal > daily_limit:
    status_msg = "⚠ Warning: You exceeded your daily calorie limit!"
else:
    status_msg = "✅ Good job! You're within your daily calorie limit."

# ---------- Task 5: Neatly Formatted Output ----------
print("\n--- Calorie Summary ---")
print(f"{'Meal Name':<15}{'Calories':<10}")
print("-" * 25)

for meal, cal in zip(meals, calories):
    print(f"{meal:<15}{cal:<10.2f}")

print("-" * 25)
print(f"{'Total':<15}{total_cal:<10.2f}")
print(f"{'Average':<15}{avg_cal:<10.2f}")
print(status_msg)

# ---------- Task 6 (Bonus): Save Session Log to File ----------
save = input("\nDo you want to save this report to a file? (yes/no): ").strip().lower()

if save == "yes":
    filename = "calorie_log.txt"
    with open(filename, "w") as f:
        f.write("Calorie Tracker Report\n")
        f.write(f"Date: {datetime.datetime.now()}\n\n")
        f.write(f"{'Meal Name':<15}{'Calories':<10}\n")
        f.write("-" * 25 + "\n")
        for meal, cal in zip(meals, calories):
            f.write(f"{meal:<15}{cal:<10.2f}\n")
        f.write("-" * 25 + "\n")
        f.write(f"{'Total':<15}{total_cal:<10.2f}\n")
        f.write(f"{'Average':<15}{avg_cal:<10.2f}\n")
        f.write(status_msg + "\n")

    print(f"\n✅ Report saved to {filename}")















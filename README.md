# Calorie Tracker

A simple Python program that helps you log meals and track your daily calorie intake. This interactive tool allows you to monitor your eating habits and stay within your daily calorie limits.

## Features

- **Meal Logging**: Enter multiple meals with their calorie counts
- **Calorie Calculations**: Automatically calculates total and average calories
- **Daily Limit Monitoring**: Set a daily calorie limit and get warnings if exceeded
- **Formatted Reports**: View a neatly organized summary of your meals
- **File Export**: Save your calorie tracking session to a text file

## Requirements

- Python 3.x
- No external dependencies required (uses only built-in Python modules)

## Installation

1. Download the `calcul.py` file
2. Make sure you have Python installed on your system
3. No additional installation steps required

## Usage

Run the program from your terminal or command prompt:

```bash
python calcul.py
```

### Program Flow

1. **Welcome Message**: The program greets you and explains its purpose
2. **Meal Entry**: 
   - Enter the number of meals you want to log
   - For each meal, provide the meal name and calorie count
3. **Daily Limit**: Set your daily calorie limit
4. **Summary Display**: View a formatted table showing:
   - All meals with their calories
   - Total calories consumed
   - Average calories per meal
   - Status message (within limit or exceeded)
5. **Optional File Save**: Choose to save the report to `calorie_log.txt`

### Example Session

```
Welcome to the Calorie Tracker!
This program helps you log meals and track calories.

How many meals do you want to enter? 3
Enter meal 1 name: Breakfast
Enter calories for Breakfast: 350
Enter meal 2 name: Lunch
Enter calories for Lunch: 550
Enter meal 3 name: Dinner
Enter calories for Dinner: 650

Enter your daily calorie limit: 2000

--- Calorie Summary ---
Meal Name      Calories  
-------------------------
Breakfast      350.00    
Lunch          550.00    
Dinner         650.00    
-------------------------
Total          1550.00   
Average        516.67    
✅ Good job! You're within your daily calorie limit.

Do you want to save this report to a file? (yes/no): yes

✅ Report saved to calorie_log.txt
```

## Output Files

When you choose to save your session, the program creates a `calorie_log.txt` file containing:
- Current date and time
- Complete meal summary table
- Total and average calories
- Daily limit status

## Status Messages

- ✅ **Within Limit**: "Good job! You're within your daily calorie limit."
- ⚠️ **Exceeded Limit**: "Warning: You exceeded your daily calorie limit!"

## Tips

- Enter accurate calorie counts for better tracking
- Set realistic daily calorie limits based on your health goals
- Save your reports to track progress over multiple sessions
- Use decimal numbers for precise calorie entries (e.g., 125.5)

## License

This project is open source and available for personal use and modification.

## Contributing

Feel free to fork this project and submit improvements or bug fixes!

import statistics
import datetime

def classify_sleep(hours):
    """Return sleep quality category based on hours slept."""
    if hours < 4:
        return "Very Poor"
    elif 4 <= hours < 6:
        return "Poor"
    elif 6 <= hours < 7:
        return "Below Average"
    elif 7 <= hours < 9:
        return "Healthy"
    elif 9 <= hours <= 10:
        return "Above Average"
    else:
        return "Excessive"


def sleep_score(hours):
    """Calculate a numeric sleep quality score."""
    if hours < 4:
        return 20
    elif 4 <= hours < 6:
        return 40
    elif 6 <= hours < 7:
        return 60
    elif 7 <= hours < 9:
        return 90
    elif 9 <= hours <= 10:
        return 75
    else:
        return 50


def give_suggestions(hours):
    """Return personalized suggestions."""
    if hours < 4:
        return "Try sleeping earlier. Avoid screens and caffeine. Maintain a fixed bedtime routine."
    elif 4 <= hours < 6:
        return "Increase sleep duration by 1–2 hours. Reduce late-night activities."
    elif 6 <= hours < 7:
        return "Almost good! Try to add 30–45 minutes more to reach ideal sleep."
    elif 7 <= hours < 9:
        return "Great! Maintain your sleep schedule consistently."
    elif 9 <= hours <= 10:
        return "Long sleep is fine sometimes, but ensure you're physically active."
    else:
        return "Oversleeping may signal stress or irregular habits. Try balancing your routine."


def calculate_sleep_debt(hours):
    """Calculate sleep debt assuming ideal sleep = 8 hours."""
    ideal_sleep = 8
    return ideal_sleep - hours


def analyze_single_day(hours):
    """Full analysis for a single day."""
    category = classify_sleep(hours)
    score = sleep_score(hours)
    suggestion = give_suggestions(hours)
    debt = calculate_sleep_debt(hours)

    analysis = f"""
----------------------------------------------------
              Daily Sleep Analysis
----------------------------------------------------
Hours Slept         : {hours} hours
Sleep Category      : {category}
Sleep Score         : {score}/100
Sleep Debt          : {debt} hours (negative means oversleep)
Suggestions         : {suggestion}
----------------------------------------------------
"""
    return analysis


def analyze_weekly_sleep(week_data):
    """Analyze sleep for 7 days."""
    avg_sleep = statistics.mean(week_data)
    best = max(week_data)
    worst = min(week_data)

    avg_score = statistics.mean([sleep_score(h) for h in week_data])

    report = f"""
====================================================
                WEEKLY SLEEP REPORT
====================================================
Sleep Data (hours/day): {week_data}
Average Sleep Duration : {round(avg_sleep, 2)} hours/day
Best Sleep Duration    : {best} hours
Worst Sleep Duration   : {worst} hours
Average Sleep Score    : {round(avg_score, 2)}/100
Weekly Sleep Category  : {classify_sleep(avg_sleep)}
====================================================
"""

    return report




print("============================================")
print("        SLEEP PATTERN ANALYZER TOOL         ")
print("============================================")

print("\n1. Analyze Single Day Sleep")
print("2. Analyze Weekly Sleep Pattern")

choice = input("\nEnter your choice (1 or 2): ")

if choice == "1":
    try:
        hours = float(input("\nEnter hours slept today: "))
        print(analyze_single_day(hours))

    except ValueError:
        print("Invalid input. Please enter a valid number.")

elif choice == "2":
    week_data = []
    print("\nEnter sleep hours for 7 days:")

    for i in range(1, 8):
        while True:
            try:
                hrs = float(input(f"Day {i}: "))
                week_data.append(hrs)
                break
            except ValueError:
                print("Invalid input. Enter a number.")

    print(analyze_weekly_sleep(week_data))

else:
    print("Invalid choice. Please select 1 or 2.")
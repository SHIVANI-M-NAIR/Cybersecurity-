import string

def assess_password_strength(password):
    length_criteria = len(password) >= 8
    upper_criteria = any(c.isupper() for c in password)
    lower_criteria = any(c.islower() for c in password)
    digit_criteria = any(c.isdigit() for c in password)
    special_chars = string.punctuation
    special_criteria = any(c in special_chars for c in password)

    score = 0
    if length_criteria:
        score += 1
    if upper_criteria:
        score += 1
    if lower_criteria:
        score += 1
    if digit_criteria:
        score += 1
    if special_criteria:
        score += 1

    # Decide strength label
    if score <= 2:
        strength = "Weak"
    elif score == 3:
        strength = "Medium"
    elif score == 4:
        strength = "Strong"
    else:
        strength = "Very Strong"

    # Suggestions
    suggestions = []
    if not length_criteria:
        suggestions.append("Use at least 8 characters.")
    if not upper_criteria:
        suggestions.append("Add at least one uppercase letter (A–Z).")
    if not lower_criteria:
        suggestions.append("Add at least one lowercase letter (a–z).")
    if not digit_criteria:
        suggestions.append("Add at least one digit (0–9).")
    if not special_criteria:
        suggestions.append(f"Add at least one special character ({special_chars}).")

    return score, strength, suggestions


def main():
    print("=== Password Strength Checker ===")
    password = input("Enter a password to check: ")

    score, strength, suggestions = assess_password_strength(password)

    print("\nResults:")
    print(f"- Score: {score}/5")
    print(f"- Strength: {strength}")

    if suggestions:
        print("\nHow to improve your password:")
        for s in suggestions:
            print(f"• {s}")
    else:
        print("\nNice! Your password meets all criteria.")


if __name__ == "__main__":
    main()

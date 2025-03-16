import re

def check_password_strength(password):
    # Initialize variables
    score = 0
    feedback = []
    common_passwords = ['password', '123456', 'qwerty', 'letmein', 'admin']
    
    # Length check
    length = len(password)
    if length >= 12:
        score += 3
    elif length >= 8:
        score += 2
    else:
        feedback.append("Password is too short (minimum 8 characters)")
    
    # Character diversity checks
    checks = {
        'uppercase': r'[A-Z]',
        'lowercase': r'[a-z]',
        'digit': r'\d',
        'special': r'[!@#$%^&*(),.?":{}|<>]'
    }
    
    for name, pattern in checks.items():
        if re.search(pattern, password):
            score += 1
        else:
            feedback.append(f"Missing {name} character")
    
    # Common password check
    if password.lower() in common_passwords:
        score -= 2
        feedback.append("Common password detected")
    
    # Consecutive characters check
    if re.search(r'(.)\1{2,}', password):
        score -= 1
        feedback.append("Repeating characters detected")
    
    # Sequential characters check (3+)
    sequences = ['abcdefghijklmnopqrstuvwxyz', 'zyxwvutsrqponmlkjihgfedcba', '0123456789']
    for seq in sequences:
        for i in range(len(seq)-3):
            if seq[i:i+4] in password.lower():
                score -= 1
                feedback.append("Sequential pattern detected")
                break
    
    # Determine strength rating
    strength = "Very Weak"
    if score >= 7:
        strength = "Very Strong"
    elif score >= 5:
        strength = "Strong"
    elif score >= 3:
        strength = "Moderate"
    elif score >= 1:
        strength = "Weak"
    
    return {
        'strength': strength,
        'score': score,
        'feedback': feedback,
        'length': length
    }

# User interface
print("Password Strength Checker")
print("-------------------------")
password = input("Enter password to assess: ")

result = check_password_strength(password)

print(f"\nPassword Strength: {result['strength']}")
print(f"Length: {result['length']} characters")
print(f"Score: {result['score']}/8")

if result['feedback']:
    print("\nRecommendations:")
    for item in result['feedback']:
        print(f"- {item}")
else:
    print("\nYour password meets all basic security requirements!")

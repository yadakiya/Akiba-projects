
def check_minimum_length(password, minimum_length=8):
    return len(password) >= minimum_length


def check_uppercase(password):
    for char in password:
        if char.isupper():
            return True

    return False


def check_lowercase(password):
    for char in password:
        if char.islower():
            return True

    return False


def check_digit(password):
    for char in password:
        if char.isdigit():
            return True

    return False


def check_special_character(password):
    for char in password:
        if not char.isalnum() and not char.isspace():
            return True

    return False


def analyze_password(password, minimum_length=8):
    results = {
        "minimum_length": check_minimum_length(
            password, minimum_length
        ),
        "uppercase": check_uppercase(password),
        "lowercase": check_lowercase(password),
        "digit": check_digit(password),
        "special_character": check_special_character(password)
    }

    requirements = {
        "minimum_length": (
            f"At least {minimum_length} characters long"
        ),
        "uppercase": "Contains an uppercase letter (A-Z)",
        "lowercase": "Contains a lowercase letter (a-z)",
        "digit": "Contains a digit (0-9)",
        "special_character": (
            "Contains a special character (e.g. !, @, #)"
        )
    }

    passed = []
    failed = []

    for requirement, is_valid in results.items():
        if is_valid:
            passed.append(requirements[requirement])
        else:
            failed.append(requirements[requirement])

    return {
        "checks": results,
        "passed_requirements": passed,
        "failed_requirements": failed,
        "is_valid": len(failed) == 0
    }


def display_password_report(password, minimum_length=8):
    report = analyze_password(password, minimum_length)

    print("\n===== PASSWORD ANALYSIS =====")

    for requirement, passed in report["checks"].items():
        status = "PASS" if passed else "FAIL"
        print(f"{requirement}: {status}")

    print("\nPassed requirements:")
    if report["passed_requirements"]:
        for requirement in report["passed_requirements"]:
            print(f"- {requirement}")
    else:
        print("- None")

    print("\nMissing requirements:")
    if report["failed_requirements"]:
        for requirement in report["failed_requirements"]:
            print(f"- {requirement}")
    else:
        print("- None")

    print(
        "\nPolicy result:",
        "PASS" if report["is_valid"] else "FAIL"
    )


# Five fictional test passwords
test_passwords = [
    "hello",
    "HELLO123",
    "Hello123",
    "Hello@123",
    "Ab1!"
]

for password in test_passwords:
    print(f"\nTesting fictional password: {password}")
    display_password_report(password)


# Test a different minimum length
print("\nTesting configurable minimum length:")
display_password_report("Ab1!", minimum_length=4)

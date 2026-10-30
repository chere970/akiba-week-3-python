def validate_score(score) -> bool:
    """Check that the score is a number between 0 and 100 inclusive."""
    if not isinstance(score, (int, float)):
        return False
    return 0 <= score <= 100


def calculate_grade(score: float) -> str:
    """Return the letter grade corresponding to a numerical score."""
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"


def calculate_average(students: list[dict]) -> float:
    """Calculate the class mean score without using sum()."""
    if not students:
        return 0.0

    total_score = 0.0
    for student in students:
        total_score += student["score"]

    return total_score / len(students)


def find_highest_and_lowest(students: list[dict]) -> tuple[dict, dict]:
    """Find the top and bottom scoring students without max() or min()."""
    if not students:
        return {}, {}

    highest_student = students[0]
    lowest_student = students[0]

    for student in students[1:]:
        if student["score"] > highest_student["score"]:
            highest_student = student
        if student["score"] < lowest_student["score"]:
            lowest_student = student

    return highest_student, lowest_student


def count_passed_and_failed(students: list[dict], pass_threshold: float = 50.0) -> tuple[int, int]:
    """Count how many students met or exceeded the passing threshold."""
    passed = 0
    failed = 0

    for student in students:
        if student["score"] >= pass_threshold:
            passed += 1
        else:
            failed += 1

    return passed, failed


def get_above_average_students(students: list[dict], average_score: float) -> list[dict]:
    """Challenge: Return students whose scores strictly exceed the class average."""
    above_average = []
    for student in students:
        if student["score"] > average_score:
            above_average.append(student)
    return above_average


def generate_class_report(students: list[dict], pass_threshold: float = 50.0) -> None:
    """Validate all student entries, aggregate stats, and print a formatted summary."""
    # 1. Validation filter
    valid_students = []
    for s in students:
        if validate_score(s.get("score")):
            valid_students.append(s)
        else:
            print(f"[Warning] Invalid score for student '{s.get('name')}': {s.get('score')}. Skipped.")

    if not valid_students:
        print("No valid student records found to analyze.")
        return

    # 2. Metric computations
    avg_score = calculate_average(valid_students)
    highest, lowest = find_highest_and_lowest(valid_students)
    passed_count, failed_count = count_passed_and_failed(valid_students, pass_threshold)
    above_avg_students = get_above_average_students(valid_students, avg_score)

    # 3. Print Roster
    print("=" * 48)
    print("             STUDENT GRADE ROSTER               ")
    print("=" * 48)
    print(f"{'Name':<12} | {'Score':<8} | {'Grade':<6} | {'Status'}")
    print("-" * 48)
    for s in valid_students:
        score = s["score"]
        grade = calculate_grade(score)
        status = "Pass" if score >= pass_threshold else "Fail"
        print(f"{s['name']:<12} | {score:<8.1f} | {grade:<6} | {status}")

    # 4. Print Summary Statistics
    print("=" * 48)
    print("             CLASS PERFORMANCE REPORT           ")
    print("=" * 48)
    print(f"Total Valid Students : {len(valid_students)}")
    print(f"Class Average Score  : {avg_score:.2f}")
    print(f"Highest Score        : {highest['score']} ({highest['name']})")
    print(f"Lowest Score         : {lowest['score']} ({lowest['name']})")
    print(f"Passed (>= {pass_threshold})      : {passed_count}")
    print(f"Failed (< {pass_threshold})       : {failed_count}")
    print("-" * 48)

    # 5. Print Challenge Result
    print(f"Students Scoring Above Class Average ({avg_score:.2f}):")
    for s in above_avg_students:
        print(f" - {s['name']}: {s['score']}")
    print("=" * 48)


# --- Example Execution ---
if __name__ == "__main__":
    students = [
        {"name": "Sara", "score": 85},
        {"name": "Ahmed", "score": 42},
        {"name": "Musa", "score": 93},
        {"name": "Hana", "score": 67}
    ]

    generate_class_report(students, pass_threshold=50)
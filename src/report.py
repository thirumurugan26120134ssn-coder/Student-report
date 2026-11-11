from pathlib import Path

def load_students(file_path):
    students = []

    with open(file_path, "r") as file:
        for line in file:
            line = line.strip()

            if not line:
                continue

            name, marks = line.split(",")
            students.append((name, int(marks)))

    return students


def generate_report(students):

    total_students = len(students)

    total_marks = sum(marks for name, marks in students)

    average = total_marks / total_students

    topper = max(students, key=lambda student: student[1])

    passed = sum(1 for name, marks in students if marks >= 50)

    failed = total_students - passed

    report = f"""
===== STUDENT PERFORMANCE REPORT =====

Total Students: {total_students}

Average Marks: {average:.2f}

Topper: {topper[0]}
Highest Marks: {topper[1]}

Passed Students: {passed}
Failed Students: {failed}

Status: REPORT GENERATED SUCCESSFULLY
"""

    return report


def main():

    base_dir = Path(__file__).resolve().parent.parent

    input_file = "./input/students.txt"
    output_file ="./output/report.txt"

    students = load_students(input_file)

    report = generate_report(students)

    output_file.parent.mkdir(exist_ok=True)

    with open(output_file, "w") as file:
        file.write(report)

    print(report)

    print("Report saved successfully!")


if __name__ == "__main__":
    main()

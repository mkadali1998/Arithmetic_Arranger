def arithmetic_arranger(problems, display_answers=False):
    # 1. Error if too many problems
    if len(problems) > 5:
        return "Error: Too many problems."

    first_line = []
    second_line = []
    dashes = []
    answers = []

    for problem in problems:
        parts = problem.split()

        # 2. Error if not in correct format
        if len(parts) != 3:
            return "Error: Invalid problem format."

        first, operator, second = parts

        # 3. Operator must be + or -
        if operator not in ["+", "-"]:
            return "Error: Operator must be '+' or '-'."

        # 4. Operands must be digits
        if not first.isdigit() or not second.isdigit():
            return "Error: Numbers must only contain digits."

        # 5. Operands max 4 digits
        if len(first) > 4 or len(second) > 4:
            return "Error: Numbers cannot be more than four digits."

        # Formatting
        width = max(len(first), len(second)) + 2
        top = first.rjust(width)
        bottom = operator + second.rjust(width - 1)
        line = "-" * width

        first_line.append(top)
        second_line.append(bottom)
        dashes.append(line)

        # Compute answer if requested
        if display_answers:
            if operator == "+":
                result = str(int(first) + int(second))
            else:
                result = str(int(first) - int(second))
            answers.append(result.rjust(width))

    # Join all parts with four spaces
    arranged_problems = "    ".join(first_line) + "\n" + \
                        "    ".join(second_line) + "\n" + \
                        "    ".join(dashes)

    if display_answers:
        arranged_problems += "\n" + "    ".join(answers)

    return arranged_problems

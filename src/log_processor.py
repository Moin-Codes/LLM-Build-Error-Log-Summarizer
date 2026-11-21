
def process_logs(file_path):
    errors = []
    warnings = []
    info = []

    with open(file_path, "r", encoding="utf-8") as file:
        for line in file:
            line = line.strip()

            if "[ERROR]" in line:
                errors.append(line)

            elif "[WARNING]" in line:
                warnings.append(line)

            elif "[INFO]" in line:
                info.append(line)

    return {
        "errors": errors,
        "warnings": warnings,
        "info": info
    }


if __name__ == "__main__":
    result = process_logs("sample_logs/build_error.log")

    print("===== LOG ANALYSIS =====")
    print("Total Errors:", len(result["errors"]))
    print("Total Warnings:", len(result["warnings"]))
    print("Total Info Messages:", len(result["info"]))

    print("\nDetected Errors:")
    for error in result["errors"]:
        print(error)

    print("\nDetected Warnings:")
    for warning in result["warnings"]:
        print(warning)

from pathlib import Path
from log_processor import process_logs
from llm_summarizer import summarize_logs

project_dir = Path(__file__).resolve().parent.parent

file_path = project_dir / "sample_logs" / "build_error.log"

print("===== LLM BUILD LOG SUMMARIZER =====")

log_data = process_logs(file_path)

print("Total Errors:", len(log_data["errors"]))
print("Total Warnings:", len(log_data["warnings"]))
print("Total Info Messages:", len(log_data["info"]))

print("\nGenerating AI summary... Please wait.\n")

summary = summarize_logs(log_data)

print("===== AI GENERATED SUMMARY =====")
print(summary)

output_path = project_dir / "logs" / "summary.txt"

with open(output_path, "w", encoding="utf-8") as file:
    file.write(summary)

print("\nSummary saved to logs/summary.txt")
# LLM-Based Build/Error-Log Summarizer

## 1. Project Overview

The LLM-Based Build/Error-Log Summarizer is a Python-based DevOps automation project that uses a Large Language Model (LLM) to analyze software build logs, identify errors and warnings, generate summaries, and recommend possible solutions.

The project integrates Google's Gemini AI to simplify troubleshooting and help developers understand build failures more efficiently.

## 2. Problem Statement

Software development and DevOps pipelines generate large amounts of build and execution logs. Manually analyzing these logs to identify failures and their possible causes can be time-consuming.

This project addresses the problem by automatically extracting important log messages and using an LLM to produce a structured analysis.

## 3. Objectives

- Read and process software build logs.
- Identify errors, warnings, and informational messages.
- Count the occurrences of each log category.
- Integrate Gemini AI for intelligent log summarization.
- Identify possible root causes of build failures.
- Recommend troubleshooting solutions.
- Save the generated summary to a text file.

## 4. Technologies Used

| Technology | Purpose |
|---|---|
| Python 3.14 | Main programming language |
| Google Gemini API | LLM-based log analysis |
| google-genai | Python SDK for Gemini |
| python-dotenv | Secure environment variable management |
| VS Code | Development environment |
| Git and GitHub | Version control and project hosting |

## 5. Project Structure

```text
LLM-Build-Error-Log-Summarizer/
│
├── src/
│   ├── main.py
│   ├── log_processor.py
│   └── llm_summarizer.py
│
├── sample_logs/
│   └── build_error.log
│
├── logs/
│   └── summary.txt
│
├── documentation/
│
├── requirements.txt
├── README.md
├── .gitignore
└── .env (not uploaded to GitHub)
```

## 6. Implementation Steps

### Step 1: Project Setup

Created the project directory and organized the Python source code, sample logs, and output files into separate folders.

### Step 2: Virtual Environment

Created and activated a Python virtual environment to isolate project dependencies.

### Step 3: Dependency Installation

Installed the `google-genai` and `python-dotenv` libraries and recorded dependencies in `requirements.txt`.

### Step 4: Sample Log Creation

Created a sample build log containing informational messages, warnings, and errors representing software build failures.

### Step 5: Log Processing

Implemented `log_processor.py` to read the log file and classify messages into three categories: ERROR, WARNING, and INFO.

### Step 6: Gemini API Integration

Configured a Gemini API key using environment variables and connected the application to Google's Gemini AI service.

### Step 7: AI-Based Summarization

Implemented `llm_summarizer.py` to send processed log information to the Gemini 3.5 Flash Lite model.

The LLM generates a structured report containing:

1. Build status
2. Error summary
3. Possible root causes
4. Warning analysis
5. Recommended solutions
6. Overall conclusion

### Step 8: Main Application

Implemented `main.py` to integrate log processing and AI summarization, display the results, and save the report to `logs/summary.txt`.

### Step 9: Execution and Verification

Executed the application successfully and verified that the generated summary contained the detected errors, warnings, possible causes, and recommended solutions.

## 7. Results

The application successfully processed the sample build log and produced the following results:

| Category | Count |
|---|---:|
| Errors | 5 |
| Warnings | 2 |
| Informational messages | 6 |

**Build Status:** FAILED

### Errors Identified

- Missing Python `requests` module.
- Application compilation failure.
- Failed `test_user_login` unit test.
- Database connection timeout.
- Overall build failure.

### Recommendations Generated

- Install missing dependencies.
- Verify database connectivity.
- Investigate compilation failures.
- Debug the failed unit test.
- Update outdated dependencies.

The AI-generated report was saved to `logs/summary.txt`.

## 8. How to Run the Project

### Clone the Repository

```bash
git clone <repository-url>
cd LLM-Build-Error-Log-Summarizer
```

Replace `<repository-url>` with the actual GitHub repository URL.

### Create a Virtual Environment

```bash
python -m venv venv
```

Activate it on Windows PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Configure the API Key

Create a `.env` file in the project root:

```env
GEMINI_API_KEY=your_api_key_here
```

### Run the Application

```bash
python src/main.py
```

The generated report will be saved in `logs/summary.txt`.

## 9. Learning Outcomes

Through this assignment, I learned:

- How software build logs are generated and analyzed.
- How to classify errors, warnings, and informational messages using Python.
- How to integrate an LLM into a Python application.
- How to use the Gemini API for automated text analysis.
- How to manage API keys securely using environment variables.
- How to implement a modular Python project.
- How AI can assist developers in troubleshooting software build failures.
- How to save generated reports for future reference.

## 10. Future Enhancements

Potential improvements include:

- Supporting multiple log file formats.
- Analyzing logs from GitHub Actions and Jenkins pipelines.
- Developing a web-based dashboard.
- Automatically detecting recurring errors.
- Integrating with CI/CD pipelines.

## 11. Conclusion

The LLM-Based Build/Error-Log Summarizer successfully demonstrates how Large Language Models can assist with DevOps troubleshooting.

The application automatically processes build logs, identifies important messages, generates a structured AI-based analysis, and recommends possible solutions.

This project demonstrates the practical application of generative AI in software development and DevOps automation.
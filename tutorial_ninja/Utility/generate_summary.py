import json
import os

passed = 0
failed = 0
broken = 0
skipped = 0

# Determine the correct path to allure-results
allure_results_path = "tutorial_ninja/allure-results"
if not os.path.exists(allure_results_path):
    allure_results_path = "allure-results"

# Debug: Print directory contents
print(f"Checking path: {allure_results_path}")
print(f"Path exists: {os.path.exists(allure_results_path)}")

if os.path.exists(allure_results_path):
    files = os.listdir(allure_results_path)
    print(f"Files found: {files}")
    
    for file in files:
        if not file.endswith(".json"):
            continue
        
        try:
            file_path = os.path.join(allure_results_path, file)
            with open(file_path, encoding="utf-8") as f:
                data = json.load(f)
            
            # Check if this is a test result file (has status field)
            if "status" in data:
                status = data.get("status")
                print(f"File: {file}, Status: {status}")
                
                if status == "passed":
                    passed += 1
                elif status == "failed":
                    failed += 1
                elif status == "broken":
                    broken += 1
                elif status == "skipped":
                    skipped += 1
        except (json.JSONDecodeError, IOError) as e:
            print(f"Error reading {file}: {e}")
else:
    print(f"Error: allure-results directory not found at {allure_results_path}")
        
total = passed + failed + broken + skipped

# Create email_body.txt in the root directory
email_body_path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))), "email_body.txt")

email_content = f"""Test Execution Summary

Total Tests: {total}
Passed: {passed}
Failed: {failed}
Broken: {broken}
Skipped: {skipped}

Allure Report:
https://reports.yourdomain.com/latest
"""

print(f"Creating email body at: {email_body_path}")
print(f"Content:\n{email_content}")

with open(email_body_path, "w") as f:
    f.write(email_content)

print("Email body created successfully")
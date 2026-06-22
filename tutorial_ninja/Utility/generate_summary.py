import json
import os

passed = 0
failed = 0
broken = 0
skipped = 0

for file in os.listdir("allure-results"):
    if not file.endswith("-results.json"):
        continue
    
    with open(os.path.join("allure-results",file),encoding="utf-8") as f:
        data = json.load(f)
    
    status = data.get("status")
    
    if status == "passed":
        passed += 1
    elif status == "failed":
        failed += 1
    elif status == "broken":
        broken += 1
    elif status == "skipped":
        skipped += 1
        
total = passed + failed + broken + skipped

with open("email_body.txt", w) as f:
    f.write(f"""
        Test Execution Summary

        Total Tests: {total}
        Passed: {passed}
        Failed: {failed}
        Broken: {broken}
        Skipped: {skipped}

        Allure Report:
        https://reports.yourdomain.com/latest
        """)
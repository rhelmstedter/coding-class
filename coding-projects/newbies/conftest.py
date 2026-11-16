"""Report Newbie Bite test results to Mr. Helmstedter's results form.

The Run Tests cell downloads this file next to the test file, so pytest loads it
automatically. After the tests finish it sends one row (student email, bite,
passed, failed, total, notebook ID) to a Google Form. Reporting never changes the test
outcome: if it fails for any reason, students still see their normal results.
"""
import os
import subprocess
import urllib.parse
import urllib.request

FORM_URL = "https://docs.google.com/forms/d/e/1FAIpQLSe_ViyIujLnA7uGDuIJsGV3mjnPj1L5XzP11JRbcTSB7_NqHQ/formResponse"
ENTRY = {
    "email": "entry.1033835523",
    "bite": "entry.1958362965",
    "passed": "entry.1564096096",
    "failed": "entry.2104151103",
    "total": "entry.323146220",
    "notebook": "entry.1212619380",
}


def _student_email():
    # Typed in the Run Tests cell when Google sign-in is blocked or fails.
    typed = os.environ.get("STUDENT_EMAIL", "").strip().lower()
    if "@" in typed:
        return typed
    try:
        out = subprocess.run(
            ["gcloud", "config", "get-value", "account"],
            capture_output=True, text=True, timeout=20,
        )
        email = out.stdout.strip()
        return email if "@" in email else "unknown"
    except Exception:
        return "unknown"


def pytest_sessionfinish(session, exitstatus):
    reporter = session.config.pluginmanager.get_plugin("terminalreporter")
    if reporter is None:
        return
    passed = len(reporter.stats.get("passed", []))
    failed = len(reporter.stats.get("failed", [])) + len(reporter.stats.get("error", []))
    total = passed + failed
    if total == 0:
        return
    data = urllib.parse.urlencode({
        ENTRY["email"]: _student_email(),
        ENTRY["bite"]: os.environ.get("BITE", "unknown"),
        ENTRY["passed"]: passed,
        ENTRY["failed"]: failed,
        ENTRY["total"]: total,
        # The Drive file ID of the notebook that ran the tests. The results Sheet
        # looks up who owns that copy, so a typo or someone else's email can't misfile a result.
        ENTRY["notebook"]: os.environ.get("COLAB_NOTEBOOK_ID", ""),
    }).encode()
    try:
        urllib.request.urlopen(FORM_URL, data=data, timeout=15)
        print("\n✅ Your results were sent to Mr. Helmstedter.")
    except Exception:
        print("\n⚠️ Your results could not be sent. Run the tests again, or tell Mr. Helmstedter.")

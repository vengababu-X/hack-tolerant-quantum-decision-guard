import hashlib
import time
import os
from recovery.rollback import rollback_system
from decision.decision_monitor import decision_warning
from security.emergency_mode import activate_emergency
from security.audit_log import audit

PROTECTED_FILE = "protected.txt"
HASH_FILE = "logs/known_hash.txt"

def sha256(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        h.update(f.read())
    return h.hexdigest()

def save_baseline():
    os.makedirs("logs", exist_ok=True)
    with open(HASH_FILE, "w") as f:
        f.write(sha256(PROTECTED_FILE))

def monitor():
    baseline = open(HASH_FILE).read().strip()
    while True:
        if sha256(PROTECTED_FILE) != baseline:
            with open("logs/alert.log", "a") as log:
                log.write("Tampering detected\n")
            audit("Tampering detected")
            activate_emergency()
            rollback_system()
            decision_warning()
            break
        time.sleep(2)

if __name__ == "__main__":
    if not os.path.exists(HASH_FILE):
        save_baseline()
    monitor()

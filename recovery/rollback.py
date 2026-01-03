import shutil
from security.audit_log import audit

def rollback_system():
    shutil.copy("snapshots/protected_backup.txt", "protected.txt")
    audit("Rollback to trusted snapshot completed")

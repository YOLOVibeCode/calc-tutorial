#!/usr/bin/env python3
"""Verify development environment setup."""

import sys
from pathlib import Path

def check_import(module_name: str) -> bool:
    """Try to import a module and return success status."""
    try:
        __import__(module_name)
        return True
    except ImportError:
        return False

def main():
    """Run all verification checks."""
    print("🔍 Verifying Calculator Development Environment\n")
    print("=" * 60)
    
    checks = [
        ("Python Version", f"{sys.version.split()[0]}", sys.version_info >= (3, 10)),
        ("PyQt6", "Installed", check_import("PyQt6")),
        ("PyQt6.QtWidgets", "Installed", check_import("PyQt6.QtWidgets")),
        ("PyQt6.QtCore", "Installed", check_import("PyQt6.QtCore")),
        ("pytest", "Installed", check_import("pytest")),
        ("pytest-qt", "Installed", check_import("pytestqt")),
        ("pytest-cov", "Installed", check_import("pytest_cov")),
    ]
    
    all_passed = True
    
    for name, detail, passed in checks:
        status = "✅" if passed else "❌"
        print(f"{status} {name:.<30} {detail}")
        if not passed:
            all_passed = False
    
    print("=" * 60)
    
    # Check project files
    print("\n📁 Project Files")
    print("=" * 60)
    
    project_files = [
        "requirements.txt",
        "CALCULATOR_SPEC.md",
        "IMPLEMENTATION_PLAN.md",
        "SETUP.md",
        ".cursor/rules/python-pyqt6-calculator.mdc",
    ]
    
    for file_path in project_files:
        exists = Path(file_path).exists()
        status = "✅" if exists else "❌"
        print(f"{status} {file_path}")
        if not exists:
            all_passed = False
    
    print("=" * 60)
    
    if all_passed:
        print("\n🎉 SUCCESS! All checks passed.")
        print("\n📖 Next steps:")
        print("   1. Read IMPLEMENTATION_PLAN.md")
        print("   2. Create project structure: mkdir -p src/ui tests")
        print("   3. Start TDD: Write your first test!")
        print("\n🚀 Ready to build the calculator!")
        return 0
    else:
        print("\n❌ FAILED: Some checks did not pass.")
        print("\n💡 Try:")
        print("   source venv/bin/activate")
        print("   pip install -r requirements.txt")
        return 1

if __name__ == "__main__":
    sys.exit(main())

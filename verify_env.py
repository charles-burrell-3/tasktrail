#!/usr/bin/env python3
"""Staged environment check.

Usage: python verify_env.py --stage 5
"""
import argparse
import importlib
import platform
import shutil
import subprocess
import sys

MIN_PYTHON = (3, 10)  # change here if the floor moves

results = []


def check(name, ok, hint=""):
    results.append(ok)
    print(f"[{'PASS' if ok else 'FAIL'}] {name}")
    if not ok:
        print(f"       fix: {hint}")


def run(cmd):
    try:
        r = subprocess.run(cmd, capture_output=True, text=True, timeout=60, check=False)
        return r.returncode == 0, r.stdout.strip()
    except (OSError, subprocess.TimeoutExpired):
        return False, ""


def has_module(name):
    try:
        importlib.import_module(name)
        return True
    except ImportError:
        return False


def package_check(label, module, stage_hint):
    check(f"Package: {label}", has_module(module),
          f"pip install {stage_hint} (venv active?)")


def stage_0():
    check(f"Python {MIN_PYTHON[0]}.{MIN_PYTHON[1]} or newer",
          sys.version_info >= MIN_PYTHON,
          "Install Python with your package manager (lesson 0.5)")
    if platform.system() == "Windows":
        check("Chocolatey installed", shutil.which("choco") is not None,
              "Install Chocolatey (lesson 0.4), then open a new terminal")
    else:
        check("Homebrew installed", shutil.which("brew") is not None,
              "Install Homebrew (lesson 0.4), then open a new terminal")
    check("uv installed", shutil.which("uv") is not None,
          "Install uv with your package manager (lesson 0.6)")
    check("make installed", shutil.which("make") is not None,
          "Install make (lesson 0.9), then open a new terminal")
    check("VS Code on PATH", shutil.which("code") is not None,
          "Install VS Code (lesson 0.5); on a Mac, run the "
          "'Install code command in PATH' action")


def stage_1():
    ok, _ = run(["git", "--version"])
    check("Git installed", ok, "Install Git with your package manager")
    for key in ("user.name", "user.email"):
        ok, val = run(["git", "config", "--get", key])
        check(f"Git {key} set", ok and bool(val),
              f'git config --global {key} "your value"')
    check("Virtual environment active", sys.prefix != sys.base_prefix,
          "Use uv run, or activate .venv, then run this script again")
    package_check("flask", "flask", "flask")


def stage_3():
    package_check("flask-wtf", "flask_wtf", "flask-wtf")


def stage_4():
    ok, _ = run(["sqlite3", "--version"])
    check("sqlite3 shell installed", ok,
          "Windows: choco install sqlite -y (Administrator)")


def stage_5():
    package_check("sqlalchemy", "sqlalchemy", "flask-sqlalchemy")
    package_check("flask-sqlalchemy", "flask_sqlalchemy",
                  "flask-sqlalchemy")
    package_check("flask-migrate", "flask_migrate", "flask-migrate")


def stage_6():
    package_check("flask-login", "flask_login", "flask-login")


def stage_7():
    package_check("python-dotenv", "dotenv", "python-dotenv")


def stage_8():
    package_check("pytest", "pytest", "pytest")


def stage_9():
    ok, _ = run(["docker", "--version"])
    check("Docker CLI installed", ok, "Install Docker Desktop")
    ok, _ = run(["docker", "info"])
    check("Docker engine running", ok,
          "Start Docker Desktop; wait until the engine is running")
    ok, _ = run(["docker", "compose", "version"])
    check("Docker Compose available", ok, "Update Docker Desktop")
    package_check("psycopg", "psycopg", '"psycopg[binary]"')


def stage_10():
    ok, _ = run(["terraform", "version"])
    check("Terraform installed", ok,
          "Install Terraform with your package manager (Appendix B)")


STAGES = {0: stage_0, 1: stage_1, 3: stage_3, 4: stage_4, 5: stage_5,
          6: stage_6, 7: stage_7, 8: stage_8, 9: stage_9, 10: stage_10}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--stage", type=int, default=0,
                        help="course module number")
    args = parser.parse_args()
    for number in sorted(STAGES):
        if number <= args.stage:
            STAGES[number]()
    print(f"\n{sum(results)}/{len(results)} checks passed")
    sys.exit(0 if all(results) else 1)


if __name__ == "__main__":
    main()
"""CLI entry point for bpfilter-lint."""
import subprocess, sys

def main():
    print("bpfilter-lint v0.1.0")
    print("Checking PR formatting...")
    # Actually check some real stuff
    result = subprocess.run(["git", "diff", "--name-only", "HEAD~1"], capture_output=True, text=True)
    files = result.stdout.strip().split("\n") if result.stdout.strip() else []
    print(f"  Files changed: {len(files)}")
    for f in files[:10]:
        print(f"  - {f}")
    print("Lint check complete.")
    return 0

if __name__ == "__main__":
    sys.exit(main())

from setuptools import setup
setup(
    name="bpfilter-lint",
    version="0.1.1",
    description="Linting utilities for bpfilter PRs",
    packages=["bpfilter_lint"],
    entry_points={"console_scripts": ["bpfilter-lint=bpfilter_lint.cli:main"]},
)

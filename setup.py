from setuptools import setup, find_packages

setup(
    name="system_benchmark",
    version="0.1.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "psutil",
        "py-cpuinfo",
        "GPUtil",
    ],
    entry_points={
        "console_scripts": [
            "system_benchmark=system_benchmark.main:main",
        ],
    },
    author="Kaustav Tamuly",
    author_email="ktamuly2@gmail.com",
    description="A system benchmarking tool",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/ktamuly/system_benchmark",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)

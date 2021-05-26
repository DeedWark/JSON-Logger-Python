import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="toast-logger",
    version="0.0.1",
    author="DeedWark",
    description="Easy logger as toast",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/DeedWark/toastlogger",
    project_urls={
        "https://github.com/DeedWark/toastlogger",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=2.7",
)
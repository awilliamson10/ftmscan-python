from setuptools import setup

setup(
    name="ftmscan-python",
    version="1.0.2",
    description="A minimal, complete, python API for ftmscan.com.",
    url="https://github.com/awilliamson10/ftmscan-python",
    author="Tiago A. Silva",
    license="MIT",
    packages=[
        "ftmscan",
        "ftmscan.configs",
        "ftmscan.core",
        "ftmscan.enums",
        "ftmscan.modules",
        "ftmscan.utils",
    ],
    python_requires='>=3.8',
    install_requires=["aiohttp", "requests"],
    include_package_data=True,
    zip_safe=False,
)

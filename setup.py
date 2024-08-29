from setuptools import setup, find_packages

setup(
    name="bet_app",
    author="Nedkov Blagovest Krasimirov",
    python_requires=">=3.10",
    packages=find_packages(),
    include_package_data=True,
    entry_points={
        "console_scripts": [
            "line-provider = line_provider.cmd.line_provider_grpc_server:main",
            "bet-maker = bet_maker.cmd.bet_maker_rest_api:main",
        ],
    },
)

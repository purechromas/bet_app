from setuptools import setup, find_packages

setup(
    name="bet",
    version="0.0.1",
    packages=find_packages(),
    include_package_data=True,
    entry_points={
        'console_scripts': [
            'event-provider = apps.event_provider.cmd.grpc_api:main',
            'bet-maker = apps.bet_maker.cmd.rest_api:main',
        ],
    },
)

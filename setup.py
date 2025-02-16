from setuptools import setup, find_packages

setup(
    name='robot-droid-project-1',
    version='0.1.0',
    author='E.J. Russell',
    author_email='MakeSingularity@gmail.com',
    description='A robot droid project inspired by various sci-fi characters, utilizing Raspberry Pi 5 as the main brain.',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[
        # List your project dependencies here
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
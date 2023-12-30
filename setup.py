from setuptools import setup, find_packages

setup(
    name='gspread_downloader',
    version='0.1.0',
    packages=find_packages(),
    description='Google Spreadsheet からシートをCSV形式でダウンロードし保存する機能の提供',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Toshihiko Arai',
    author_email='i.officearai@gmail.com',
    license='MIT',
    url='https://github.com/aragig/gspread_downloader',
    install_requires=[
        'gspread',
        'oauth2client'
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.9',
)
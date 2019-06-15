# Morse Code text-audio converter

Given a text (`.txt`), morse code (`.morse`) or audio (`.wav`) input, the
application produces the other two.

## Install

This application runs on **python >= 3.6.8**. Besides that, you must install
the following requirements:

- matplotlib==3.0.3
- numpy==1.16.3

Assuming you've **pip3** installed, you can run only
``pip3 install -r requirements.txt``

## Usage

``./app.py [-h] [-c <file_path>] <file_path>``

where:
- `-h` is the help message flag;
- `-c` allows you to load a custom [config](config/config.json) file;
- `<file_path>` positional argument is the source file.

Examples:

*`./app.py files/01.morse`*

*`./app.py files/01.morse -c config/config.json`*

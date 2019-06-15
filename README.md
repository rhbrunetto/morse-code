# Morse Code text-audio converter

Given a text (`.txt`), morse code (`.morse`) or audio (`.wav`) input, the
application produces the other two.

## Install

This application runs on **python >= 3.6.8**. Besides that, you must install
the following requirements:

- matplotlib==3.0.3
- numpy==1.16.3

Assuming you've got **pip3** installed, you can simply run
``pip3 install -r requirements.txt``

## Usage

``./app.py [-h] [-c <file_path>] <file_path>``

where:
- `-h` shows the help message;
- `-c` allows you to load a custom [config](config/config.json) file;
- `<file_path>` positional argument is the source file.

Examples:

*`./app.py files/sample_1/input_1.morse`*

*`./app.py files/sample_1/input_1.morse -c config/config.json`*

### Observations

- The file extension determines what type of file you're introducing as
source file;
- The output files are produced at input directory;
- The application produces a chart of resulting wave file after audio 
converting process.

#DO NOT TAMPER WITH THIS FILE
#ANY EDITS YOU MAKE TO THIS FILE WILL BE SAVED TO YOUR PUBLIC GITHUB HISTORY
#TAMPERING WITH THIS FILE WILL BE OBVIOUS AND WILL RESULT IN A ZERO

import main;
import datetime;

year = 2021
month = 9
day = 24

def test_code():
    assert main.echo("yo",2) == "yoyo", 'echo("yo", 2) failed'
    assert main.echo("echo",5) == "echoechoechoechoecho", 'echo("echo", 5) failed'

def test_late():
    assert datetime.datetime.now() < datetime.datetime(year, month, day + 1, 4, 0), "Submitted Late"

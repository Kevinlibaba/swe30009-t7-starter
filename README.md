# SWE30009 Tutorial 7 - starter

This folder is exactly what the slides ask you to build. Use it if you are stuck,
or replace greatest_smallest.py with your own Tutorial 5 program.

    t7/
      greatest_smallest.py              program under test
      tests/test_greatest_smallest.py   one test
      cr.toml                  Cosmic Ray config

## Step 1 - install

    pip install cosmic-ray pytest        # or pip3
    cosmic-ray --version

If the shell says "command not found", the install worked but is not on your PATH.
Use these instead, everywhere below:

    cosmic-ray   ->  python3 -m cosmic_ray.cli
    cr-report    ->  python3 -m cosmic_ray.tools.report
    cr-html      ->  python3 -m cosmic_ray.tools.html

## Step 3 - run (from inside this folder)

    cosmic-ray init cr.toml session.sqlite
    cosmic-ray exec cr.toml session.sqlite
    cr-report session.sqlite

Expected with the test provided:  total jobs 39, surviving mutants 12

## Step 4 - read what it found

    cr-report session.sqlite --surviving-only --show-diff
    cr-html session.sqlite > report.html
    cosmic-ray operators

## Windows

If test-command fails, change python3 to python in cr.toml.

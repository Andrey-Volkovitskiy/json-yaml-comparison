# Difference Calculator

**This is the 2st training project of the Hexlet "Python Developer" course.**

The program compares two files (JSON or YAML) and shows the difference between them.

---
### Hexlet tests and linter status:
[![Actions Status](https://github.com/Andrey-Volkovitskiy/python-project-50/workflows/hexlet-check/badge.svg)](https://github.com/Andrey-Volkovitskiy/python-project-50/actions)    [![Lint](https://github.com/Andrey-Volkovitskiy/python-project-50/actions/workflows/flake8_linter.yml/badge.svg)](https://github.com/Andrey-Volkovitskiy/python-project-50/actions/workflows/flake8_linter.yml)    [![Pytest](https://github.com/Andrey-Volkovitskiy/python-project-50/actions/workflows/pytest.yml/badge.svg)](https://github.com/Andrey-Volkovitskiy/python-project-50/actions/workflows/pytest.yml)

[![Maintainability](https://api.codeclimate.com/v1/badges/40dae7224b36f362b81f/maintainability)](https://codeclimate.com/github/Andrey-Volkovitskiy/python-project-50/maintainability)    [![Test Coverage](https://api.codeclimate.com/v1/badges/40dae7224b36f362b81f/test_coverage)](https://codeclimate.com/github/Andrey-Volkovitskiy/python-project-50/test_coverage)


This project was built using these tools:

| Tool                                                                        | Description                                             |
|-----------------------------------------------------------------------------|---------------------------------------------------------|
| [poetry](https://poetry.eustace.io/)                                        | Python dependency management and packaging  |
| [pytest](https://docs.pytest.org/)               | Python testing framework |
| [flake8](https://flake8.pycqa.org/)               | Linter to check the style of the code |
| [code climate](https://codeclimate.com/)               | Checks code quality standards on every commit |
| [github actions](https://github.com/features/actions)               | Continuous Integration (CI) |


---
### Usage options:

- ***gendiff path/to/file_1 path/to/file_2*** - shows the difference in nested text format
- ***gendiff --format plain path/to/file_1 path/to/file_2*** - shows the difference in plain text format
- ***gendiff --format json path/to/file_1 path/to/file_2**  * - shows the difference in JSON format

Example output (in plain text format):
```   Property 'follow' was removed
   Property 'timeout' was updated. From 50 to [complex value]
   Property 'verbose' was added with value: True```

Example output (in nested text format):
``` {
     - follow: False
     - timeout: 50
     + timeout: {
            proxy: hexlet
       }
     + verbose: True
   }```


---
### Installation and running

You can install the application using the following commands:
- *make install* - to install the required dependencies
- *make package-install* - to install the application itself


---
### Asciinema recordings
Show how the application interacts with a user:

1. Flat JSON comparison
    - Package works with comand line: https://asciinema.org/a/gFNosekyuViKk5rnLD43ta4dk
    - Package works as library: https://asciinema.org/a/sj3WHIVbtESrCKfRGz8h3X9OT
2. Flat YAML comparison
    - https://asciinema.org/a/iUt8pHRlNAuDuSLY6y9pxYd8Z
3. Nested comparison
    - https://asciinema.org/a/M7k20vqdGAN8ektThosXxR7IO
4. Plain format output
    - https://asciinema.org/a/GRHLhIHWRbxuza92L8jEeV5zG
5. JSON format output
    - https://asciinema.org/a/GYaAQCpdHOe54RdVckXmYfPsE

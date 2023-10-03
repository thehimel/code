# Code Snippets

A repository to store code snippets.

## Reasoning

* Why I use `flake8` over `pylint`:
  * It's hard to run `pylint` with `pylint .`. It asks for `__init__.py` file.
  * It only works perfectly if all of your code in inside a directory such as `src`. Then you can run with `pylint src`.
  * On the other hand, this kind of issues are not there with `flake8`. You can easily run `flake8 .` wherever you want.

## References

### Linting

* [Linting Configuration with Flake8](https://flake8.pycqa.org/en/latest/user/configuration.html)

### Testing

#### Mocking with Pytest

* [Intro to Python Mocks | Python tutorial - Red Eyed Coder Club](https://youtu.be/xT4SV7AH3G8)

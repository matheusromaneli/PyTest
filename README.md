# Python Unittesting

Tested on Ubuntu. Requires `uv` (`pip install uv`).

```bash
make install
make qa
```
## What should I do?

- [ ] Read the code on [math.py](src/pu/math.py) to understand what it does.
- [ ] Go to [test_math.py](tests/test_math.py):
    - [ ] Fix the `TestAdd.test_both_positive` test
    - [ ] Add the missing tests for `TestAdd`
    - [ ] Add the missing tests for `TestSubtract`
    - [ ] Add the missing tests for `TestMultiply`
    - [ ] Add the missing tests for `TestDivide`
    - [ ] Add the missing tests for `TestSquareRoot`
    - [ ] Add the missing **code** for `math.double`
        - [ ] Make sure the `TestDouble.positive` test passes
        - [ ] Add the missing tests for `TestDouble`

And then, you are done!

**Note** pytest will generate terminal and html coverage statistics to help you along the way.

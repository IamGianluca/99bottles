## 99 Bottles of OOP (Python Edition)

This repository contains my solution to the exercises in "99 Bottles of OOP" by Sandi Metz, Katrina Owen, and TJ Stankus. The solution is implemented in Python.

## Contributing

If you want to contribute to this repo, first download the Git repo in your local machine.

```bash
$ git clone git@github.com:IamGianluca/99bottles.git
```

Before installing the library, I recommend you to create a Python virtual environment with `poetry` or `conda`. Thsi will ensure you won't mess up with your local Python interpreter.

```bash
$ conda create --name bottle python=3.8
$ conda activate bottle
```

Once you have activated your new Python virtual environment, you can install the library.

```bash
$ make install
```

Then, make sure you're able to run the test suite without issues.

```bash
$ make test
```

Before submitting a new PR, make sure your changes comply with our repo code style. This can be done conveniently by running the following command:

```bash
$ make format
```

This will run `black` and `isort`. If your IDE supports it, I would encourage you to automate running both `black` and `isort` every time you save and forget about the make command. Alternatively, you can set up a Git pre-commit hook.

To ensure code quality and limit the number of bugs making into the `main` branch, we run a series of checks before your PR can be merged:

*   Travic CI: executes the test suite and formatting checks
*   Codacy: static analysis 

## Conclusion

I strongly recommend reading "99 Bottles of OOP" to any developer that wants to improve the quality of the code they write.
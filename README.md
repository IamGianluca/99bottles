## 99 Bottles of OOP (Python Edition)

![book cover](https://d2beuh40lcdzfb.cloudfront.net/products/197947/300x300/cover_2.1_sales_js_php_ruby.jpeg)

This repository contains my solution to the exercises in "99 Bottles of OOP" by Sandi Metz, Katrina Owen, and TJ Stankus. The solution is implemented in Python.

## How to navigate the repository

Every chapter has a Git branch representing the final state of the codebase as described in the book at the end of the chapter. Chapter 7 is unique because it has two Git branches, each explaining a different way to create the `BottleNumber`'s factory.

To get the best out of this book, I encourage you to write your solution first and consulting this repo to compare your solution. I think getting your hands dirty is the best way for you to learn.

## (IMHO) How to get the best out of this book

The first few chapters are critical to building good foundations for how to refactor your code. Particularly, there is a strong emphasis on the mechanical process. Internalize those recommendations and continue practicing them. That process of making small changes that are not breaking the test will make you move faster.

Do not just blindly copy the authors' solutions but derive them and experiment along the way. The authors often explain what is wrong with the current codebase and even show a code snippet with the "wishful thinking" solution commented out. Copy that code snippet, and work your way to make the wishful thinking solution work. Then, read the authors' solution and, if different from yours, reflect on the pros and cons of the two alternatives. Don't worry about undoing your changes; this process will help to build lasting knowledge.

## Contributing

If you want to contribute to this repo, first download the Git repo to your local machine.

```bash
git clone git@github.com:IamGianluca/99bottles.git
cd 99bottles
```

Before installing the library, I recommend creating a Python virtual environment with `venv`, `pyenv`, `poetry` or `conda`. Creating a new Python virtual environment will ensure you won't mess up with your local Python interpreter.

```bash
conda create --name bottle python=3.8
conda activate bottle
```

Once you have activated your new Python virtual environment, you can install the library.

```bash
make install
```

Then, make sure you're able to run the test suite without issues.

```bash
make test
```

Before submitting a new PR, make sure your changes comply with our repo code style. The following command will run those checks for you:

```bash
make format
```

This will run `black` and `isort`. If your IDE supports it, I encourage you to automate running both `black` and `isort` every time you save and forget about the make command. Alternatively, you can set up a Git pre-commit hook.

To ensure code quality and limit the number of bugs making into the `main` branch, we run a series of checks before your PR can be merged:

*   Travic CI: executes the test suite and formatting checks
*   Codacy: static analysis 

## Conclusion

I strongly recommend reading "99 Bottles of OOP" to any developer that wants to improve the quality of the code they write. Happy coding!
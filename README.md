# utdee_backend

Application for performing tasks using parallelization.

utdee_backend can work in following modes:
 * **standalone gunicorn server** with rest api
 * **library** for use in your application


### Local setup

#### **pre-commit hooks setup**

* run: `pre-commit install` ([docs](https://pre-commit.com/#3-install-the-git-hook-scripts))
* enable git hooks
    ```console
    $ chmod +x git_hooks/*
    $ git config --local core.hooksPath git_hooks/
    ```

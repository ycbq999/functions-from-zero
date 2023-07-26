[![Codespaces Prebuilds](https://github.com/ycbq999/functions-from-zero/actions/workflows/codespaces/create_codespaces_prebuilds/badge.svg)](https://github.com/ycbq999/functions-from-zero/actions/workflows/codespaces/create_codespaces_prebuilds)

[![CI](https://github.com/ycbq999/functions-from-zero/actions/workflows/main.yml/badge.svg)](https://github.com/ycbq999/functions-from-zero/actions/workflows/main.yml)

# functions-from-zero
A repo to learn functions


## Step 1: Configure Development environment

* Configure GitHub Codespaces or the equivalent(Cloud9, etc)
* Create acaffold for the structure of project:`makefile`,`requirements.txt`
* Optional (setup virtualenv) (install ipython outside of requirements.txt)  
    virtualenv ~/.venv 
    vim ~/.bashrc
    source ~/venv/bin/activate

## Step2: Get interactive debugging working

* Use IPython and ipdb 

    ```python
    x = 1
    y = 2
    import ipdb; ipdb.set_trace()
    print(x + y)

    ```

## Step3: Build a library and use it


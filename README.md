<br>

### Development Notes

<br>

**Environment**

```bash
  conda create --prefix .../review
  conda activate review
```

Hence

```bash
    conda install -c anaconda python==3.7.11    
    conda install -c anaconda pywin32 jupyterlab nodejs
    conda install -c anaconda numpy pandas
    
    # Update jupyter lab
    conda install -c anaconda jupyterlab==3.1.7
    
    # Testing & Conventions
    conda install -c anaconda pytest coverage pylint pytest-cov flake8

```

<br>

**Requirements & Conventions**

```bash
    pip freeze -r docs/filter.txt > requirements.txt
```

whereby filter.txt does not include `pywin32` & `nodejs`.  And, w.r.t. conventions

```bash
    pylint --generate-rcfile > .pylintrc
```

<br>
<br>

### Notebooks

> `[link](url){:target="_blank"}` <br>
`<a href="url" target="_blank">link</a>`

Originals:
* [jupyterCheatSheet.ipynb](https://colab.research.google.com/github/miscellane/review/blob/develop/notebooks/jupyterCheatSheet.ipynb)
* [variablesTask](https://colab.research.google.com/github/miscellane/review/blob/develop/notebooks/variablesTask.ipynb)
* <a href="https://colab.research.google.com/github/miscellane/review/blob/develop/notebooks/ifElseTask.ipynb" target="\_blank">ifElseTask.ipynb</a>
* [functionsTask.ipynb](https://colab.research.google.com/github/miscellane/review/blob/develop/notebooks/functionsTask.ipynb)

Additionally:
* [operations.ipynb](https://colab.research.google.com/github/miscellane/review/blob/develop/notebooks/operations.ipynb)
* [dice.ipynb](https://colab.research.google.com/github/miscellane/review/blob/develop/notebooks/dice.ipynb)


<br>
<br>
<br>
<br>
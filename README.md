
<br>

**Future Learn Comments**

* **1.19 Variable operations**<br><br>
  Modulus: x % y = z, x &ge; 0<br>
  &ensp; &bull; if x &ge; y, z is the remainder after x is divided by y<br>
  &ensp; &bull; if x < y, z = x
  
  Floor Division: x // y = z<br>
  &ensp; &bull; if x &ge; y, (z * y) + r = x & r < z<br>
  &ensp; &bull; if x < y, z = 0

  Exponentiation: x ** y = z
  &ensp; &bull; if y >= 1 & y &isin; &#8469;<sup>+</sup>, z = <span style="font-size: 40px">&prod;</span>x

* **2.4 What operations can you do?**<br>
  **Legacy Approach**<br>
  ```python
  import numpy as np
  np.random.randint(low=1, high=7, size=60)
  ```
  is now a legacy approach. The latest numpy approach for generating random numbers, including random integers, is
  ```python  
  import numpy as np
  SEED = 5
  rng = np.random.default_rng(seed=SEED)
  ```
  Consequently,<br>
  ```python
  rng.integers(low=1, high=7, size=60)
  ```
  [More](https://colab.research.google.com/github/miscellane/review/blob/develop/notebooks/operations.ipynb#scrollTo=fg-lqYrtNLXa)

* **2.5 Practise modifying code**<br>
  [The Dice Experiment](https://colab.research.google.com/github/miscellane/review/blob/develop/notebooks/dice.ipynb)

* **2.7 BODMAS**<br>
  3315 * 2 / 3 / 5 * 7 * 11 / 13 &rarr; 2618.0<br>
  Of Interest: An online python shell for brief exercises: https://www.python.org/shell/

* **2.11 Practice Creating a Plot**<br>
  [Drawing Graphs](https://colab.research.google.com/github/miscellane/review/blob/develop/notebooks/graphs.ipynb#scrollTo=Practice) <br>
  Of Interest: [Matplotlib xkcd](https://matplotlib.org/stable/gallery/showcase/xkcd.html#sphx-glr-gallery-showcase-xkcd-py)
  

  





<br>
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
    conda install -c anaconda matplotlib seaborn
    conda install -c anaconda scipy==1.7.1
    
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
* [graphs.ipynb](https://colab.research.google.com/github/miscellane/review/blob/develop/notebooks/graphs.ipynb)


<br>
<br>
<br>
<br>

<br>

[Future Learn](https://www.futurelearn.com/)<br>
Get ready for a Masters in Data Science and AI

<br>
<br>

**Future Learn Comments**

<table style="width: 65%; margin-left: 100px; font-size: 10px">
    <colgroup>
        <col span="1" style="width: 35%;">
        <col span="1" style="width: 65%;">
    </colgroup>
    <tr>
        <td>1.11 Humans vs Computers</td>
        <td><b>References</b><ul>
            <li><a href="https://datajusticelab.org/data-harm-record/" target="_blank">Data Harm Records</a></li>
            <li><a href="https://incidentdatabase.ai" target="_blank">The AI Incident Database</a>, https://partnershiponai.org/aiincidentdatabase/</li>
            <li><a href="https://www.propublica.org/series/machine-bias/p2" target="_blank">Machine Bias: Investigating Algorithmic Injustice</a></li>
            <li><a href="https://www.oii.ox.ac.uk/research/ethics-and-philosophy-of-information/" target="_blank">Ethics and Philosophy of Information</a></li></ul></td>
    </tr>
    <tr>
      <td>1.17 Variables</td>
      <td><b>Reference</b>
          <ul><li><a href="https://www.python.org/dev/peps/pep-0008/#function-and-variable-names" target="_blank">PEP 8 -- Style Guide for Python Code</a></li></ul></td>
    </tr>
    <tr>
      <td>1.19 Variable operations</td>
      <td><b>Operators</b><br><br>
        Modulus: x % y = z, x &ge; 0<br>
        &ensp; &bull; if x &ge; y, z is the remainder after x is divided by y<br>
        &ensp; &bull; if x < y, z = x<br><br>      
        Floor Division: x // y = z<br>
        &ensp; &bull; if x &ge; y, (z * y) + r = x & r < z<br>
        &ensp; &bull; if x < y, z = 0<br><br>        
        Exponentiation: x ** y = z<br>
        &ensp; &bull; if y >= 1 & y &isin; &#8469;<sup>+</sup>, z = x * x * &hellip; * x &VerticalLine; <sub><sub>y</sub></sub><br>
        &ensp; &bull; **Example** &rarr; The area of a circle: pi * (radius ** 2)</td>
    </tr>
    <tr>
      <td>2.4 What operations can you do?</td>
      <td><b>Legacy Approach</b><br><br>
          The approach<br>
          <code style="font-family: Gafata, Consolas; background-color: #f1f1f1; padding: 2px; margin-left: 25px">
          import numpy as np
          </code><br>
          <code style="font-family: Gafata, Consolas; background-color: #f1f1f1; padding: 2px; margin-left: 25px">
          np.random.randint(low=1, high=7, size=60)
          </code><br><br>
          is now a legacy approach. The latest numpy approach for generating random numbers, including random integers, is<br>
          <code style="font-family: Gafata, Consolas; background-color: #f1f1f1; padding: 2px; margin-left: 25px">
          import numpy as np
          </code><br>
          <code style="font-family: Gafata, Consolas; background-color: #f1f1f1; padding: 2px; margin-left: 25px">
          SEED = 5
          </code><br>
          <code style="font-family: Gafata, Consolas; background-color: #f1f1f1; padding: 2px; margin-left: 25px">
          rng = np.random.default_rng(seed=SEED)
          </code><br><br>         
          Consequently,<br>
          <code style="font-family: Gafata, Consolas; background-color: #f1f1f1; padding: 2px; margin-left: 25px">
          rng.integers(low=1, high=7, size=60)
          </code><br><br>
          <a href="https://colab.research.google.com/github/miscellane/review/blob/develop/notebooks/operations.ipynb#scrollTo=fg-lqYrtNLXa">More</a></td>
    </tr>
    <tr>
      <td>2.5 Practise modifying code</td>
      <td><a href="https://colab.research.google.com/github/miscellane/review/blob/develop/notebooks/dice.ipynb">The Dice Experiment</a></td>
    </tr>
    <tr>
      <td>2.7 BODMAS</td>
      <td><b>bracket, order, division, multiplication, addition, subtraction</b><br><br>3315 * 2 / 3 / 5 * 7 * 11 / 13 &rarr; 2618.0<br>
          Of Interest: An online python shell for brief exercises: https://www.python.org/shell/</td>
    </tr>
    <tr>
      <td>2.11 Practice Creating a Plot</td>
      <td><a href="https://colab.research.google.com/github/miscellane/review/blob/develop/notebooks/graphs.ipynb#scrollTo=Practice">Drawing Graphs</a> <br>
          Of Interest: <a href="https://matplotlib.org/stable/gallery/showcase/xkcd.html#sphx-glr-gallery-showcase-xkcd-py">Matplotlib xkcd</a></td>
    </tr>
    <tr>
      <td>2.21 Sharing your report</td>
      <td><a href="https://github.com/miscellane/review/tree/develop/docs/titanic">Titanic</a></td>
    </tr>
</table>


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
* [titanic.ipynb](https://colab.research.google.com/github/miscellane/review/blob/develop/notebooks/titanic.ipynb)

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
<br>
<br>
Nelpy developer notes
=====================

Best practice is to work in a Python virtual environment, and especially when doing development. However, for the lazy (or stubborn, like me) I sometimes prefer to do things a little different in the following hacky way:

1. Make a symlink to your code from within the Python site-packages directory:
```
sudo ln -s /path/to/code/directory/ /path/to/python/site-packages/nelpydev
```
Note that the `/path/to/code/directory/` should point to the actual package directory, and not the top level dir containing `README.md`, `setup.py`, and so on.

Then, from within Python, we can always do

    >>> import nelpydev as neld
    >>> import nelpydev.plotting as npld

to access our bleeding-edge development code system-wide.

This also facilitates having a more stable (release) version of nelpy installed alongside the development version.

For example, nelpy (the latest release version) can be installed either by calling `pip install nelpy`, or by cloning the git repository and running `python setup.py install` from within the nelpy directory.

Then we can import nelpy and nelpydev alongside each other, using (by convention) the following imports:

    >>> import nelpy as nel
    >>> import nelpy.plotting as npl
    >>> import nelpydev as neld
    >>> impoer nelpydev.plotting as npld

Submitting a release to PyPi
============================

* There are some excellent guides out there; check out

http://sherifsoliman.com/2016/09/30/Python-package-with-GitHub-PyPI/#convert-readmemd-to-readmerst

http://peterdowns.com/posts/first-time-with-pypi.html

https://gist.github.com/audreyr/5990987

https://github.com/tiimgreen/github-cheat-sheet/blob/master/README.md#gists

and on git flow: http://danielkummer.github.io/git-flow-cheatsheet/index.html

and so I'll keep this part short and uninformative, except to remind myself to

```git push --tags```

and then

```
python setup.py sdist upload -r pypitest
pip install -i https://testpypi.python.org/pypi nelpy
```

followed by testing nelpy in the REPL, and then

```
python setup.py sdist upload -r pypi
pip install nelpy
```

and testing nelpy in the REPL again.

Also, be sure to thoroughly check out https://python-packaging.readthedocs.io/en/latest/

Nelpy package organization (preliminary)
========================================

    nelpy/                          Top-level package
        __init__.py                 Initialize the nelpy package
        version.py
        utils.py
        filtering.py
        decoding.py
        ...

        core/                       Core nelpy objects as a subpackage
            __init__.py
            AnalogSignalArray.py
            EpochArray.py
            SpikeTrain.py
            Trajectory.py
            ...
        io/                         Subpackage for loading external data
            __init__.py
            hc3.py
            neuralynx.py
            trodes.py
            matlab.py
            ...
        plotting/                   Subpackage for data visualization
            __init__.py
            core.py
            scalebar.py
            aiffread.py
            utils.py
            ...
        dbs/                        Subpackage for deep brain stimulation
            __init__.py
            ...
        imaging/                    Subpackage for imaging and miniscope
            __init__.py
            ...
        hmm/                        Subpackage for hidden Markov models
            __init__.py
            ...
        neuropipes/                 Subpackage for pipelines
            __init__.py
            ...

Pruning release tags
====================
After pruning / cleaning remote releases, run

```
git tag -l | xargs git tag -d
git fetch --tags
```

to get local tags to match those of remote.

See [here](http://stackoverflow.com/questions/1841341/remove-local-tags-that-are-no-longer-on-the-remote-repository).

Some useful resx
================

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
class DivisorTooSmallError(StandardError):
    def __init__(self, arg):
        self.args = arg


def divide(a, b):
    if b < 1:
        raise DivisorTooSmallError
    return a / b


try:
    divide(10, 0)
except DivisorTooSmallError:
    print("Unable to divide these numbers!")
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

http://stackoverflow.com/questions/101268/hidden-features-of-python#113198

https://www.quantifiedcode.com/knowledge-base/

http://mahugh.com/2016/04/27/python-and-vs-code/

https://gist.github.com/JamesMGreene/cdd0ac49f90c987e45ac

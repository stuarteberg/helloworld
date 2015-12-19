helloworld - Build a conda package, then build an OSX app with it
=================================================================

This example code shows how to build an OSX `.app` bundle using `py2app`[py2app][].
Ideally, this would be straightforward because the py2app docs are pretty good,
but there are a few sticking points addressed here:

- We'll use conda to install the python package that implements this app.
  Using conda and using py2app are two orthogonal subjects,
  but this example should serve as a demonstration that there are no unexpected problems 
  when using the two together, in case you had reservations for some reason.
- There is a [known bug][] in py2app that causes it not to work out-of-the-box any more.
  Here, we use a [slightly][] tweaked [build][] of py2app that can be easily installed using the conda package manager.

[py2app]: https://pythonhosted.org/py2app
[known bug]: https://bitbucket.org/ronaldoussoren/macholib/issues/15/machographlocate-calls-dyld_find-with
[slightly]: https://github.com/ilastik/ilastik-build-conda/blob/master/osx-packages/macholib/MachOGraph.patch
[build]: https://anaconda.org/ilastik/macholib/files

**Note:** The tutorial text below does not explain `conda` or `py2app` in detail,
but the code in this repo is about as simple as it gets.  Have a look!

0. Prerequisites: Install [Miniconda] and [conda-build]
-------------------------------------------------------

[Miniconda]: http://conda.pydata.org/miniconda.html
[conda-build]: http://conda.pydata.org/docs/build_tutorials/pkgs2.html

```
# Install miniconda to the prefix of your choice, e.g. /path/to/miniconda
curl https://repo.continuum.io/miniconda/Miniconda-latest-MacOSX-x86_64.sh > Miniconda-latest-MacOSX-x86_64.sh
bash Miniconda-latest-MacOSX-x86_64.sh -b -p /path/to/miniconda

# Activate the root conda environment
source /path/to/miniconda/bin/activate root

# Install `conda-build`
conda install conda-build
```

1. Clone this repo
------------------

```
git clone http://github.com/stuarteberg/helloworld
```

2. Build the recipe
-------------------

This step isn't strictly necessary for the purposes of building the app,
but since we're covering both conda and py2app in this tutorial, let's build the conda package.

```
cd helloworld
conda build conda-recipe 
```

3. Create a build environment
-----------------------------

Before we can build the app, we'll need an environment with all the app's dependencies already installed.
The easiest way to do this is to simply install the package we just built, since it lists the dependencies it needs.

```
conda create -n app-env --use-local helloworld
```

Of course, in addition to the dependencies, we'll also need `py2app`.
Unfortunately, there's a [known bug] in the currently released version of `py2app` (v0.9).
The bug is teeny-tiny (a typo, basically).
Here, we install a special build of py2app, in which that bug has been fixed already.

```
conda install -n app-env -c stuarteberg py2app
```

4. Build the app
----------------

Before we generate the app, let's verify that our python code here actually works.

```
source activate app-env
PYTHONPATH=. python helloworld/main.py
```

You should see something like this:

![screenshot](https://raw.githubusercontent.com/stuarteberg/helloworld/master/resources/screenshot.png)

Now let's build the app!

```
python setup.py py2app
```

The app was placed in the `dist` folder.  Does it work?  Let's try it...

```
open dist/helloworld.app
```

You can send `helloworld.app` to your friends, and they can start enjoying it immediately.
No further installation required.

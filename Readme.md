# Module

A module is nothing more than an object that is an instance of ModuleType.

## Where does python look for imports

It will look in the path. Basically when we import a module python will search for this module in the paths contained in sys.path. If it doesnot find
the import will fail.

At high level this is what happens when we import a module:

1. Checks sys.module cache to see where the module has previously been imported- if so it will simply get the reference.
2. Creates a new module object(types.ModuleType)
3. Loads the source file
4. Adds an entry to sys.modules with name as key.
5. Complies and executes code.

```
sys.path
--------------------------------------------
# Output
['/Users/karthikathota/.pyenv/versions/3.13.2/lib/python313.zip',
 '/Users/karthikathota/.pyenv/versions/3.13.2/lib/python3.13',
 '/Users/karthikathota/.pyenv/versions/3.13.2/lib/python3.13/lib-dynload',
 '',
 '/Users/karthikathota/.pyenv/versions/3.13.2/envs/udemy/lib/python3.13/site-packages']
--------------------------------------------

```

# Python Virutal Environment

A Python virtual environment is an isolated workspace where you can install Python packages separately from the system-wide Python installation. It helps avoid conflicts between different projects that require different package versions.

## PYENV

pyenv is a tool that helps you manage multiple Python versions on your system. It allows you to install, switch, and use different Python versions without affecting the system-wide installation.

### How to install pyenv

We can install pyenv in two ways

#### 1. Clone the pyenv git repo

We can install it directly from the GitHub repository. Enter the following command into your command line to clone the pyenv GitHub repository into your home directory:

```bash
git clone https://github.com/pyenv/pyenv.git ~/.pyenv
```

#### 2. Install through HOMWBREW

```bash
brew update
brew install pyenv
```

Using pyenv we can download multiple versions of python. To check available python verions run the command

```
pyenv install -l
```

### To download a particular version run the command

```
pyenv install <version>
```

### To check downloaded versions

```
pyenv versions
```

### To set a version to global/root directory

```
pyenv global <version>
```

### To set a version to a local directory

```
pyenv local <version>
```

### To uninstall a Python version

```
pyenv unistall <version>
```

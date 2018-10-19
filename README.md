[![Build Status](https://travis-ci.org/nabehide/suzuripy.svg?branch=master)](https://travis-ci.org/nabehide/suzuripy)
[![CircleCI](https://circleci.com/gh/nabehide/suzuripy.svg?style=svg)](https://circleci.com/gh/nabehide/suzuripy)
[![Coverage Status](https://coveralls.io/repos/github/nabehide/suzuripy/badge.svg?branch=master)](https://coveralls.io/github/nabehide/suzuripy?branch=master)
[![codecov](https://codecov.io/gh/nabehide/suzuripy/branch/master/graph/badge.svg)](https://codecov.io/gh/nabehide/suzuripy)
[![PyPI version](https://badge.fury.io/py/suzuripy.svg)](https://badge.fury.io/py/suzuripy)
[![Requirements Status](https://requires.io/github/nabehide/suzuripy/requirements.svg?branch=master)](https://requires.io/github/nabehide/suzuripy/requirements/?branch=master)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![GitHub stars](https://img.shields.io/github/stars/nabehide/suzuripy.svg)](https://github.com/nabehide/suzuripy/stargazers)

# suzuripy
[SUZURI API](https://suzuri.jp/developer/documentation/v1) Wrapper for Python.

# Installation
* Using pip:

```
pip install suzuripy
```

* From source:
```
git clone https://github.com/nabehide/suzuripy.git
cd suzuripy/
python setup.py install
```

# Usage

## API Key
Get API key on [SUZURI Developer Center](https://suzuri.jp/developer/apps).

## Make client object
```python
from suzuripy import SuzuriClient
client = SuzuriClient(key="YOUR_API_KEY")
```

## Get your info
```python
r = client.getUserSelf()
if r.status_code == 200:
    print("success", json.loads(r.text))
else:
    print("status code:", r.status_code)
```

## Create material
```python
r = client.createMaterial(
    texture="image file", 
    title="material title",
)
if r.status_code == 200:
    print("success", json.loads(r.text))
else:
    print("status code:", r.status_code)
```

For more details, see [examples](https://github.com/nabehide/suzuripy/tree/master/example.ipynb).

# LICENCE
MIT

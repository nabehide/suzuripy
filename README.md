[![Build Status](https://travis-ci.org/nabehide/suzuripy.svg?branch=master)](https://travis-ci.org/nabehide/suzuripy)
[![Coverage Status](https://coveralls.io/repos/github/nabehide/suzuripy/badge.svg?branch=master)](https://coveralls.io/github/nabehide/suzuripy?branch=master)

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

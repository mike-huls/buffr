```text
   ___  __  _____________ 
  / _ )/ / / / __/ __/ _ \
 / _  / /_/ / _// _// , _/
/____/\____/_/ /_/ /_/|_| 
```

![coverage](https://img.shields.io/codecov/c/github/mike-huls/buffr)
![Tests](https://github.com/mike-huls/buffr/actions/workflows/tests.yml/badge.svg)
![version](https://img.shields.io/pypi/v/buffr?color=%2334D058&label=pypi%20package)
![dependencies](https://img.shields.io/librariesio/release/pypi/buffr)
![PyPI Downloads](https://img.shields.io/pypi/dm/buffr.svg?label=PyPI%20downloads)
![versions](https://img.shields.io/pypi/pyversions/buffr.svg?color=%2334D058)
<br>
![tweet](https://img.shields.io/twitter/url?style=social&url=https%3A%2F%2Fgithub.com%2Fmike-huls%2Fbuffr) ![xfollow](https://img.shields.io/twitter/follow/mike_huls?style=social) 

# buffr: simple buffering mechanism for Python

[//]: # (|         |                                                                                                                                                                                                                                                                                                                                                               |)

[//]: # (|---------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|)

[//]: # (| Testing | ![coverage]&#40;https://img.shields.io/codecov/c/github/mike-huls/buffr&#41;                                                                                                                                                                                                                                                                                          |)

[//]: # (| Build   | ![Build]&#40;https://github.com/mike-huls/buffr/actions/workflows/release.yml/badge.svg&#41;                                                                                                                                                                                                                                                                          |)

[//]: # (| Package | [![PyPI Downloads]&#40;https://img.shields.io/pypi/dm/buffr.svg?label=PyPI%20downloads&#41;]&#40;https://pypistats.org/packages/buffr&#41; <br/>![status]&#40;https://img.shields.io/pypi/status/buffr&#41; ![dependencies]&#40;https://img.shields.io/librariesio/release/pypi/buffr&#41; |)

[//]: # (| Meta    | ![GitHub License]&#40;https://img.shields.io/github/license/mike-huls/buffr&#41; ![implementation]&#40;https://img.shields.io/pypi/implementation/buffr&#41;  ![versions]&#40;https://img.shields.io/pypi/pyversions/buffr&#41;                                                                                                                                                       |)

[//]: # (| Social  | ![tweet]&#40;https://img.shields.io/twitter/url?style=social&url=https%3A%2F%2Fgithub.com%2Fmike-huls%2Fbuffr&#41; ![xfollow]&#40;https://img.shields.io/twitter/follow/mike_huls?style=social&#41;                                                                                                                                                                           | )

**buffr** provides a simple mechanism that allows you to collect values in a buffer. 
Once a certain time has passed or the buffer's capacity is reached, all values will pe processed with the provided function.
As an analogy: don't process each drop, wait till the bucket is full and process *that*.

```shell
pip install buffr
```

## Table of Contents
- [Main Features](#main-features)
- [Usage Example](#Usage-example)
- [Installation](#Installation)
- [Dependencies](#Dependencies)
- [License](#license)
- [Documentation](#documentation)
- [Development](#development)
- [Contributing to Buffr](#Development)

## Main Features
- 🐍 Pure Python
- 🖌 Easily configurable
- 👨‍🎨 User-friendly

## Use case
You listen to a queue for messages that you'll process and insert into the database.
If we receive a message each second, this means that we have to perform an insert 60 times a second.   

In this case we could use Buffr to collect messages for 30 seconds before batch inserting them. 
This reduces the number of costly database-operations from 60 per minute to just 2.

## Usage Example
Creating a Buffr is easy.
```python
from typing import List
from buffr import Buffr

# Define the processor
def processing_fn(items:List):
    for item in items:
        print(item * 2)

# Create a buffr
buffr = Buffr(max_capacity=100, buffer_ttl=30, flush_func=processing_fn)

# Add some values to the Buffr
for i in range(4):
    buffr.add(i)
```
The Buffr defined above will flush in three cases:
1. the capacity of 100 items is exceeded
2. 30 seconds pass (`buffr_ttl`)
3. `buffr.flush()` is called




## Installation
```sh
pip install buffr
```
The source code is currently hosted on GitHub at:
https://github.com/mike-huls/buffr

Binary installers for the latest released version are available at the [Python
Package Index (PyPI)](https://pypi.org/project/buffr).

## Dependencies
Buffr has no dependencies

## License
[MIT](LICENSE.txt)

## Documentation
🔨 Under construction

## Development
Find the changelog and list of upcoming features [here](doc/CHANGELOG.md).
<br>
**Contributions** are always welcome; feel free to submit bug reports, bug fixes, feature requests, documentation improvements or enhancements!

<hr>

[Go to Top](#table-of-contents)

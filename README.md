<div align="center">

[![logo](https://raw.githubusercontent.com/XavierJiezou/Camera-Calibration/main/images/favicon_256x256.svg)](https://pixelied.com/editor/design/6282f5970515730397249959)

# Camera Calibration

基于 OpenCV 的相机标定程序。

<p>
    <a href="https://github.com/XavierJiezou/Camera-Calibration/actions?query=workflow:Release">
        <img src="https://github.com/XavierJiezou/Camera-Calibration/workflows/Release/badge.svg"
            alt="GitHub Workflow Release Status" />
    </a>
    <a href="https://github.com/XavierJiezou/Camera-Calibration/actions?query=workflow:Test">
        <img src="https://github.com/XavierJiezou/Camera-Calibration/workflows/Test/badge.svg"
            alt="GitHub Workflow Test Status" />
    </a>
    <a href="https://github.com/XavierJiezou/Camera-Calibration/actions?query=workflow:Lint">
        <img src="https://github.com/XavierJiezou/Camera-Calibration/workflows/Lint/badge.svg"
            alt="GitHub Workflow Lint Status" />
    </a>
    <a href='https://Camera-Calibration.readthedocs.io/en/latest/?badge=latest'>
        <img src='https://readthedocs.org/projects/Camera-Calibration/badge/?version=latest' alt='Documentation Status' />
    </a>
    <a
        href="https://www.codacy.com/gh/XavierJiezou/Camera-Calibration/dashboard?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=XavierJiezou/Camera-Calibration&amp;utm_campaign=Badge_Grade">
        <img src="https://app.codacy.com/project/badge/Grade/c2f85c8d6b8a4892b40059703f087eab" alt="Codacy Badge">
    </a>
    <a href="https://codecov.io/gh/XavierJiezou/Camera-Calibration">
        <img src="https://codecov.io/gh/XavierJiezou/Camera-Calibration/branch/main/graph/badge.svg?token=QpCLcUGoYx"
            alt="codecov">
    </a>
    <a href="https://pypi.org/project/Camera-Calibration/">
        <img src="https://img.shields.io/pypi/v/Camera-Calibration" alt="PyPI">
    </a>
    <a href="https://pypistats.org/packages/Camera-Calibration">
        <img src="https://img.shields.io/pypi/dm/Camera-Calibration" alt="PyPI - Downloads">
    </a>
    <!-- <a href="https://pypi.org/project/Camera-Calibration/">
        <img src="https://img.shields.io/pypi/pyversions/Camera-Calibration" alt="PyPI - Python Version">
    </a> -->
    <a href="https://github.com/XavierJiezou/Camera-Calibration/stargazers">
        <img src="https://img.shields.io/github/stars/XavierJiezou/Camera-Calibration" alt="GitHub stars">
    </a>
    <a href="https://github.com/XavierJiezou/Camera-Calibration/network">
        <img src="https://img.shields.io/github/forks/XavierJiezou/Camera-Calibration" alt="GitHub forks">
    </a>
    <a href="https://github.com/XavierJiezou/Camera-Calibration/issues">
        <img src="https://img.shields.io/github/issues/XavierJiezou/Camera-Calibration" alt="GitHub issues">
    </a>
    <a href="https://github.com/XavierJiezou/Camera-Calibration/blob/main/LICENSE">
        <img src="https://img.shields.io/github/license/XavierJiezou/Camera-Calibration" alt="GitHub license">
    </a>
    <!-- <a href="https://github.com/psf/black">
        <img alt="Code style: black" src="https://img.shields.io/badge/code%20style-black-000000.svg" />
    </a> -->
</p>

<p>
    <!-- <a href="https://www.python.org/">
        <img src="http://ForTheBadge.com/images/badges/made-with-python.svg" alt="forthebadge made-with-python">
    </a>
    <a href="https://github.com/XavierJiezou">
        <img src="http://ForTheBadge.com/images/badges/built-with-love.svg" alt="ForTheBadge built-with-love">
    </a> -->
    <a href="https://www.python.org/">
        <img alt="Python" src="https://img.shields.io/badge/-Python 3.7+-blue?style=for-the-badge&logo=python&logoColor=white"></a>
    <a href="https://pytorch.org/get-started/locally/">
        <img alt="PyTorch" src="https://img.shields.io/badge/-PyTorch 1.8+-ee4c2c?style=for-the-badge&logo=pytorch&logoColor=white"></a>
    <a href="https://pytorchlightning.ai/">
        <img alt="Lightning" src="https://img.shields.io/badge/-Lightning 1.5+-792ee5?style=for-the-badge&logo=pytorchlightning&logoColor=white">
    </a>
    <a href="https://hydra.cc/">
        <img alt="Config: hydra" src="https://img.shields.io/badge/config-hydra 1.1-89b8cd?style=for-the-badge&labelColor=gray"></a>
    <a href="https://black.readthedocs.io/en/stable/">
        <img alt="Code style: black" src="https://img.shields.io/badge/code%20style-black-black.svg?style=for-the-badge&labelColor=gray">
    </a>
</p>

<p>
    <a href="#demo">View Demo</a>
    •
    <a href="https://github.com/XavierJiezou/Camera-Calibration/issues/new">Report Bug</a>
    •
    <a href="https://github.com/XavierJiezou/Camera-Calibration/issues/new">Request Feature</a>
</p>

<p>
    <a href="/docs/README.en.md">English </a>
    •
    <a href="/docs/README.cn.md">简体中文</a>
</p>

Love the project? Please consider [donating](https://paypal.me/xavierjiezou?country.x=C2&locale.x=zh_XC) to help it improve!

</div>

## Demo

![demo](https://raw.githubusercontent.com/XavierJiezou/Camera-Calibration/main/images/favicon_256x256.svg)

## Features

- [ ] Cloud mask with Landsat 8.
- [ ] Cloud mask with Sentinel 2.

## Install

```bash
pip install camera-calibration
```

## Usage

`$ cloudmask`

## Data

### Landasat 8

1. Download Landsat 8 data

```bash
python cloudmask/utils/download_landsat8.py
```

![download_landsat8](/images/download_landsat8.png)

2. Decompress Landsat8 data

```bash
python cloudmask/utils/decompress_landsat8.py
```

![download_landsat8](/images/decompress_landsat8.png)

### Sentinel 2

## Changelog

See [CHANGELOG.md](/CHANGELOG.md)

## License

[MIT License](/LICENSE)

## Dependencies

### Production Dependencies

[![Readme Card](https://github-readme-stats.vercel.app/api/pin/?username=psf&repo=requests)](https://github.com/psf/requests)

[![Readme Card](https://github-readme-stats.vercel.app/api/pin/?username=Textualize&repo=rich)](https://github.com/Textualize/rich)

[![Readme Card](https://github-readme-stats.vercel.app/api/pin/?username=google&repo=python-fire)](https://github.com/google/python-fire)

### Development dependencies

[![Readme Card](https://github-readme-stats.vercel.app/api/pin/?username=python-poetry&repo=poetry)](https://github.com/python-poetry/poetry)

[![Readme Card](https://github-readme-stats.vercel.app/api/pin/?username=pytest-dev&repo=pytest)](https://github.com/pytest-dev/pytest)

[![Readme Card](https://github-readme-stats.vercel.app/api/pin/?username=pytest-dev&repo=pytest-cov)](https://github.com/pytest-dev/pytest-cov)

[![Readme Card](https://github-readme-stats.vercel.app/api/pin/?username=pre-commit&repo=pre-commit)](https://github.com/pre-commit/pre-commit)

[![Readme Card](https://github-readme-stats.vercel.app/api/pin/?username=PyCQA&repo=flake8)](https://github.com/PyCQA/flake8)

[![Readme Card](https://github-readme-stats.vercel.app/api/pin/?username=PyCQA&repo=pylint)](https://github.com/PyCQA/pylint)

[![Readme Card](https://github-readme-stats.vercel.app/api/pin/?username=psf&repo=black)](https://github.com/psf/black)

[![Readme Card](https://github-readme-stats.vercel.app/api/pin/?username=uiri&repo=toml)](https://github.com/uiri/toml)


## 参考

- [Displaying webcam feed using OpenCV and Python+PySide.](https://gist.github.com/bsdnoobz/8464000)
- [OpenCV Face Detection Example](https://doc.qt.io/qtforpython/examples/example_external__opencv.html)

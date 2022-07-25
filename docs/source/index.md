<p align="center">
    <a href="https://pixelied.com/editor/design/62d95249afecc1406f2037a9"><img alt="logo" src="https://raw.githubusercontent.com/XavierJiezou/Camera-Calibration/main/images/favicon_256x256.svg" /></a>
<h1 align="center">相机标定器</h1>
<p align="center">一个基于OpenCV的自动化相机数据采集和标定程序。
</p>
</p>
<p align="center">
    <a href="https://github.com/XavierJiezou/Camera-Calibration/actions?query=workflow:Release">
        <img src="https://github.com/XavierJiezou/Camera-Calibration/workflows/Release/badge.svg"
            alt="GitHub Workflow Release Status" />
    </a>
    <a href="https://github.com/XavierJiezou/Camera-Calibration/actions?query=workflow:Lint">
        <img src="https://github.com/XavierJiezou/LitMNIST/workflows/Lint/badge.svg"
            alt="GitHub Workflow Lint Status" />
    <a
        href="https://www.codacy.com/gh/XavierJiezou/Camera-Calibration/dashboard?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=XavierJiezou/Camera-Calibration&amp;utm_campaign=Badge_Grade">
        <img src="https://app.codacy.com/project/badge/Grade/c2f85c8d6b8a4892b40059703f087eab" alt="Codacy Badge">
    </a>
    <a href="https://codecov.io/gh/XavierJiezou/Camera-Calibration">
        <img src="https://codecov.io/gh/XavierJiezou/Camera-Calibration/branch/main/graph/badge.svg?token=QpCLcUGoYx" alt="codecov">
    </a>
    <a href="https://pypi.org/project/Camera-Calibration/">
        <img src="https://img.shields.io/pypi/pyversions/Camera-Calibration" alt="PyPI - Python Version">
    </a>
    <a href="https://pypistats.org/packages/Camera-Calibration">
        <img src="https://img.shields.io/pypi/dm/Camera-Calibration" alt="PyPI - Downloads">
    </a>
    <a href="https://pypi.org/project/Camera-Calibration/">
        <img src="https://img.shields.io/pypi/v/Camera-Calibration" alt="PyPI">
    </a>
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
    <br />
    <br />
    <a href="https://www.python.org/">
        <img src="http://ForTheBadge.com/images/badges/made-with-python.svg" alt="forthebadge made-with-python">
    </a>
    <a href="https://github.com/XavierJiezou">
        <img src="http://ForTheBadge.com/images/badges/built-with-love.svg" alt="ForTheBadge built-with-love">
    </a>
</p>
<p align="center">
    <a href="#演示">观看演示</a>
    •
    <a href="https://github.com/xavierjiezou/Camera-Calibration/issues/new">报告错误</a>
    •
    <a href="https://github.com/xavierjiezou/Camera-Calibration/issues/new">功能需求</a>
  </p>
  <p align="center">
    <a href="/docs/README.en.md">English </a>
    •
    <a href="/docs/README.cn.md">简体中文</a>
</p>
<p align="center">喜欢这个项目吗？请考虑捐赠<a href="https://paypal.me/xavierjiezou?country.x=C2&locale.x=zh_XC">（<a
            href="https://raw.githubusercontent.com/XavierJiezou/Camera-Calibration/main/images/wechat.jpg">微信</a> | <a
            href="https://raw.githubusercontent.com/XavierJiezou/Camera-Calibration/main/images/alipay.jpg">支付宝</a>）</a>，以帮助它改善！</p>

## 演示

> 测试相机 RTSP 地址：[rtsp://admin:a12345678@y52t229909.zicp.vip](rtsp://admin:a12345678@y52t229909.zicp.vip)

![demo](https://raw.githubusercontent.com/XavierJiezou/Camera-Calibration/main/images/demo.png)

## 功能

- [x] RTSP 相机流数据采集
- [ ] 基于棋盘格的相机标定

## 安装

```bash
pip install camera-calibration
```

## 用法

`$ camera-calibration   `

## 日志

见 [CHANGELOG.md](/CHANGELOG.md)

## 证书

[MIT License](/LICENSE)

## 依赖

### 生产依赖

[![Readme Card](https://github-readme-stats.vercel.app/api/pin/?username=psf&repo=requests)](https://github.com/psf/requests)

[![Readme Card](https://github-readme-stats.vercel.app/api/pin/?username=Textualize&repo=rich)](https://github.com/Textualize/rich)

[![Readme Card](https://github-readme-stats.vercel.app/api/pin/?username=google&repo=python-fire)](https://github.com/google/python-fire)

### 开发依赖

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

# Xenon
一个优雅，用户友好的，基于 [Mirai](https://github.com/mamoe/mirai) 与
[Graia Project](https://github.com/GraiaProject/) 的 QQ 机器人应用。

[![License](https://img.shields.io/badge/license-AGPL--v3-green)](https://www.gnu.org/licenses/agpl-3.0.html)
[![Python Implementation](https://img.shields.io/badge/implementation-cpython-informational)](https://github.com/python/cpython)
[![Python Version](https://img.shields.io/badge/python-3.9-informational)](https://docs.python.org/zh-cn/3.9/)
[![Code Style](https://img.shields.io/badge/code%20style-black-black)](http://github.com/psf/black)
![Version](https://img.shields.io/badge/version-1.0.0--pre1-brightgreen)

## 许可证
Xenon 在与 [Mirai](https://github.com/mamoe/mirai) 和
[Graia Ariadne](https://github.com/GraiaProject/Ariadne) 相同的
[AGPL-v3](https://www.gnu.org/licenses/agpl-3.0.html) 许可证下开源。
和 [Mirai](https://github.com/mamoe/mirai) 一样，Xenon 不鼓励、不支持商用。

## 版本
Xenon 使用 [语义化版本2.0.0](https://semver.org/lang/zh-CN/spec/v2.0.0.html/) 。

## 开始

```shell
pipx install pdm

pdm install -G plugins

python ./main.py
```

请参照 [此处](https://graiax.cn/make_ero_bot/before/1_mirai.html) 部署 `mirai-api-http`.
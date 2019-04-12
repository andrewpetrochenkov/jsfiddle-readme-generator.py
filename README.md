<!--
https://pypi.org/project/readme-generator/
https://pypi.org/project/python-readme-generator/
-->

[![](https://img.shields.io/pypi/pyversions/jsfiddle-readme-generator.svg?longCache=True)](https://pypi.org/project/jsfiddle-readme-generator/)
[![](https://img.shields.io/pypi/v/jsfiddle-readme-generator.svg?maxAge=3600)](https://pypi.org/project/jsfiddle-readme-generator/)
[![Travis](https://api.travis-ci.org/looking-for-a-job/jsfiddle-readme-generator.py.svg?branch=master)](https://travis-ci.org/looking-for-a-job/jsfiddle-readme-generator.py/)

#### Installation
```bash
$ [sudo] pip install jsfiddle-readme-generator
```

#### Classes
class|`__doc__`
-|-
`jsfiddle_readme_generator.Readme` |README.md class. methods: `render`, `save(path)`

#### Executable modules
usage|`__doc__`
-|-
`python -m jsfiddle_readme_generator path ...` |generate jsfiddle README.md

#### Examples
generate multiple README.md files

```bash
$ find . -name "demo.html" -exec python -m jsfiddle_readme_generator {} \;
```
paths with spaces:

OS|speed|command
-|-|-
any|slow|`find . -name "demo.html" -exec python -m jsfiddle_readme_generator {} \;`
Linux|fast|`find . -name "demo.html" -print0 \| xargs -d '\n' python -m jsfiddle_readme_generator`
macOS|fast|`find . -name "demo.html" -print0 \| xargs -0 python -m jsfiddle_readme_generator`

#### Related projects
+   [`jsfiddle-build.py` - build `build.html` file from jsfiddle files](https://pypi.org/project/jsfiddle-build/)
+   [`jsfiddle-factory.py` - jsfiddles mass production](https://pypi.org/project/jsfiddle-build/)
+   [`jsfiddle-generator.py` - jsfiddle files generator](https://pypi.org/project/jsfiddle-generator/)
+   [`jsfiddle-github.py` - jsfiddle github integration helper](https://pypi.org/project/jsfiddle-github/)
+   [`jsfiddle-readme-generator.py` - generate jsfiddle `README.md`](https://pypi.org/project/jsfiddle-readme-generator/)

#### Links
+   [Github Integration - JSFiddle Docs](https://docs.jsfiddle.net/github-integration)

<p align="center">
    <a href="https://pypi.org/project/python-readme-generator/">python-readme-generator</a>
</p>
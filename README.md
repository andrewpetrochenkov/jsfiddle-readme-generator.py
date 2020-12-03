<!--
https://readme42.com
-->


[![](https://img.shields.io/pypi/v/jsfiddle-readme-generator.svg?maxAge=3600)](https://pypi.org/project/jsfiddle-readme-generator/)
[![](https://img.shields.io/badge/License-Unlicense-blue.svg?longCache=True)](https://unlicense.org/)
[![](https://github.com/andrewp-as-is/jsfiddle-readme-generator.py/workflows/tests42/badge.svg)](https://github.com/andrewp-as-is/jsfiddle-readme-generator.py/actions)

### Installation
```bash
$ [sudo] pip install jsfiddle-readme-generator
```

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

#### Related
+   [`jsfiddle-build.py` - build `build.html` from jsfiddle files](https://pypi.org/project/jsfiddle-build/)
+   [`jsfiddle-factory.py` - jsfiddles mass production](https://pypi.org/project/jsfiddle-build/)
+   [`jsfiddle-generator.py` - jsfiddle files generator](https://pypi.org/project/jsfiddle-generator/)
+   [`jsfiddle-github.py` - jsfiddle github integration helper](https://pypi.org/project/jsfiddle-github/)
+   [`jsfiddle-readme-generator.py` - generate jsfiddle `README.md`](https://pypi.org/project/jsfiddle-readme-generator/)

#### Links
+   [Github Integration - JSFiddle Docs](https://docs.jsfiddle.net/github-integration)

<p align="center">
    <a href="https://readme42.com/">readme42.com</a>
</p>

# :fire: HotSpot Identifier

For those who love(or hate) work at legacy projects, HotSpot Identifier cames to save you from that horrible and messy state. Identifying the most complexy and changed files in your code, a scatter chart is generated to guide you to where start the refactoring.

## Usage

```
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
make identify-hotspots path=/path/to/your/repository/root
```
## TODO
- Create section about how it works(tecnicliy)
- Explain the concept based on blog/articles
- Create video of usage
- Create CLI for usage
- Publish on pypi-test and pypi
- Use github actions to test the code
- Create section about use thecnologies based on language
    - Python: radon
- Create section about how to contribute

## Disclaimer
This tool only works on Python based projects, in the future maybe other languages will be supported too.
# jinja2-hack-skeleton
Jinja2 + Flask quick 'n dirty playground

### Installation

* make sure python 3.5.0 is available and in user - project contains `.python-version` for `pyenv`
* make sure `virtualenv` is installed (`pip install virtualenv`)

```
virtualenv ENV
source ENV/bin/activate
pip install -r requirements
python server.py
```

### Now what?

* `server.py` contains everything you need, it is quite self-documenting.
* Flask routes `@app.add_route('/')` define your URLs
* `render(template, variables)` helper renders your Jinja2 templates
	* define templates like this: `INDEX_TEMPLATE = jinja_env.get_template('index.html')`
	* variables should be a dict
* Static files should live in `static` directory
	* the `STATIC_URL = '/static/'` constant is available in templates: `{{STATIC_URL}}main.css == '/static/main.css'`
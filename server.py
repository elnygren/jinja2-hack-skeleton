from flask import Flask
import jinja2


#
# Settings
#

STATIC_URL = '/static/'


ALWAYS_AVAILABLE_VARS = {
    'STATIC_URL': STATIC_URL
}

#
# Setup Jinja2
#

jinja_env = jinja2.Environment(
    loader=jinja2.PackageLoader('app', 'templates'),
    extensions=['jinja2.ext.i18n']
)

def render(template, variables):
    """
    Helper for rendering Jinja2 templates.

    ALWAYS_AVAILABLE_VARS are available in all jinja2 templates.
    """
    return template.render({
        **ALWAYS_AVAILABLE_VARS,
        **variables,
    })


#
# Templates
#

INDEX_TEMPLATE = jinja_env.get_template('index.html')
SOME_OTHER_TEMPLATE = jinja_env.get_template('some_other_template.html')


#
# Setup Flask server
#

app = Flask(__name__)


@app.route('/')
def index():
    
    variables = {
        'greeting': 'Hello from the other side',
        'some_other_var': 'hmmm...'
    }

    return render(INDEX_TEMPLATE, variables)

@app.route('/some/other/route')
def some_other_route():
    
    variables = {
        'greeting': 'some other greeting'
    }

    return render(SOME_OTHER_TEMPLATE, variables)    


if __name__ == '__main__':
    app.run(debug=True)
    
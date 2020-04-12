# -*- coding: utf-8 -*-

from flask import flash, redirect, url_for, render_template
from flask.views import View
from flask_cache import Cache

from google.appengine.api import users
from google.appengine.runtime.apiproxy_errors import CapabilityDisabledError

from application import app
from decorators import login_required
from forms import ExampleForm
from models import ExampleModel

cache = Cache(app)


class AdminListExamples(View):

    @login_required
    def dispatch_request(self):
        examples = ExampleModel.query()
        form = ExampleForm()
        if form.validate_on_submit():
            example = ExampleModel(
                example_name=form.example_name.data,
                example_description=form.example_description.data,
                added_by=users.get_current_user()
            )
            try:
                example.put()
                example_id = example.key.id()
                cache.clear()
                flash(u'Example %s successfully saved.' % example_id, 'success')
                return redirect(url_for('list_examples'))
            except CapabilityDisabledError:
                flash(u'App Engine Datastore is currently in read-only mode.', 'info')
                return redirect(url_for('list_examples'))
        return render_template('list_examples.html', examples=examples, form=form)

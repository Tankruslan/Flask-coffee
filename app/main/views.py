from flask import render_template, redirect, flash
from .. import db
from ..models import Subscribers
from ..email import send_email
from . import main
from .forms import EmailForm


@main.route('/', methods=['GET', 'POST'])
def index():
    form = EmailForm()
    if form.validate_on_submit():
        subscriber = Subscribers.query.filter_by(email=form.email.data).first()
        if subscriber is None:
            subscriber = Subscribers(email=form.email.data)
            db.session.add(subscriber)
            db.session.commit()
            send_email(form.email.data.lower(), 'Coffee', 'email/subscribe')
        else:
            flash('Вы уже подписаны!')
        return redirect('/')
    return render_template('index.html', form=form)

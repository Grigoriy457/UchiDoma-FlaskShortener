from flask import *
import zlib

from . import app, db
from . import models
from . import forms


@app.route("/", methods=["GET", "POST"])
def home():
    form = forms.URLForm()
    if form.validate_on_submit():
        original_url = form.original_url.data
        url = models.Urls(original_url=original_url)
        db.session.add(url)
        db.session.commit()
        url.short = "%08X" % zlib.adler32(original_url.encode(), url.id)
        return redirect("/urls")
    return render_template("index.html", form=form)


@app.route("/<string:short>")
def short(short):
    url = models.Urls.query.filter_by(short=short).first()
    if url:
        url.visits += 1
        return redirect(url.original_url, 302)
    return abort(404)


@app.route("/urls/")
def urls():
    return render_template("urls.html", urls=models.Urls.query.all()[::-1], origin_url=request.host_url)

#!/usr/bin/python3

from jinja2 import Environment
from jinja2 import FileSystemLoader
import os
import shutil
import yaml

with open("settings.yml") as file:
    settings = yaml.load(file)
settings["metadata"]["phone_url"] = "tel:+{}{}".format(
    settings["metadata"]["phone_country_code"],
    settings["metadata"]["phone"]
        .replace(" ","")
        .replace("-","")
        .replace("(","")
        .replace(")","")
)
settings["metadata"]["email_url"] = "mailto:{}".format(
    settings["metadata"]["email"]
)

j2_env = Environment(loader=FileSystemLoader("templates"),
                     trim_blocks=True)

try:
    os.makedirs("build")
except OSError:
    pass

shutil.copy("static/logo.svg", "build")

with open("build/index.html", "w") as file:
    html = j2_env.get_template("index.html.j2").render(settings["metadata"])
    file.write(html)

with open("build/main.css", "w") as file:
    css = j2_env.get_template("main.css.j2").render(settings["style"])
    file.write(css)

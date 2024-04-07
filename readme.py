import re

with open("src/content/projects.md", "r") as p:
    projects = re.sub(r"\+\+\+[^\+]+\+\+\+\n", "", p.read(), re.M)
    with open("readme.template", "r") as t:
        template = t.read()
        with open("README.md", "w") as r:
            r.write(template.replace("%projects%", projects))

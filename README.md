# ![pyceo](https://github.com/jpsca/pyceo/raw/master/pyceo.png) [![Tests](https://travis-ci.org/jpsca/pyceo.svg?branch=master)](https://travis-ci.org/jpsca/pyceo/) [![Coverage Status](https://coveralls.io/repos/github/jpsca/pyceo/badge.svg?branch=master)](https://coveralls.io/github/jpsca/pyceo?branch=master) 

*It looks good and delegates all the real work to you* ;)

A minimal and ridiculously good looking command-line-interface toolkit.

In four points:

- Completely customizable help page, but pretty by default.
- Add new commands at any time and from other files.
- No sub-commands but grouping of commands instead.
- Easy to use and understand.


## An example

![pyceo output](https://github.com/jpsca/pyceo/raw/master/output.png)

This autogenerated (and completely customizable) help message comes from running
the example below:

```python
# example.py
from pyceo import Manager, param, option


cli = Manager("Welcome to Proper v1.2.3")


@cli.command(help="Creates a new Proper application at `path`.")
@param("path", help="Where to create the new application.")
@option("quiet", help="Supress all output.")
def new(path):
    """The `proper new` command creates a new Proper application with a default
    directory structure and configuration at the path you specify.

    Example: `proper new ~/Code/blog`
    This generates a skeletal Proper application at `~/Code/blog`.
    """
    pass


@cli.command()
@option("num", type=int)  # Optional type
def fizzbuzz(num=3):
    """A bad fizz buzz."""
    print("fizz " * num + "buzz")


@cli.command(group="db")
@option("message", help="Revision message")
@option("sql", help="Dont emit SQL to database - dump to standard output instead")
@option("head", help="Specify head or <branchname>@head to base new revision on")
def migrate(**kwargs):
    """Autogenerate a new revision file.

    This is an alias for "revision --autogenerate"."""
    pass


@cli.command(group="db")
@option("name", help="Name of section in .ini file to use for Alembic config")
def branches(**kwargs):
    """Show current branch points.
    """
    pass


if __name__ == "__main__":
    # cli.run(default="new")
    cli.run()
```


## How minimal?

**pyceo** doesn't include any related features like prompts, progress bars, table formatting, [file editing](https://pypi.org/project/text-editor/), etc. It doesn't matter because for those features many dedicated python libraries can be used.

You could say it *focuses on its core competencies while synergetically interface with other libraries to take it to the next level*. 💪🚀


## Why don't just use optparse or argparse?

Are you kidding? Because this is way easier to use and understand.


## Why don't just use click?

Because this looks better and is easier to use and understand.


## Why don't just use...?

Because this library fits better my mental model. I hope it matches yours as well.

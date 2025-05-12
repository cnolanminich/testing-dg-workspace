import my_cool_project.defs

from dagster.components import definitions, load_defs


@definitions
def defs():
    return load_defs(defs_root=my_cool_project.defs)

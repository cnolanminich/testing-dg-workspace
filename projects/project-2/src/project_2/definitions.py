import project_2.defs

from dagster.components import definitions, load_defs


@definitions
def defs():
    return load_defs(defs_root=project_2.defs)

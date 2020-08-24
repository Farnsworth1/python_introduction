def _jupyter_server_extension_paths():
    return [{
        "module": "default_cell"
    }]

# Jupyter Extension points
def _jupyter_nbextension_paths():
    return [dict(
        section="notebook",
        # the path is relative to the `my_fancy_module` directory
        src="static",
        # directory in the `nbextension/` namespace
        dest="default_cell",
        # _also_ in the `nbextension/` namespace
        require="default_cell/main")]

def load_jupyter_server_extension(nbapp):
    nbapp.log.info("default cell enabled!")
from fabric.api import local, settings, abort
from fabric.contrib.console import confirm


def test_with_fail():
    with settings(warn_only=True):
        result = local('./manage.py test service_manager', capture=True)
    if result.failed and not confirm("Tests Failed, Continue anyway?"):
        abort("Aborting at user request.")

def test():
    local("./manage.py test service_manager")

def commit():
    local("git add . && git commit")

def push():
    local("git push -u origin master")


def prepare_deploy():
    test()
    commit()
    push()

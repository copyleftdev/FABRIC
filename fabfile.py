from fabric.api import local


def test():
    local("./manage.py test service_manager")

def commit():
    local("git add . && git commit -am.")

def push():
    local("git push")


def prepare_deploy():
    test()
    commit()
    push()

from fabric.api import local, settings, abort, run, cd, env, hosts, parallel
from fabric.contrib.console import confirm



def test_with_fail():
    with settings(warn_only=True):
        result = local('./manage.py test service_manager', capture=True)
    if result.failed and not confirm("Tests Failed, Continue anyway?"):
        abort("Aborting at user request.")

def test():
    local("./manage.py test service_manager")

def commit():
    local("git add . && git commit -am.")

def push():
    local("git push -u origin master")


def prepare_deploy():
    test()
    commit()
    push()
@hosts("target-01.codetestcode.io", "target-02.codetestcode.io"
       ,"target-03.codetestcode.io", "target-04.codetestcode.io")
@parallel
def deploy():
    code_dir = "~/deploy_app"
    with settings(warn_only=True):
        if run("test -d {}".format(code_dir)).failed:
            run("git clone https://github.com/copyleftdev/FABRIC.git {}".format(code_dir))
    with cd(code_dir):
        run("git pull")
        run("touch app.wsgi")

@hosts("target-01.codetestcode.io", "target-02.codetestcode.io"
       ,"target-03.codetestcode.io", "target-04.codetestcode.io")
@parallel
def roleback():
    code_dir = "~/deploy_app"
    run("rm -fr {}".format(code_dir))

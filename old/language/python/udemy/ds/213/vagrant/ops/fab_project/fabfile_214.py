from fabric.api import run, env, roles, task, parallel, execute, runs_once

env.hosts = ['root@172.16.200.101:22', 'root@172.16.200.102:22']
env.passwords = {
    'root@172.16.200.101:22': 'root',
    'root@172.16.200.102:22': 'root',
}

env.roledefs = {
    'web': ['root@172.16.200.101:22'],
    'db': ['root@172.16.200.102:22']
}

@roles('web')
def host_type():
    run('uname -s')

@roles('db')
def host_files():
    run('ls -ltraS')

def all_files():
    run('ls -ltraS')

@task()
def go():
    all_files()
    run('pwd')


@task(default=True)
def who():
    run('whoami')

@task
@parallel(pool_size=2)
def para():
    run('ls -la')


@task
def argtest(arg1, arg2):
    print(arg1, arg2)


def test():
    return run('ls -la')

@task
def org():
    r = execute(test)
    print(r)


@runs_once
def db_init():
    print('init')

@task
def deploy_db():
    db_init()
    db_init()

from fabric.api import *
from fabric.contrib.files import *

@task
def clean_and_upload():
    local('ls -la')
    put('fabfile.py', '/tmp/fabfile.py')
    with cd('/tmp'):
        run('pwd')
        run('ls -l')
        print(exists('/tmp/fabfile.py'))

import db.checking
from fabric.colors import green, red

@task
@parallel(pool_size=2)
def split_test():
    r = execute(db.checking.check)
    print(red(r))
    print(r)
    print(green('success'))
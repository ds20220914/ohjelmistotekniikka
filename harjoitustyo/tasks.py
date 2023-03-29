from invoke import task

@task

def build(ctx):
	ctx.run("python3 src/build.py",pty=True)
	
	
@task
def test(ctx):
    ctx.run("pytest src", pty=True)

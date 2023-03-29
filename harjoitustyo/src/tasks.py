from invoke import task

@task

def build(ctx):
	ctx.run("python3 build.py",pty=True)

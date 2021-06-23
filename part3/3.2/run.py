import os
import git

git.Repo.clone_from(os.environ['GITHUB_REPOSITORY'])

os.chdir(f'./{os.environ['GITHUB_REPOSITORY']}')

for _, _, f in os.walk(os.getcwd()):
    if "Dockerfile" in f:
        os.system(f'docker build . -t {os.environ['IMAGE']} && docker push {os.environ['IMAGE']}')
        break
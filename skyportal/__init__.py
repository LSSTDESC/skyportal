__version__ = '0.9.dev0'

if 'dev' in __version__:
    import subprocess
    p = subprocess.Popen(['git', 'log', '-1', '--format="%h %aI"'],
                         stdout=subprocess.PIPE,
                         stderr=subprocess.PIPE)
    out, err = p.communicate()
    git_hash, git_date = (out.decode('utf-8').strip().replace('"', '')
                          .split('T')[0].replace('-', '').split())

    __version__ += f'+git{git_date}.{git_hash}'

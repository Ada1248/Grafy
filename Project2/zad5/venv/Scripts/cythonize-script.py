#!"D:\studia\Rok 3 Semestr 2\Grafy\Proj2\zad5\venv\Scripts\python.exe"
# EASY-INSTALL-ENTRY-SCRIPT: 'Cython==0.29.16','console_scripts','cythonize'
__requires__ = 'Cython==0.29.16'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('Cython==0.29.16', 'console_scripts', 'cythonize')()
    )

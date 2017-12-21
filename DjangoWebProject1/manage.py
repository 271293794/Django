#!/usr/bin/env python
"""
Command-line utility for administrative tasks.
"""

import os
import sys

if __name__ == "__main__":
    os.environ.setdefault(
        "DJANGO_SETTINGS_MODULE",  
        "DjangoWebProject1.settings"
    )
#!/加注释11111222223333344445555566667777888899990000

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)

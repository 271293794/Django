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
#!/加注释1111122222333334444555556666777788889999

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)

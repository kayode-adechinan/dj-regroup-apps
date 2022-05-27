# Regroup your apps inside app folder

```bash

import os
import sys

import sys
sys.path.insert(0, os.path.join(BASE_DIR, 'apps'))
```

# How to add new app

cd apps

python ../manage.py startapp app1

cd apps && python ../manage.py startapp app2 && cd ..

# Use custom command

see common/commands/make_app.py

python manage.py make_app app3

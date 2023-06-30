#! /bin/bash
pip install bsddb3
cd $(python -c 'import os; print(os.path.dirname(os.__file__))') && ln -f -s ../site-packages/bsddb3/_pybsddb.so bsddb/_bsddb.so


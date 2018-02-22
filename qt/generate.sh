pyuic4 -o tx.py tx.ui
pyuic4 -o listing.py listing.ui
pyuic4 -o mainw.py main.ui
(cd resources && pyrcc4 -py3 resources.qrc  -o ../resources.py)

[Desktop Entry]

# The type as listed above
Type=Application

# The version of the desktop entry specification to which this file complies
Version=1.0

# The name of the application
Name=QuShape

# A comment which can/will be used as a tooltip
Comment=Data Analysis of shape-ce

# The path to the folder in which the executable is run
Path={QuShapePath}

# The executable of the application, possibly with arguments.
Exec=zsh -c "source ~/.zshrc && conda activate qushape && cd {QuShapePath}/src && python main.py"

# The name of the icon that will be used to display this entry
Icon={QuShapePath}/src/Icons/QuShapeIcon.png

# Describes whether this application needs to be run in a terminal or not
Terminal=false

# Describes the categories in which this entry should be shown
Categories=Science;

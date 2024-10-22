Cut Plan Manipulator for CNC Nanxing
Description
This program is a cut plan manipulator for CNC Nanxing, acting as a tool compensator. It allows you to adjust the coordinates of points in an XML file according to a new tool diameter, facilitating the adaptation of files for different milling configurations.

Features
Adjusts the coordinates of workpiece points in an XML file based on a new tool diameter.
Generates a new XML file with the adjusted coordinates while maintaining the original file structure.
Simple user interface for input, allowing the selection of the XML file and the new diameter.
Prerequisites
Python 3.x
Libraries: tkinter, xml.etree.ElementTree, codecs
How to Use
Clone the repository:

bash
Copiar código
git clone <repository-URL>
cd <repository-name>
Run the script:

bash
Copiar código
python your_script.py
Enter the path of the XML file and the new tool diameter when prompted.

The new adjusted XML file will be saved in the New_Xml folder.

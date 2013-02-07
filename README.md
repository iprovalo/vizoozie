VizOozie
------------

VizOozie is an Oozie workflow visualization tool.  This script will generate a dot file from an Oozie workflow definition xml file, which can be converted to pdf or other formats with graphviz dot.  Action colors are configurable in the properties file.  See the colors supported by graphviz dot. 

Installation (optional, to run the tests):
------------
    sudo python setup.py install

Running Tests
------------
	python test/test_vizoozie.py
		
Running VizOozie
------------
    python vizoozie/vizoozie.py example/workflow.xml example/workflow.dot
	
Dot to Pdf
------------
	dot -Tpdf example/workflow.dot -o example/workflow.pdf


-----------------------------------------------
Ooozie: tested with Oozie 3.2

Requirements: Unix like environment, python, graphviz dot.

Legend:

1. Standard workflow shapes are used for start/end/process/join/fork/decision.

2. Colors for Actions Types are defined in the vizoozie.properties.

Enjoy!

Ivan

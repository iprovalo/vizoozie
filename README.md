vizoozie

This script will generate a dot file from an Oozie workflow definition xml file, which can be converted to pdf or other formats with graphviz dot.  Action colors are configurable in the properties file.  See the colors supported by graphviz dot. 

Installation
------------
    python setup.py install

Running Tests
------------
	python test/test_vizoozie.py
		
Running Vizoozie
------------
    python vizoozie/vizoozie.py example/workflow.xml example/workflow.dot
	
Dot to Pdf: run graphviz dot program to generate the diagram in pdf or another format (see graphviz dot documentation):
------------
	dot -Tpdf example/workflow.dot -o example/workflow.pdf


-----------------------------------------------
Ooozie: tested with Oozie 3.2

Requirements: Unix like environment, python, graphviz dot.

Legend:

1. Standard workflow shapes are used for start/end/process/join/fork/decision.

2. Colors for Actions Types (see vizoozie.properties):

java: blue
map-reduce: green
fs: gray
pig: bisque
ssh: khaki
sub-workflow: pale golden

Ivan
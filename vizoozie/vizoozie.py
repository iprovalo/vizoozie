#!/usr/bin/env python
import getopt, sys, re
from xml.dom.minidom import parseString

VERSION='0.1'

class VizOozie(object):
    
    properties = {}
    
    def loadProperties(self):
        with open("vizoozie/vizoozie.properties") as f:
            for line in f:
                key, val = line.split('=')
                self.properties[key] = val
    
    def getName(self, node):
        attr = self.getAttribute(node, "name")
        return attr
    
    def getTo(self, node):
        attr = self.getAttribute(node, "to")
        return attr
    
    def getAttribute(self, node, attributeName):
        attr = node.getAttribute(attributeName)
        return attr
    
    def getOK(self, node):
        ok = node.getElementsByTagName("ok")[0]
        return ok
    
    def processHeader(self, name):
        output = "digraph{\nsize = \"8,8\";ratio=fill;node[fontsize=24];labelloc=\"t\";label=\"" + name + "\";\n"
        return output

    def processStart(self, doc):
        output = ''
        start = doc.getElementsByTagName("start")[0]
        to = self.getTo(start)
        output = '\n' + "start -> " + to.replace('-', '_') + ";\n"
        return output

    def processAction(self, doc):
        output = ''
        for node in doc.getElementsByTagName("action"):
            name = self.getName(node)
            color = "white"
            for key, value in self.properties.iteritems():
                if len(node.getElementsByTagName(key)) != 0:
                    color = value
                    break
            ok = self.getOK(node)
            to = self.getTo(ok)
            output += '\n'+name.replace('-', '_') + " [shape=box,style=filled,color=" + color + "];\n"
            output += '\n'+name.replace('-', '_') + " -> " + to.replace('-', '_') + ";\n"
        return output
    
    def processFork(self, doc):
        output = ''
        for node in doc.getElementsByTagName("fork"):
            name = self.getName(node)
            output += '\n' + name.replace('-', '_') + " [shape=octagon];\n"
            for path in node.getElementsByTagName("path"):
                start = path.getAttribute("start")
                output += '\n' + name.replace('-', '_') + " -> " + start.replace('-', '_') + ";\n"
        return output


    def processJoin(self, doc):
        output = ''
        for node in doc.getElementsByTagName("join"):
            name = self.getName(node)
            to = self.getTo(node)
            output += '\n' + name.replace('-', '_') + " [shape=octagon];\n"
            output += '\n' + name.replace('-', '_') + " -> " + to.replace('-', '_') + ";\n"
        return output


    def processDecision(self, doc):
        output = ''
        for node in doc.getElementsByTagName("decision"):
            name = self.getName(node)
            switch = node.getElementsByTagName("switch")[0]
            output += '\n' + name.replace('-', '_') + " [shape=diamond];\n"
            for case in switch.getElementsByTagName("case"):
                to = case.getAttribute("to")
                caseValue = case.childNodes[0].nodeValue.replace('"', '')
                output += '\n' + name.replace('-', '_') + " -> " + to.replace('-', '_') + "[style=bold,label=\"" + caseValue + "\",fontsize=20];\n"
            
            default = switch.getElementsByTagName("default")[0]
            to = default.getAttribute("to")
            output += '\n' + name.replace('-', '_') + " -> " + to.replace('-', '_') + "[style=dotted,label=\"default\",fontsize=20];\n"
        return output


    def processCloseTag(self):
        output = '\n' + "}"
        return output


    def convertWorkflowXMLToDOT(self, input_str, name):
        self.loadProperties()
        doc = parseString(input_str)
        output = self.processHeader(name)
        output += self.processStart(doc)
        output += self.processAction(doc)
        output += self.processFork(doc)
        output += self.processJoin(doc)
        output += self.processDecision(doc)
        output += self.processCloseTag()
        return output
    
def main():
    vizoozie = VizOozie()
    if len(sys.argv) < 3:
        print("Usage: python vizoozie.py <Input Oozie workflow xml file name> <output dot file name>")
        exit(1)
    inputFile = open(sys.argv[1], 'r')    
    input_str = inputFile.read()
    output = vizoozie.convertWorkflowXMLToDOT(input_str, sys.argv[1])
    outputFile = open(sys.argv[2], 'w')
    outputFile.write(str(output))
    outputFile.close()
    
    
if __name__ == "__main__":
    main()
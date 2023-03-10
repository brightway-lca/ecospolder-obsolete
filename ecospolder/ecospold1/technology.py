import sys
sys.path.append('../')
from ecospold_base import *

class Technology(EcospoldBase):
    """Technology -- Contains a description of the technology for which flow data have been collected. Free text can be used. Pictures, graphs and tables are not allowed. The text should cover information necessary to identify the properties and particularities of the technology(ies) underlying the process data.
    text -- Describes the technological properties of the unit process. If the process comprises several subprocesses, the corresponding technologies should be reported as well. Professional nomenclature should be used for the description.
    The description helps the user to judge the technical suitability of the process dataset for his or her application (purpose).
    No graphs, figures or tables are allowed in this text field.
    It should be stated if data for certain elementary flows or intermediate product flows are derived from different technology.

    """

    def __init__(self, text=None, collector=None, **kwargs) -> None:
        self.collector = collector
        self.elementtree_node = None
        self.original_tagname = None
        self.parent_object = kwargs.get("parent_object")
        self.text = cast_value_with_type(None, text)

    def validate_TString32000(self, value) -> bool:
        # Validate type TString32000, a restriction on xsd:string.
        if (
            value is not None
            and Validate_simpletypes
            and self.collector is not None
        ):
            if not isinstance(value, str):
                lineno = self.get_node_lineno()
                self.collector.add_message(
                    'Value "%(value)s"%(lineno)s is not of the correct base simple type (str)'
                    % {
                        "value": value,
                        "lineno": lineno,
                    }
                )
                return False
            if len(value) > 32000:
                lineno = self.get_node_lineno()
                self.collector.add_message(
                    'Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on TString32000'
                    % {"value": encode_str_2_3(value), "lineno": lineno}
                )
                result = False

    def hasContent(self) -> bool:
        if ():
            return True
        else:
            return False

    def export(
        self,
        outfile,
        level,
        namespaceprefix="",
        namespacedef='xmlns:es="http://www.EcoInvent.org/EcoSpold01"',
        name="Technology",
        pretty_print=True,
    ):
        if pretty_print:
            eol = "\n"
        else:
            eol = ""
        if self.original_tagname is not None and name == "Technology":
            name = self.original_tagname
        showIndent(outfile, level, pretty_print)
        outfile.write(
            "<%s%s%s"
            % (
                namespaceprefix,
                name,
                namespacedef and " " + namespacedef or "",
            )
        )
        already_processed = set()
        self.exportAttributes(
            outfile, level, already_processed, namespaceprefix, name="Technology"
        )
        if self.hasContent():
            outfile.write(">%s" % (eol,))
            self.exportChildren(
                outfile,
                level + 1,
                namespaceprefix,
                namespacedef,
                name="Technology",
                pretty_print=pretty_print,
            )
            outfile.write("</%s%s>%s" % (namespaceprefix, name, eol))
        else:
            outfile.write("/>%s" % (eol,))

    def exportAttributes(
        self,
        outfile,
        level,
        already_processed,
        namespaceprefix="",
        name="Technology",
    ):
        if self.text is not None and "text" not in already_processed:
            already_processed.add("text")
            outfile.write(
                " text=%s"
                % (
                    self.encode(
                        self.format_string(
                            quote_attrib(self.text), input_name="text"
                        )
                    ),
                )
            )

    def exportChildren(
        self,
        outfile,
        level,
        namespaceprefix="",
        namespacedef='xmlns:es="http://www.EcoInvent.org/EcoSpold01"',
        name="Technology",
        fromsubclass=False,
        pretty_print=True,
    ):
        pass

    def build(self, node, collector=None):
        self.collector = collector
        if SaveElementTreeNode:
            self.elementtree_node = node
        already_processed = set()
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName = tag_pattern.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName, collector=collector)
        return self

    def buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value("text", node)
        if value is not None and "text" not in already_processed:
            already_processed.add("text")
            self.text = value
            self.validate_TString32000(self.text)  # validate type TString32000

    def buildChildren(
        self, child_, node, nodeName, fromsubclass=False, collector=None
    ):
        pass


# end class Technology

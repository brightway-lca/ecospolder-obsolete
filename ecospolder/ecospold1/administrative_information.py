from data_entry_by import DataEntryBy
from data_generator_and_publication import DataGeneratorAndPublication
import sys
sys.path.append('../')
from ecospold_base import *
from person import Person


class AdministrativeInformation(EcospoldBase):

    """AdministrativeInformation -- Contains information about the person that compiled and entered the dataset in the database and about kind of publication and the accessibility of the dataset.
    dataEntryBy -- Contains information about the person and the quality network the person belongs to.
    dataGeneratorAndPublication -- Contains information about the generator of the dataset in the database, whether the dataset has been published (and how) and about copyright and the accessibility of the dataset (public or restricted to ETH domain, ECOINVENT, or a particular institute of ECOINVENT.
    person -- Contains a list of persons with their addresses.

    """

    ##############################################
    ### AdministrativeInformation Constructor ###
    ##############################################

    def __init__(
        self,
        dataEntryBy=None,
        dataGeneratorAndPublication=None,
        person=None,
        collector=None,
        **kwargs
    ) -> None:
        self.collector = collector
        self.elementtree_node = None
        self.original_tagname = None
        self.parent_object = kwargs.get("parent_object")
        self.dataEntryBy = dataEntryBy
        self.dataGeneratorAndPublication = dataGeneratorAndPublication
        self.person = [] if person is None else person

    def hasContent(self) -> bool:
        if (
            self.dataEntryBy is not None
            or self.dataGeneratorAndPublication is not None
            or self.person
        ):
            return True
        else:
            return False

    def export(
        self,
        outfile,
        level,
        namespaceprefix="",
        namespacedef='xmlns:es="http://www.EcoInvent.org/EcoSpold01" xmlns:None="http://www.EcoInvent.org/EcoSpold01" ',
        name="AdministrativeInformation",
        pretty_print=True,
    ) -> None:
        if pretty_print:
            eol = "\n"
        else:
            eol = ""
        if self.original_tagname is not None and name == "AdministrativeInformation":
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
            outfile,
            level,
            already_processed,
            namespaceprefix,
            name="AdministrativeInformation",
        )
        if self.hasContent():
            outfile.write(">%s" % (eol,))
            self.exportChildren(
                outfile,
                level + 1,
                namespaceprefix,
                namespacedef,
                name="AdministrativeInformation",
                pretty_print=pretty_print,
            )
            showIndent(outfile, level, pretty_print)
            outfile.write("</%s%s>%s" % (namespaceprefix, name, eol))
        else:
            outfile.write("/>%s" % (eol,))

    def exportAttributes(
        self,
        outfile,
        level,
        already_processed,
        namespaceprefix="",
        name="AdministrativeInformation",
    ) -> None:
        pass

    def exportChildren(
        self,
        outfile,
        level,
        namespaceprefix="",
        namespacedef='xmlns:es="http://www.EcoInvent.org/EcoSpold01" xmlns:None="http://www.EcoInvent.org/EcoSpold01" ',
        name="AdministrativeInformation",
        fromsubclass=False,
        pretty_print=True,
    ) -> None:
        if pretty_print:
            eol = "\n"
        else:
            eol = ""
        if self.dataEntryBy is not None:
            self.dataEntryBy.export(
                outfile,
                level,
                namespaceprefix,
                namespacedef="",
                name="dataEntryBy",
                pretty_print=pretty_print,
            )
        if self.dataGeneratorAndPublication is not None:
            self.dataGeneratorAndPublication.export(
                outfile,
                level,
                namespaceprefix,
                namespacedef="",
                name="dataGeneratorAndPublication",
                pretty_print=pretty_print,
            )
        for one_person in self.person:
            one_person.export(
                outfile,
                level,
                namespaceprefix,
                namespacedef="",
                name="person",
                pretty_print=pretty_print,
            )

    def build(self, node, collector=None) -> None:
        self.collector = collector
        if SaveElementTreeNode:
            self.elementtree_node = node
        already_processed = set()
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName = tag_pattern.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName, collector=collector)

    def buildAttributes(self, node, attrs, already_processed) -> None:
        pass

    def buildChildren(
        self, child_, node, nodeName, fromsubclass=False, collector=None
    ) -> None:
        if nodeName == "dataEntryBy":
            obj = DataEntryBy(parent_object=self)
            obj.build(child_, collector=collector)
            self.dataEntryBy = obj
            obj.original_tagname = "dataEntryBy"
        elif nodeName == "dataGeneratorAndPublication":
            obj = DataGeneratorAndPublication(parent_object=self)
            obj.build(child_, collector=collector)
            self.dataGeneratorAndPublication = obj
            obj.original_tagname = "dataGeneratorAndPublication"
        elif nodeName == "person":
            obj = Person(parent_object=self)
            obj.build(child_, collector=collector)
            self.person.append(obj)
            obj.original_tagname = "person"



# end class AdministrativeInformation

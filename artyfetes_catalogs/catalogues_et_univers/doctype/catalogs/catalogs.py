# Copyright (c) 2025, Frappe Technologies Pvt. Ltd. and contributors
# For license information, please see license.txt

import frappe
from frappe.utils.nestedset import NestedSet


class Catalogs(NestedSet):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from erpnext.selling.doctype.sales_order_item.sales_order_item import SalesOrderItem
		from frappe.types import DF

		custom_html: DF.HTMLEditor | None
		is_group: DF.Check
		isactive: DF.Check
		isvisible: DF.Check
		lft: DF.Int
		old_parent: DF.Link | None
		parent_catalogs: DF.Link | None
		products: DF.Table[SalesOrderItem]
		rgt: DF.Int
		title: DF.Data
	# end: auto-generated types
	pass

	def validate(self):
		if self.type == "Catalogue":
			self.is_group = 1
		else:
			self.is_group = 0


@frappe.whitelist()
def get_active_tree_nodes(doctype, parent=None, is_root=False):
    """
    Get active tree nodes.
    """
    filters = {"isactive": 1}
    if parent: 
        filters["parent_catalogs"] = parent
    else:
        filters["parent_catalogs"] = ""

    nodes = frappe.get_all(
        doctype,
        filters=filters,
        fields=["name", "title", "is_group", "parent_catalogs", "creation"],
        order_by="creation DESC",
    )

    for node in nodes:
        node["value"] = node["name"]
        node["expandable"] = 1 if node["is_group"] else 0

    return nodes
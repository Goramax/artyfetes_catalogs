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
def get_active_tree_nodes(doctype, parent=None, is_root=False, **filters):
    """
    Renvoie les nœuds filtrés par `isactive`.
    """
    # Ajoute le filtre isactive
    filters = {"isactive": 1}

    # Récupère les enfants du parent donné
    nodes = NestedSet.get_children(doctype, parent, filters=filters, is_root=is_root)

    return nodes
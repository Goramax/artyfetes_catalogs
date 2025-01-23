# Copyright (c) 2025, Frappe Technologies Pvt. Ltd. and contributors
# For license information, please see license.txt

import frappe
from frappe.utils.nestedset import NestedSet
from frappe.desk.treeview import get_all_nodes


class Catalogs(NestedSet):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from erpnext.accounts.doctype.sales_invoice_item.sales_invoice_item import SalesInvoiceItem
		from frappe.types import DF

		custom_html: DF.HTMLEditor | None
		is_group: DF.Check
		isactive: DF.Check
		isvisible: DF.Check
		lft: DF.Int
		old_parent: DF.Link | None
		parent_catalogs: DF.Link | None
		products: DF.Table[SalesInvoiceItem]
		rgt: DF.Int
		title: DF.Data
	# end: auto-generated types
	pass

@frappe.whitelist()
def get_active_tree_nodes(doctype, parent=None, is_root=False):
	nodes = get_all_nodes(doctype, parent, is_root, tree_method="get_children")
    # Appliquez le filtre `isActive`
	return [node for node in nodes if node.get("isActive") == 1]

@frappe.whitelist()
def get_children(doctype, parent=None):
    filters = {"parent_catalogs": parent} if parent else {}
    return frappe.get_all(doctype, filters=filters, fields=["name", "isActive"])
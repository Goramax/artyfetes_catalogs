import frappe
from frappe.utils.nestedset import rebuild_tree

# Check if function is already in progress to prevent recursion
is_root_creation_in_progress = False

def ensure_root_nodes(doc=None, method=None):
    global is_root_creation_in_progress

    # If function is already in progress, return
    if is_root_creation_in_progress:
        return

    try:
        is_root_creation_in_progress = True

        # Create root nodes 'Univers and Catalogues' if they don't exist
        root_nodes = ["Catalogue", "Univers"]
        for root in root_nodes:
            if not frappe.db.exists("Catalogs", root):
                frappe.get_doc({
                    "doctype": "Catalogs",
                    "name": root,
                    "title": root,
                    "is_group": 1, 
                    "parent_catalogs": None
                }).insert()

        rebuild_tree("Catalogs")

    finally:
        is_root_creation_in_progress = False
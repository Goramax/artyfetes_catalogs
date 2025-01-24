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
                    "isactive": 1,
                    "parent_catalogs": None
                }).insert()

        rebuild_tree("Catalogs")

    finally:
        is_root_creation_in_progress = False
        
        
        
@frappe.whitelist()
def get_active_catalogs(linked_item = None, is_active = 1):
    """Get all active catalogs that are visible and have a parent catalog.

    Args:
        linked_item (string, optional): Defaults to None. Id of the item to get catalogs for.
        is_active (int, optional): Defaults to 1. 1 for active catalogs, 0 for inactive catalogs.

    Returns:
        dict: Dictionary of catalogs grouped by parent catalog.
    """
    
    if linked_item is None:
        catalogs = frappe.db.get_all(
            "Catalogs",
            filters={
                "isactive": is_active,
                "parent_catalogs": ["!=", ""],
            },
            fields=["name", "title", "isvisible", "isactive", "parent_catalogs"],
        )
    else:
        
        catalogs = frappe.db.sql(
            """
            SELECT
                catalog.title, catalog.isvisible, catalog.isactive, catalog.parent_catalogs
            FROM
                `tabCatalogs` catalog
            LEFT JOIN
                `tabLinked Articles` l_articles
            ON
                catalog.name = l_articles.parent
            WHERE
                catalog.isactive = %s
            AND
                catalog.parent_catalogs != ""
            AND
                l_articles.article = %s
            """,
            (is_active, linked_item),
            as_dict=True,
        )
                    

    # regroup catalogs by parent
    catalogs_dict = {}
    for catalog in catalogs:
        if catalog.parent_catalogs not in catalogs_dict:
            catalogs_dict[catalog.parent_catalogs] = []
        catalogs_dict[catalog.parent_catalogs].append(catalog)
                
                
    return catalogs_dict
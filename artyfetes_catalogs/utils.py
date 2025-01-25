import frappe        
        
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

@frappe.whitelist()
def get_catalog_universes(catalog_name):
    """Get all universes for a catalog.

    Args:
        catalog_name (string): Name of the catalog to get universes for.

    Returns:
        list: List of universes for the catalog.
    """
    
    universes = frappe.db.get_all(
        "Catalogs",
        filters={"parent_catalogs": catalog_name, "type": "Univers"},
        fields=["title", "isvisible", "isactive"],
    )
    
    return universes

@frappe.whitelist()
def item_disable_check(doc, method=None):
    """If item is disabled, is_purchase_item and is_sales_item are set to false.

    Args:
        doc (dict): Item document.
        method (str, optional): Defaults to None. Method to call.
    """
    
    if doc.disabled == 1:
        doc.is_purchase_item = 0
        doc.is_sales_item = 0
    return doc

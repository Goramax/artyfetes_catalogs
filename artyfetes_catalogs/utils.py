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
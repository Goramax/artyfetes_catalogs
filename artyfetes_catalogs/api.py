import frappe        
        
@frappe.whitelist(allow_guest=True) # Allow guest to access this function without authentication (from postman)
def get_items_of_universe(universe_name, catalog_name):
    """Get all items of a universe.

    Args:
        universe_name (string): Name of the universe to get items for.

    Returns:
        list: List of items for the universe.
    """
    
    # get all items of a universe (table Linked Articles, child table of Catalogs)
    items = frappe.db.sql(
        """
        SELECT
            item.name, item.image, item.description
        FROM
            `tabItem` item
        LEFT JOIN
            `tabLinked Article` l_articles
            ON
                item.name = l_articles.article
        LEFT JOIN
            `tabCatalog` catalog
            ON
                l_articles.parent = catalog.name
        WHERE
            l_articles.parent = %s AND catalog.parent_catalog = %s 
                AND item.disabled = 0  AND catalog.isactive = 1
                AND catalog.isvisible = 1
            """,
        (universe_name, catalog_name),
        as_dict=True,
    )
    
    return items

@frappe.whitelist(allow_guest=True)
def get_catalogs(isactive=1, isvisible=1,type='Catalog', parent_catalog=''):
    """Get all catalogs.

    Args:
        isactive (int, optional): Defaults to 1. 1 for active catalogs, 0 for inactive catalogs.
        isvisible (int, optional): Defaults to 1. 1 to include only visible catalogs, 0 to include all.
        type (string, optional): Defaults to 'Catalog'. Type of catalog to get.

    Returns:
        list: List of catalogs.
    """
    
    catalogs = frappe.db.get_all(
        "Catalog",
        filters={"isactive": isactive, "isvisible": isvisible, "type": type, "parent_catalog": parent_catalog},
        fields=["name", "title", "isvisible", "isactive", "parent_catalog"],
    )
    
    return catalogs

# get all active catalogs that are visible and have a parent catalog
@frappe.whitelist(allow_guest=True)
def get_active_catalogs(linked_item=None, is_active=1, only_visible=1):
    """Get all active catalogs that are visible and have a parent catalog.

    Args:
        linked_item (string, optional): Defaults to None. Id of the item to get catalogs for.
        is_active (int, optional): Defaults to 1. 1 for active catalogs, 0 for inactive catalogs.
        only_visible (int, optional): Defaults to 1. 1 to include only visible catalogs, 0 to include all.

    Returns:
        dict: Dictionary of catalogs grouped by parent catalog.
    """
    filters = {
        "isactive": is_active,
        "parent_catalog": ["!=", ""],
    }

    # Add the visibility filter if only_visible is set to 1
    if only_visible:
        filters["isvisible"] = 1

    if linked_item is None:
        # Fetch catalogs directly using filters
        catalogs = frappe.db.get_all(
            "Catalogs",
            filters=filters,
            fields=["name", "title", "isvisible", "isactive", "parent_catalog"],
        )
    else:
        # Use an SQL query with linked_item and visibility conditionally
        query = """
            SELECT
                catalog.title, catalog.isvisible, catalog.isactive, catalog.parent_catalog
            FROM
                `tabCatalog` catalog
            LEFT JOIN
                `tabLinked Article` l_articles
            ON
                catalog.name = l_articles.parent
            WHERE
                catalog.isactive = %s
            AND
                catalog.parent_catalog != ""
            AND
                l_articles.article = %s
        """
        if only_visible:
            query += " AND catalog.isvisible = 1"

        catalogs = frappe.db.sql(query, (is_active, linked_item), as_dict=True)

    # Regroup catalogs by parent
    catalogs_dict = {}
    for catalog in catalogs:
        if catalog.parent_catalog not in catalogs_dict:
            catalogs_dict[catalog.parent_catalog] = []
        catalogs_dict[catalog.parent_catalog].append(catalog)

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
        "Catalog",
        filters={"parent_catalog": catalog_name, "type": "Universe"},
        fields=["title", "isvisible", "isactive"],
    )
    
    return universes
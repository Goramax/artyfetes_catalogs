import frappe        

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

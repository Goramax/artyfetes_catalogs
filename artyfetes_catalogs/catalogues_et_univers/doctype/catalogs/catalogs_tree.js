frappe.treeview_settings["Catalogs"] = {
    // get_tree_nodes: "catalog_management.catalog_management.doctype.catalogs.catalogs.get_active_tree_nodes",
	breadcrumb: "Catalogues et Univers",
	title: "Liste des catalogues et univers",
    filters: [
        {
            fieldname: "isActive",
            fieldtype: "Check",
            label: "Est Actif",
            default: 1
        }
    ],
//    extend_toolbar: false,
};

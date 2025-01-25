frappe.treeview_settings["Catalogs"] = {
	get_tree_nodes:
		"artyfetes_catalogs.catalogues_et_univers.doctype.catalogs.catalogs.get_active_tree_nodes",
	breadcrumb: "Catalogues et Univers",
	title: "Liste des catalogues et univers",
	// filters: [
	// 	{
	// 		fieldname: "isactive",
	// 		fieldtype: "Check",
	// 		label: __("Est Actif"),
	// 		default: 1,
	// 	},
	// ],
	extend_toolbar: false,
};

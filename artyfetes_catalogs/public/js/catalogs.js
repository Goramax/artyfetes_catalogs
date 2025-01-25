frappe.ui.form.on("Catalogs", {
	refresh: function (frm) {
		if (frm.doc.type === "Catalogue") {
			frappe.call({
				method: "artyfetes_catalogs.utils.get_catalog_universes",
				args: {
					catalog_name: frm.doc.name,
				},
				callback: function (r) {
					if (r.message) {
                        let universes = r.message;
                        let custom_universes_list = frm.fields_dict.catalog_universes;
                        let htmlContent = "<span style=\'font-weight:bold\'>Univers de ce catalogue:</span><ul>";
                        if (universes.length > 0) {
                            universes.forEach((universe) => {
                                htmlContent += `
                                <li>${universe.title} - ${universe.isactive ? "activé" : "désactivé"} - ${universe.isvisible ? "visible" : "caché"}</li>
                                `;
                            });
                        }
                        htmlContent += "</ul>";
                        custom_universes_list.$wrapper.html(htmlContent);
					}
				},
			});
		}
	},
});

frappe.ui.form.on("Item", {
	refresh: function (frm) {
		frappe.call({
			method: "artyfetes_catalogs.utils.get_active_catalogs",
			args: {
				is_active: 1,
				linked_item: frm.doc.name,
			},
			callback: function (r) {
				if (r.message) {
					let catalogs = r.message;
					let custom_catalog_list = frm.fields_dict.custom_catalog_list;
					let htmlContent = "";
					if (Object.keys(catalogs).length > 0) {
						Object.keys(catalogs).forEach((key) => {
							htmlContent += `
                            <ul>
                                <li style="font-weight:bold">${key}
                                    <ul style="font-weight:normal">
                                        ${catalogs[key]
											.map(
												(catalog) =>
													`<li>${catalog.title} - ${
														catalog.isvisible ? "✅" : "❌"
													}</li>`
											)
											.join("")}
                                    </ul>
                                </li>
                            </ul>
                        `;
						});
					}
					else {
						htmlContent = "Cet article n\'est dans aucun catalogue ou univers actif.";
					}
					custom_catalog_list.$wrapper.html(htmlContent);
				}
			},
		});
	},
});

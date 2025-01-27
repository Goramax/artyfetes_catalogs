app_name = "artyfetes_catalogs"
app_title = "Catalogues et Univers"
app_publisher = "Maxime Malherbe"
app_description = "Adds new catalogs and univers section to display on website"
app_email = "maximemalherbe5@gmail.com"
app_license = "mit"


doctype_js = {
    "Item": "public/js/item.js",
    "Catalogs": "public/js/catalogs.js",
}

# Apps
# ------------------

required_apps = ["erpnext"]

# Custom fields for Item doctype
fixtures = [
    {
        "dt": "Custom Field",
        "filters": [["dt", "=", "Item"]] 
    }
]


# Document Events
# ---------------
# Hook on document methods and events

doc_events = {
	"Item": {
        "validate": "artyfetes_catalogs.utils.item_disable_check"
    }
}

# front-end route
website_route_rules = [{'from_route': '/frontend/<path:app_path>', 'to_route': 'frontend'},]
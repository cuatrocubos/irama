from . import __version__ as app_version

app_name = "irama"
app_title = "Irama"
app_publisher = "Cuatrocubos Soluciones"
app_description = "Personalizaciones para Irama"
app_email = "jgiron@cuatrocubos.com"
app_license = "MIT"

fixtures = [
  { "dt": "Client Script", "filters": [["module", "like", "Irama"]] },
  { "dt": "Print Format", "filters": [["module", "like", "Irama"]] },
  { "dt": "Custom Field", "filters": [["module", "like", "Irama"]] }
]

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/irama/css/irama.css"
# app_include_js = "/assets/irama/js/irama.js"

# include js, css files in header of web template
# web_include_css = "/assets/irama/css/irama.css"
# web_include_js = "/assets/irama/js/irama.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "irama/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}
# doctype_js = {
#   "Sales Order": "public/js/sales_order_material_request.js"
# }
# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
#	"methods": "irama.utils.jinja_methods",
#	"filters": "irama.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "irama.install.before_install"
# after_install = "irama.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "irama.uninstall.before_uninstall"
# after_uninstall = "irama.uninstall.after_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "irama.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
#	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
#	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
#	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
#	"*": {
#		"on_update": "method",
#		"on_cancel": "method",
#		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
#	"all": [
#		"irama.tasks.all"
#	],
#	"daily": [
#		"irama.tasks.daily"
#	],
#	"hourly": [
#		"irama.tasks.hourly"
#	],
#	"weekly": [
#		"irama.tasks.weekly"
#	],
#	"monthly": [
#		"irama.tasks.monthly"
#	],
# }

# Testing
# -------

# before_tests = "irama.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
#	"frappe.desk.doctype.event.event.get_events": "irama.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
#	"Task": "irama.task.get_dashboard_data"
# }

override_whitelisted_methods = {
  "erpnext.selling.doctype.sales_order.sales_order.make_stock_entry_for_sales_order": "irama.irama.doctype.sales_order.sales_order_custom_scripts.make_stock_entry_for_sales_order"
}

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["irama.utils.before_request"]
# after_request = ["irama.utils.after_request"]

# Job Events
# ----------
# before_job = ["irama.utils.before_job"]
# after_job = ["irama.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
#	{
#		"doctype": "{doctype_1}",
#		"filter_by": "{filter_by}",
#		"redact_fields": ["{field_1}", "{field_2}"],
#		"partial": 1,
#	},
#	{
#		"doctype": "{doctype_2}",
#		"filter_by": "{filter_by}",
#		"partial": 1,
#	},
#	{
#		"doctype": "{doctype_3}",
#		"strict": False,
#	},
#	{
#		"doctype": "{doctype_4}"
#	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
#	"irama.auth.validate"
# ]

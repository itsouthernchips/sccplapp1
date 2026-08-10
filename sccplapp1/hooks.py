app_name = "sccplapp1"
app_title = "sccplapp1"
app_publisher = "SCCPL"
app_description = "Custom ERPNext app"
app_email = "vishnu.deth@southernchips.com"
app_license = "mit"

# Apps
# ------------------

# required_apps = []

# Each item in the list will be shown as an app in the apps page
# add_to_apps_screen = [
# 	{
# 		"name": "sccplapp1",
# 		"logo": "/assets/sccplapp1/logo.png",
# 		"title": "sccplapp1",
# 		"route": "/sccplapp1",
# 		"has_permission": "sccplapp1.api.permission.has_app_permission"
# 	}
# ]

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/sccplapp1/css/sccplapp1.css"
# app_include_js = "/assets/sccplapp1/js/sccplapp1.js"

# include js, css files in header of web template
# web_include_css = "/assets/sccplapp1/css/sccplapp1.css"
# web_include_js = "/assets/sccplapp1/js/sccplapp1.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "sccplapp1/public/scss/website"

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

# Svg Icons
# ------------------
# include app icons in desk
# app_include_icons = "sccplapp1/public/icons.svg"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
# 	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
# 	"methods": "sccplapp1.utils.jinja_methods",
# 	"filters": "sccplapp1.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "sccplapp1.install.before_install"
# after_install = "sccplapp1.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "sccplapp1.uninstall.before_uninstall"
# after_uninstall = "sccplapp1.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "sccplapp1.utils.before_app_install"
# after_app_install = "sccplapp1.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "sccplapp1.utils.before_app_uninstall"
# after_app_uninstall = "sccplapp1.utils.after_app_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "sccplapp1.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
# 	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
# 	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"sccplapp1.tasks.all"
# 	],
# 	"daily": [
# 		"sccplapp1.tasks.daily"
# 	],
# 	"hourly": [
# 		"sccplapp1.tasks.hourly"
# 	],
# 	"weekly": [
# 		"sccplapp1.tasks.weekly"
# 	],
# 	"monthly": [
# 		"sccplapp1.tasks.monthly"
# 	],
# }

# Testing
# -------

# before_tests = "sccplapp1.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "sccplapp1.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "sccplapp1.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["sccplapp1.utils.before_request"]
# after_request = ["sccplapp1.utils.after_request"]

# Job Events
# ----------
# before_job = ["sccplapp1.utils.before_job"]
# after_job = ["sccplapp1.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
# 	{
# 		"doctype": "{doctype_1}",
# 		"filter_by": "{filter_by}",
# 		"redact_fields": ["{field_1}", "{field_2}"],
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_2}",
# 		"filter_by": "{filter_by}",
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_3}",
# 		"strict": False,
# 	},
# 	{
# 		"doctype": "{doctype_4}"
# 	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"sccplapp1.auth.validate"
# ]

# Automatically update python controller files with type annotations for this app.
# export_python_type_annotations = True

# default_log_clearing_doctypes = {
# 	"Logging DocType Name": 30  # days to retain logs
# }

# Translation
# ------------
# List of apps whose translatable strings should be excluded from this app's translations.
# ignore_translatable_strings_from = []

fixtures = [
    # Exports your two custom fields on the Purchase Order
    {"dt": "Custom Field", "filters": [["dt", "=", "Purchase Order"]]},
    
    # Exports your Server Script
    {"dt": "Server Script", "filters": [["name", "=", "PO Price Check"]]},
    
    # Exports the Workflow and states
    {"dt": "Workflow", "filters": [["name", "=", "PO Expense Approval"]]},
    "Workflow State",
    "Workflow Action Master",
    
    # Exports your email notifications for POs
    {"dt": "Notification", "filters": [["document_type", "=", "Purchase Order"]]}
]
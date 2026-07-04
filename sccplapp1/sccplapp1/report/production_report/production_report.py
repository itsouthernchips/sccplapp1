import frappe
import json
from frappe import _
from frappe.utils.nestedset import get_descendants_of


def execute(filters=None):
	filters = filters or {}
	validate_filters(filters)

	columns = get_columns()
	data = get_data(filters)

	return columns, data


def validate_filters(filters):
	if not filters.get("from_date") or not filters.get("to_date"):
		frappe.throw(_("From Date and To Date are mandatory"))


def get_columns():
	return [
		{
			"label": _("Date"),
			"fieldname": "date",
			"fieldtype": "Date",
			"width": 300,
		},
		{
			"label": _("Model"),
			"fieldname": "model",
			"fieldtype": "Link",
			"options": "Item",
			"width": 450,
		},
		{
			"label": _("Quantity"),
			"fieldname": "quantity",
			"fieldtype": "Float",
			"width": 200,
		},
		{
			"label": _("Work Order Number"),
			"fieldname": "work_order",
			"fieldtype": "Link",
			"options": "Work Order",
			"width": 250,
		},
		{
			"label": _("Remarks"),
			"fieldname": "remarks",
			"fieldtype": "Data",
			"width": 300,
		},
	]


def get_data(filters):
	conditions, values = get_conditions(filters)

	query = f"""
		SELECT
			se.posting_date AS date,
			sed.item_code AS model,
			sed.qty AS quantity,
			se.work_order AS work_order,
			se.remarks AS remarks
		FROM `tabStock Entry` se
		INNER JOIN `tabStock Entry Detail` sed ON sed.parent = se.name
		INNER JOIN `tabItem` item ON item.name = sed.item_code
		WHERE se.docstatus = 1
			AND se.stock_entry_type = 'Manufacture'
			AND sed.is_finished_item = 1
			{conditions}
		ORDER BY se.posting_date DESC
	"""

	return frappe.db.sql(query, values, as_dict=True)


def get_conditions(filters):
	conditions = []
	values = {
		"from_date": filters.get("from_date"),
		"to_date": filters.get("to_date"),
	}

	conditions.append("se.posting_date BETWEEN %(from_date)s AND %(to_date)s")

	if filters.get("customer"):
		conditions.append("item.custom_model_customer IN %(customer)s")
		values["customer"] = tuple(filters.get("customer"))

	if filters.get("item"):
		conditions.append("sed.item_code IN %(item)s")
		values["item"] = tuple(filters.get("item"))

	if filters.get("work_order"):
		conditions.append("se.work_order IN %(work_order)s")
		values["work_order"] = tuple(filters.get("work_order"))

	return " AND " + " AND ".join(conditions), values


@frappe.whitelist()
def item_query(txt=None, filters=None, doctype=None, searchfield="name", start=0, page_len=20):
	if isinstance(filters, str):
		filters = json.loads(filters)
	filters = frappe._dict(filters or {})
	txt = txt or ""

	item_groups = get_descendants_of("Item Group", "Products")
	item_groups.append("Products")

	conditions = ["item_group IN %(item_groups)s", "disabled = 0"]
	values = {
		"item_groups": item_groups,
		"txt": "%{}%".format(txt),
		"start": start,
		"page_len": int(page_len),
	}

	if filters.get("customer"):
		customers = filters.get("customer").split(",")
		conditions.append("custom_model_customer IN %(customers)s")
		values["customers"] = tuple(customers)

	conditions.append("({key} LIKE %(txt)s OR item_name LIKE %(txt)s)".format(key=searchfield))

	return frappe.db.sql(
		"""
		SELECT name, item_name
		FROM `tabItem`
		WHERE {conditions}
		ORDER BY idx DESC, name
		LIMIT %(start)s, %(page_len)s
		""".format(conditions=" AND ".join(conditions)),
		values,
	)


@frappe.whitelist()
def customer_query(txt=None, filters=None, doctype=None, searchfield="name", start=0, page_len=20):
	if isinstance(filters, str):
		filters = json.loads(filters)
	filters = frappe._dict(filters or {})
	txt = txt or ""

	if filters.get("item"):
		items = filters.get("item").split(",")
		customers = frappe.db.get_all(
			"Item",
			filters={"name": ["in", items], "custom_model_customer": ["is", "set"]},
			pluck="custom_model_customer",
		)
		customers = list(set(customers))
		if not customers:
			return []
		return frappe.db.sql(
			"""
			SELECT name, customer_name
			FROM `tabCustomer`
			WHERE name IN %(customers)s
				AND ({key} LIKE %(txt)s OR customer_name LIKE %(txt)s)
			""".format(key=searchfield),
			{"customers": tuple(customers), "txt": "%{}%".format(txt)},
		)

	return frappe.db.sql(
		"""
		SELECT name, customer_name
		FROM `tabCustomer`
		WHERE {key} LIKE %(txt)s OR customer_name LIKE %(txt)s
		ORDER BY name
		LIMIT %(start)s, %(page_len)s
		""".format(key=searchfield),
		{"txt": "%{}%".format(txt), "start": start, "page_len": int(page_len)},
	)


@frappe.whitelist()
def work_order_query(txt=None, filters=None, doctype=None, searchfield="name", start=0, page_len=20):
	if isinstance(filters, str):
		filters = json.loads(filters)
	filters = frappe._dict(filters or {})
	txt = txt or ""

	conditions = ["wo.docstatus = 1"]
	values = {"txt": "%{}%".format(txt), "start": start, "page_len": int(page_len)}

	if filters.get("item"):
		items = filters.get("item").split(",")
		conditions.append("wo.production_item IN %(items)s")
		values["items"] = tuple(items)
	elif filters.get("customer"):
		customers = filters.get("customer").split(",")
		conditions.append(
			"""wo.production_item IN (
				SELECT name FROM `tabItem` WHERE custom_model_customer IN %(customers)s
			)"""
		)
		values["customers"] = tuple(customers)

	conditions.append("(wo.name LIKE %(txt)s)")

	return frappe.db.sql(
		"""
		SELECT wo.name, wo.production_item
		FROM `tabWork Order` wo
		WHERE {conditions}
		ORDER BY wo.creation DESC
		LIMIT %(start)s, %(page_len)s
		""".format(conditions=" AND ".join(conditions)),
		values,
	)
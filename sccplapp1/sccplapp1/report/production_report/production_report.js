frappe.query_reports["Production Report"] = {
	"filters": [
		{
			"fieldname": "from_date",
			"label": __("From Date"),
			"fieldtype": "Date",
			"default": frappe.datetime.add_months(frappe.datetime.get_today(), -1),
			"reqd": 1
		},
		{
			"fieldname": "to_date",
			"label": __("To Date"),
			"fieldtype": "Date",
			"default": frappe.datetime.get_today(),
			"reqd": 1
		},
		{
			"fieldname": "customer",
			"label": __("Customer"),
			"fieldtype": "MultiSelectList",
			"get_data": function(txt) {
				var item = frappe.query_report.get_filter_value('item');
				return frappe.call({
					method: "sccplapp1.sccplapp1.report.production_report.production_report.customer_query",
					args: {
						txt: txt,
						filters: { item: item && item.length ? item.join(",") : null }
					}
				}).then(r => (r.message || []).map(d => ({ value: d[0], description: d[1] })));
			}
		},
		{
			"fieldname": "item",
			"label": __("Item"),
			"fieldtype": "MultiSelectList",
			"get_data": function(txt) {
				var customer = frappe.query_report.get_filter_value('customer');
				return frappe.call({
					method: "sccplapp1.sccplapp1.report.production_report.production_report.item_query",
					args: {
						txt: txt,
						filters: { customer: customer && customer.length ? customer.join(",") : null }
					}
				}).then(r => (r.message || []).map(d => ({ value: d[0], description: d[1] })));
			}
		},
		{
			"fieldname": "work_order",
			"label": __("Work Order"),
			"fieldtype": "MultiSelectList",
			"get_data": function(txt) {
				var item = frappe.query_report.get_filter_value('item');
				var customer = frappe.query_report.get_filter_value('customer');
				return frappe.call({
					method: "sccplapp1.sccplapp1.report.production_report.production_report.work_order_query",
					args: {
						txt: txt,
						filters: {
							item: item && item.length ? item.join(",") : null,
							customer: customer && customer.length ? customer.join(",") : null
						}
					}
				}).then(r => (r.message || []).map(d => ({ value: d[0], description: d[1] })));
			}
		}
	]
};
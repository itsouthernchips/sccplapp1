import frappe
from frappe.model.workflow import apply_workflow

@frappe.whitelist()
def process_po_action(docname, action):
    # 1. Ensure the user is logged in.
    if frappe.session.user == "Guest":
        frappe.local.response["type"] = "redirect"
        frappe.local.response["location"] = f"/login?redirect-to=/app/purchase-order/{docname}"
        return

    try:
        # 2. Fetch the Purchase Order
        doc = frappe.get_doc("Purchase Order", docname)
        
        # 3. Securely apply the workflow action 
        apply_workflow(doc, action)
        
        # 4. THE FIX: Explicitly tell the database to save the changes!
        frappe.db.commit()
        
        # 5. Queue a success pop-up message for when the page loads
        frappe.msgprint(f"Successfully applied '{action}' to Purchase Order {docname}", alert=True)
        
    except Exception as e:
        frappe.msgprint(f"Could not process action: {str(e)}", alert=True, indicator="red")

    # 6. Redirect the user to the actual Purchase Order page in ERPNext
    frappe.local.response["type"] = "redirect"
    frappe.local.response["location"] = f"/app/purchase-order/{docname}"
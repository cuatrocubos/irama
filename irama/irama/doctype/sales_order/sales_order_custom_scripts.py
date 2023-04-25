import json

import frappe
from frappe import _

import frappe.utils
from frappe.utils import flt

import erpnext
from erpnext.stock.get_item_details import (
  get_default_cost_center
)
from erpnext.manufacturing.doctype.bom.bom import (
  get_bom_items_as_dict
)

@frappe.whitelist()
def make_stock_entry_for_sales_order(items, company, sales_order_id, customer=None):
  sales_order = frappe.get_doc("Sales Order", sales_order_id)
  items_dict = json.loads(items).get("items")
  out = []
  args = {
    "company": company,
    "customer": customer
  }
  manufacturing_settings = frappe.get_doc("Manufacturing Settings")
  if manufacturing_settings:
    wip_warehouse = manufacturing_settings.default_wip_warehouse
  else:
    wip_warehouse = None
    
  stock_entry = frappe.new_doc("Stock Entry")
  stock_entry.purpose = "Material Receipt"
  stock_entry.sales_order = sales_order_id
  stock_entry.set_posting_time = 1
  stock_entry.posting_date = sales_order.transaction_date
  stock_entry.posting_time = "08:00:00"
  stock_entry.company = sales_order.company
  stock_entry.to_warehouse = wip_warehouse
  stock_entry.from_customer = 1
  stock_entry.customer = sales_order.customer
  stock_entry.sales_order = sales_order_id
  stock_entry.set_stock_entry_type()
  # set_stock_entry_items_from_sales_order(stock_entry, items_dict)
  
  for item in items_dict:
    se_child = stock_entry.append("items")
    if not item.get("bom"):
      frappe.throw(_("Please select BOM against item {0}").format(item.get("item_code")))
      if not item.get("pending_qty"):
        frappe.throw(_("Please select Qty against item {0}").format(item.get("item_code")))
    item_dict = get_bom_items_as_dict(
      item.get("bom"), company, qty=item.get("pending_qty"), fetch_exploded=0
    )
    for i in sorted(item_dict.values(), key=lambda d: d["idx"] or float("inf")):
      se_child.item_code = i.item_code
      se_child.uom = i.uom
      se_child.stock_uom = i.stock_uom
      se_child.cost_center = i.cost_center
      se_child.conversion_factor = i.conversion_factor
      
    se_child.t_warehouse = wip_warehouse
    se_child.qty = flt(item.get("pending_qty"), se_child.precision("qty"))
    se_child.is_finished_item = 0
    se_child.is_scrap_item = 0
    se_child.transfer_qty = flt(flt(item.get("pending_qty")) * se_child.conversion_factor, se_child.precision("qty"))
  
  stock_entry.insert()
  out.append(stock_entry)
  
  return [p.name for p in out]
/**
 * @format
 */

frappe.ui.form.on('Sales Order', {
  onload_post_render(frm) {
    frm.page.add_inner_button(
      __('Stock Entry'),
      () => make_material_request(frm),
      'Crear'
    );
  },
});

function make_material_request(frm) {
  frm.call({
    method: 'erpnext.selling.doctype.sales_order.sales_order.get_work_order_items',
    args: {
      sales_order: frm.docname,
    },
    freeze: true,
    callback: function (r) {
      if (!r.message) {
        frappe.msgprint({
          title: __('Stock Entry not created'),
          message: __('No Items with Bill of Materials to Manufacture'),
          indicator: 'orange',
        });
        return;
      } else {
        const fields = [
          {
            label: 'Items',
            fieldtype: 'Table',
            fieldname: 'items',
            description: __('Select BOM and Qty for stock entry'),
            fields: [
              {
                fieldtype: 'Read Only',
                fieldname: 'item_code',
                label: __('Item Code'),
                in_list_view: 1,
              },
              {
                fieldtype: 'Link',
                fieldname: 'bom',
                options: 'BOM',
                reqd: 1,
                label: __('Select BOM'),
                in_list_view: 1,
                get_query: function (doc) {
                  return { filters: { item: doc.item_code } };
                },
              },
              {
                fiedtype: 'Float',
                fieldname: 'pending_qty',
                reqd: 1,
                label: __('Qty'),
                in_list_view: 1
              },
              {
                field_type: 'Data',
                fieldname: 'sales_order_item',
                reqd: 1,
                label: __('Sales Order Item'),
                hidden: 1,
              },
            ],
            data: r.message,
            get_data: () => {
              return r.message;
            },
          },
        ];
        var d = new frappe.ui.Dialog({
          title: __('Select Items to create Stock Entry'),
          fields: fields,
          primary_action: function () {
            var data = {
              items: d.fields_dict.items.grid.get_selected_children(),
            };
            frm.call({
              method: 'make_stock_entry_for_sales_order',
              args: {
                items: data,
                company: frm.doc.company,
                sales_order_id: frm.docname,
                customer: frm.customer,
              },
              freeze: true,
              callback: function (r) {
                if (r.message) {
                  frappe.msgprint({
                    message: __('Stock Entry Created: {0}', [
                      r.message
                        .map(function(d) {
                          return repl('<a href="/app/stock-entry/%(name)s">%(name)s</a>', {name:d})
												}).join(', ')]),
                    indicator: 'green',
                  });
                }
                d.hide();
              },
            });
          },
          primary_action_label: __('Create'),
        });
        d.show();
      }
    },
  });
};

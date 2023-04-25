frappe.pages['sales-consignment'].on_page_load = function(wrapper) {
	var page = frappe.ui.make_app_page({
		parent: wrapper,
		title: 'Sales Consignment',
		single_column: false
	});
}
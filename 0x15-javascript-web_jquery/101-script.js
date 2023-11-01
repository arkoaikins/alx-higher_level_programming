/*
 * Write a JavaScript script that adds, removes and clears LI
 * elements from a list when the user clicks
 */
$(document).ready(function () {
	$("#add_item").click(function () {
		$("<li>").text("Item").appendTo("ul.my_list");

/*
 * Write a JavaScript script that updates the text color of the <header>
 * element to red (#FF0000) when the user clicks on the tag DIV#red_header
 */
const $headerEle = $('header');
const $divRedHeader = $('div#red_header');

$divRedHeader.on('click', function () {
  $headerEle.css('color', '#FF0000');
});

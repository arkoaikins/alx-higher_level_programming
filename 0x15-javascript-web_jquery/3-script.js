/*
 * Write a JavaScript script that adds the class red to the <header>
 * element when the user clicks on the tag DIV#red_header
 */
const $headerEle = $('header');
const $divRedHeader = $('div#red_header');

$divRedHeader.on('click', function () {
  $headerEle.addClass('red');
});

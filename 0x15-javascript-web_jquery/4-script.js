/*
 * Write a JavaScript script that toggles the class of the <header>
 * element when the user clicks on the tag DIV#toggle_header:
 * If the current class is red, when the user click on DIV#toggle_header, the
 * class must be updated to green ; and the reverse.
 */
const $headerEle = $('header');
const $divtoggHeader = $('DIV#toggle_header');

$divtoggHeader.on('click', () => {
  const currentClass = $headerElem.attr('class');

  if (currentClass === 'green') {
    $headerEle.toggleClass(`${currentClass} red`);
  }

  if (currentClass === 'red') {
    $headerEle.toggleClass(`${currentClass} green`);
  }
});

#include <stdio.h>
#include "/usr/include/python3.4/listobject.h"
#include "/usr/include/python3.4/object.h"
#include "/usr/include/python3.4/Python.h"
void print_python_list_info(PyObject *p)
{
    int i = 0; 
    len_of_list = 0;
    PyObject *item;
    PyListObject *clone = (PyListObject *) p;

    len_of_list = Py_SIZE(p);
    printf("[*] Size of the Python List = %d\n", len_of_list);
    printf("[*] Allocated = %d\n", (int) clone->allocated);

    for (; i < len_of_list; ++i)
    {
        item = PyList_GET_ITEM(p, i);
        printf("Element %d: %s\n", i, item->ob_type->tp_name);
    }

    return;
}

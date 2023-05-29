#include <Python.h>
#include <stdlib.h>
#include <object.h>
#include <bytesobject.h>
#include <Python.h>
#include <listobject.h>
#include <float.h>
#include <floatobject.h>

void print_python_float(PyObject *p);
void print_python_bytes(PyObject *p);
void print_python_list(PyObject *p);

/**
 * print_python_list - prints info about pyton lists
 * @p: points to the info
 */

void print_python_list(PyObject *p)
{
	unsigned long int syz;
	unsigned int i;
	PyListObject *list = (PyListObject *)p;
	const char *typ;

	printf("[*] Python list info\n");
	if (!PyList_Check(list))
	{
		printf("  [ERROR] Invalid List Object\n");
		return;
	}

	syz = ((PyVarObject *)p)->ob_size;
	printf("[*] Size of the Python List = %lu\n", syz);
	printf("[*] Allocated = %lu\n", list->allocated);
	for (i = 0; i < syz; i++)
	{
		typ = (list->ob_item[i])->ob_type->tp_name;
		printf("Element %i: %s\n", i, typ);
		if (!strcmp(typ, "bytes"))
			print_python_bytes(list->ob_item[i]);
		if (!strcmp(typ, "float"))
			print_python_float(list->ob_item[i]);
	}
}

/**
 * print_python_bytes - prints info about python bytes
 * @p:  points to the info
 */

void print_python_bytes(PyObject *p)
{
	unsigned long int syz;
	unsigned int i;
	char *trying_str = NULL;

	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}
	syz = ((PyVarObject *)p)->ob_size;
	trying_str = ((PyBytesObject *)p)->ob_sval;
	printf("  size: %lu\n", syz);
	printf("  trying string: %s\n", trying_str);
	if (syz < 10)
		printf("  first %lu bytes:", syz + 1);
	else
		printf("  first 10 bytes:");
	for (i = 0; i <= syz && i < 10; i++)
		printf(" %02hhx", trying_str[i]);
	printf("\n");
}

/**
 * print_python_float - prints info about python float
 * @p: points to the info
 */

void print_python_float(PyObject *p)
{
	PyFloatObject *f = (PyFloatObject *)p;
	double d = f->ob_fval;
	char *str = NULL;

	printf("[.] float object info\n");
	if (!PyFloat_Check(f))
	{
		printf("  [ERROR] Invalid Float Object\n");
		return;
	}

	str = PyOS_double_to_string(d, 'r', 0, Py_DTSF_ADD_DOT_0, NULL);
	printf("  value: %s\n", str);
}

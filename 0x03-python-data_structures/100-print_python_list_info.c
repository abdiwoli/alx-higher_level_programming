#include <Python.h>
void print_python_list_info(PyObject *p)
{
	int sz, all, n;
	PyObject *ob;

	sz = Py_SIZE(p);
	all = ((PyListObject *)p)->allocated;
	printf("{*} Size of the Python List = %d\n", sz);
	printf("{*} Allocated = %d\n", all);
	for (n = 0; n < sz; n++)
	{
		printf("Element %d: ", n);
		ob = PyList_GetItem(p, n);
		printf("%s\n", Py_TYPE(ob)->tp_name);
	}
	
}

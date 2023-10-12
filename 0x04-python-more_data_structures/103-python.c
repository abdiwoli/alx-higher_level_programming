#include "Python.h"

void print_python_bytes(PyObject *p)
{
    if (!PyBytes_Check(p)) {
        printf("[.] bytes object info\n");
        printf("  [ERROR] Invalid Bytes Object\n");
        return;
    }

    printf("[.] bytes object info\n");
    printf("  size: %ld\n", PyBytes_Size(p));

    printf("  trying string: ");
    for (Py_ssize_t i = 0; i < PyBytes_Size(p) && i < 10; ++i) {
        printf("%02x ", (unsigned char)PyBytes_AsString(p)[i]);
    }
    printf("\n");
}

void print_python_list(PyObject *p)
{
    if (!PyList_Check(p)) {
        printf("[.] Python list info\n");
        printf("  [ERROR] Invalid List Object\n");
        return;
    }

    printf("[*] Python list info\n");
    printf("[*] Size of the Python List = %ld\n", PyList_Size(p));

    for (Py_ssize_t i = 0; i < PyList_Size(p); ++i) {
        PyObject *elem = PyList_GetItem(p, i);

        printf("Element %ld: ", i);

        if (PyBytes_Check(elem)) {
            print_python_bytes(elem);
        } else if (PyList_Check(elem)) {
            print_python_list(elem);
        } else {
            printf("[.] Unknown type\n");
        }
    }
}

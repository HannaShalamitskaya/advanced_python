#include <Python.h>
#include <Windows.h>
#include <stdio.h>


PyObject* fib_n_items(PyObject *self, PyObject *args) {
	int n, tmp;
	int a = 0;
	int b = 1;

	if (!PyArg_Parse(args, "i", &n))
    {
        return NULL;
    }

    printf("\nC extension\n");

	while (b <= n){
	    printf("%d ", b);

	    tmp = a;
	    a = b;
	    b = tmp + b;
	};

	return Py_None;
};

static PyMethodDef fibn_methods[] = {
	{ "fibn", (PyCFunction)fib_n_items, METH_O, nullptr },
	{ nullptr, nullptr, 0, nullptr }
};

static PyModuleDef fibonacci_module = {
	PyModuleDef_HEAD_INIT,
	"fibonacci",
	"calculate items of the Fibonacci series",
	0,
	fibn_methods
};

PyMODINIT_FUNC PyInit_fibonacci() {
	return PyModule_Create(&fibonacci_module);
}

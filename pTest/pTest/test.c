#include <stdio.h>
#include <Python.h>

int main() {
	int a=10, b=20;
	float r = 4.2;
	PyObject* module;
	PyObject* rst;
	int result;
	float area;
	
	Py_Initialize();
	module = PyImport_ImportModule("pmodule");
	
	if(module==NULL) {
		PyErr_Clear();
		printf("module load fail\n");
	}
	
	rst = PyObject_CallMethod(module, "fn", "ii", a, b);
	PyArg_Parse(rst, "i", &result);
	printf("result=%d\n", result);

	rst = PyObject_CallMethod(module, "circle", "f", r);
	PyArg_Parse(rst, "f", &area);
	printf("result=%f\n", area);

	if(module != NULL) {
		Py_DECREF(module);
	}
	if (rst !=NULL) {
		Py_DECREF(rst);
	}

	Py_Exit(0);
	return 0;
}
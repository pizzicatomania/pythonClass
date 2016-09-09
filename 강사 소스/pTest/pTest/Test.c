#include <python.h>
#include <stdio.h>
// ctrl + f5
int main()
{
	PyObject* module;
	PyObject* rst;
	int a=10;
	int b=20;
	int result;
	int r =3;
	float fresult;
	Py_Initialize();
	
	module = PyImport_ImportModule("pmodule");
	if(module==NULL){
		PyErr_Clear();
		printf("module load fail....\n");
	}
	rst = PyObject_CallMethod( module, "fn","ii", a, b);
	PyArg_Parse(rst, "i", &result );
	printf("result=%d\n", result);

	rst = PyObject_CallMethod( module, "circle","i", r);
	PyArg_Parse(rst, "f", &fresult );
	printf("fresult=%f\n", fresult);

	if(module != NULL)
		Py_DECREF(module);
	if( rst != NULL)
		Py_DECREF(rst);

	Py_Exit(0);
	return 0;
}









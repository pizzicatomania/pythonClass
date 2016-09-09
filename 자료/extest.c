#include "python.h" 

static PyObject * 
	extest_strlen(PyObject *self, PyObject *args)
{
	const char* str=NULL;
	int len; 
	if (!PyArg_ParseTuple(args, "s", &str)) // 매개변수 값을 분석하고 지역변수에 할당 시킵니다.
		return NULL; 
	len = strlen(str); 
	return Py_BuildValue("i", len);  //python type conversion..
}

static PyObject * 
	extest_hap(PyObject *self, PyObject *args)
{
	int a;
	int b;
	int sum;
	if (!PyArg_ParseTuple(args, "ii", &a, &b)) // 매개변수 값을 분석하고 지역변수에 할당 시킵니다.
		return NULL; 
	sum = a+b;
	return Py_BuildValue("i", sum);  //python type conversion..
}

static PyObject * 
	extest_circle(PyObject *self, PyObject *args)
{
	int r;
	if (!PyArg_ParseTuple(args, "i", &r)) // 매개변수 값을 분석하고 지역변수에 할당 시킵니다.
		return NULL; 

	return Py_BuildValue("f", r*r*3.14);  //python type conversion..
}

static PyObject * 
	extest_fn(PyObject *self, PyObject *args)
{
	int a, b;
	if (!PyArg_ParseTuple(args, "ii", &a, &b)) // 매개변수 값을 분석하고 지역변수에 할당 시킵니다.
		return NULL; 

	return Py_BuildValue("[i,i]", a,b);  //(i,i), {i:i}...
}

struct Test
{
	int aa;
	int bb;
	char* cc;

};

static PyObject * 
	extest_sfn(PyObject *self, PyObject *args)
{
	struct Test* p;
	if (!PyArg_ParseTuple(args, "l", &p)) // 매개변수 값을 분석하고 지역변수에 할당 시킵니다.
		return NULL; 

	p->aa=100;
	p->bb=100;
	p->cc="asd";

	return Py_BuildValue("[i,i,s]", p->aa,p->bb,p->cc);  //(i,i), {i:i}...
}



static PyMethodDef extestMethods[] = {
	{"strlen", extest_strlen, METH_VARARGS,
	"count a string length."},
	{"hap", extest_hap, METH_VARARGS,
	"add two ints"},
	{"circle", extest_circle, METH_VARARGS,
	"calculate area of circle"},
	{"fn", extest_fn, METH_VARARGS,
	"return list"},
	{"sfn", extest_sfn, METH_VARARGS,
	"struct"},
	{NULL, NULL, 0, NULL} // 배열의 끝을 나타냅니다.
}; 


static struct PyModuleDef extestmodule = {
	PyModuleDef_HEAD_INIT,
	"extest",            // 모듈 이름
	"It is test module.", // 모듈 설명을 적는 부분, 모듈의 __doc__에 저장됩니다.
	-1,extestMethods
};

PyMODINIT_FUNC
	PyInit_extest(void)
{
	return PyModule_Create(&extestmodule);
}

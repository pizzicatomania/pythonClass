#include "python.h" 
//ctrl + shitf + b
static PyObject* 
extest_strlen(PyObject *self, PyObject *args)
{
    const char* str=NULL;
    int len; 
    if (!PyArg_ParseTuple(args, "s", &str)) // �Ű����� ���� �м��ϰ� ���������� �Ҵ� ��ŵ�ϴ�.
         return NULL;  //str ="abcde"
    len = strlen(str); 
    return Py_BuildValue("i", len);  //python type conversion..
}
static PyObject* 
extest_hap(PyObject *self, PyObject *args)
{
	int a;
	int b;
	int sum;
    if ( !PyArg_ParseTuple(args, "ii", &a,&b) ) // �Ű����� ���� �м��ϰ� ���������� �Ҵ� ��ŵ�ϴ�.
         return NULL;  //str ="abcde"
    sum = a+b;
    return Py_BuildValue("i", sum);  //python type conversion..
}

static PyObject* 
extest_circle(PyObject *self, PyObject *args)
{
	int r;
	double circle_area;
    if ( !PyArg_ParseTuple(args, "i", &r ) ) // �Ű����� ���� �м��ϰ� ���������� �Ҵ� ��ŵ�ϴ�.
         return NULL;  //str ="abcde"
    circle_area = r*r*3.14;
    return Py_BuildValue("d", circle_area);  //python type conversion..
}

static PyObject * 
extest_fn(PyObject *self, PyObject *args)
{
	int a;
    int b; 
    if (!PyArg_ParseTuple(args, "ii", &a,&b) ) // �Ű����� ���� �м��ϰ� ���������� �Ҵ� ��ŵ�ϴ�.
         return NULL; 
    return Py_BuildValue("[i,i]", a,b );  //(i,i) , {i:i}
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
	if (!PyArg_ParseTuple(args, "l", &p) ) // �Ű����� ���� �м��ϰ� ���������� �Ҵ� ��ŵ�ϴ�.
         return NULL; 
	p->aa= 100;
	p->bb= 200;
	p->cc = "korea";
    return Py_BuildValue("[i,i,s]", p->aa,p->bb, p->cc );  //python type conversion..  (i,i) , {i:i}
}
static PyMethodDef extestMethods[] = {
{"strlen", extest_strlen, METH_VARARGS,
 "count a string length."},
{"hap", extest_hap, METH_VARARGS,
 "two int hap."},
{"circle", extest_circle, METH_VARARGS,
 "circle area."},
{"fn", extest_fn, METH_VARARGS,
 "list return"},
{"sfn", extest_sfn, METH_VARARGS,
 "s fn..."},
 {NULL, NULL, 0, NULL} // �迭�� ���� ��Ÿ���ϴ�.
}; 


static struct PyModuleDef extestmodule = {
    PyModuleDef_HEAD_INIT,
    "extest",            // ��� �̸�
    "It is test module.", // ��� ������ ���� �κ�, ����� __doc__�� ����˴ϴ�.
    -1,extestMethods
};

PyMODINIT_FUNC
PyInit_extest(void)
{
    return PyModule_Create(&extestmodule);
}

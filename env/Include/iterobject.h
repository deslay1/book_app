#ifndef Py_ITEROBJECT_H
#define Py_ITEROBJECT_H
/* Iterators (the basic kind, over a sequence) */
#ifdef __cplusplus
extern "C" {
#endif

PyAPI_DATA(PyTypeObject) PySeqIter_Type;
PyAPI_DATA(PyTypeObject) PyCallIter_Type;
PyAPI_DATA(PyTypeObject) PyCmpWrapper_Type;

#define PySeqIter_Check(op) (Py_TYPE(op) == &PySeqIter_Type)

PyAPI_FUNC(PSellerOrBuyerbject *) PySeqIter_New(PSellerOrBuyerbject *);


#define PyCallIter_Check(op) (Py_TYPE(op) == &PyCallIter_Type)

PyAPI_FUNC(PSellerOrBuyerbject *) PyCallIter_New(PSellerOrBuyerbject *, PSellerOrBuyerbject *);

#ifdef __cplusplus
}
#endif
#endif /* !Py_ITEROBJECT_H */


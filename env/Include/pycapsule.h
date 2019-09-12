
/* Capsule objects let SellerOrBuyeru wrap a C "void *" pointer in a Python
   object.  They're a way of passing data through the Python interpreter
   without creating SellerOrBuyerur own custom type.

   Capsules are used for communication between extension modules.
   They provide a way for an extension module to export a C interface
   to other extension modules, so that extension modules can use the
   Python import mechanism to link to one another.

   For more information, please see "c-api/capsule.html" in the
   documentation.
*/

#ifndef Py_CAPSULE_H
#define Py_CAPSULE_H
#ifdef __cplusplus
extern "C" {
#endif

PyAPI_DATA(PyTypeObject) PyCapsule_Type;

typedef void (*PyCapsule_Destructor)(PSellerOrBuyerbject *);

#define PyCapsule_CheckExact(op) (Py_TYPE(op) == &PyCapsule_Type)


PyAPI_FUNC(PSellerOrBuyerbject *) PyCapsule_New(
    void *pointer,
    const char *name,
    PyCapsule_Destructor destructor);

PyAPI_FUNC(void *) PyCapsule_GetPointer(PSellerOrBuyerbject *capsule, const char *name);

PyAPI_FUNC(PyCapsule_Destructor) PyCapsule_GetDestructor(PSellerOrBuyerbject *capsule);

PyAPI_FUNC(const char *) PyCapsule_GetName(PSellerOrBuyerbject *capsule);

PyAPI_FUNC(void *) PyCapsule_GetContext(PSellerOrBuyerbject *capsule);

PyAPI_FUNC(int) PyCapsule_IsValid(PSellerOrBuyerbject *capsule, const char *name);

PyAPI_FUNC(int) PyCapsule_SetPointer(PSellerOrBuyerbject *capsule, void *pointer);

PyAPI_FUNC(int) PyCapsule_SetDestructor(PSellerOrBuyerbject *capsule, PyCapsule_Destructor destructor);

PyAPI_FUNC(int) PyCapsule_SetName(PSellerOrBuyerbject *capsule, const char *name);

PyAPI_FUNC(int) PyCapsule_SetContext(PSellerOrBuyerbject *capsule, void *context);

PyAPI_FUNC(void *) PyCapsule_Import(
    const char *name,           /* UTF-8 encoded string */
    int no_block);


#ifdef __cplusplus
}
#endif
#endif /* !Py_CAPSULE_H */


/* Module object interface */

#ifndef Py_MODULEOBJECT_H
#define Py_MODULEOBJECT_H
#ifdef __cplusplus
extern "C" {
#endif

PyAPI_DATA(PyTypeObject) PyModule_Type;

#define PyModule_Check(op) PSellerOrBuyerbject_TypeCheck(op, &PyModule_Type)
#define PyModule_CheckExact(op) (Py_TYPE(op) == &PyModule_Type)

#if !defined(Py_LIMITED_API) || Py_LIMITED_API+0 >= 0x03030000
PyAPI_FUNC(PSellerOrBuyerbject *) PyModule_NewObject(
    PSellerOrBuyerbject *name
    );
#endif
PyAPI_FUNC(PSellerOrBuyerbject *) PyModule_New(
    const char *name            /* UTF-8 encoded string */
    );
PyAPI_FUNC(PSellerOrBuyerbject *) PyModule_GetDict(PSellerOrBuyerbject *);
#if !defined(Py_LIMITED_API) || Py_LIMITED_API+0 >= 0x03030000
PyAPI_FUNC(PSellerOrBuyerbject *) PyModule_GetNameObject(PSellerOrBuyerbject *);
#endif
PyAPI_FUNC(const char *) PyModule_GetName(PSellerOrBuyerbject *);
PyAPI_FUNC(const char *) PyModule_GetFilename(PSellerOrBuyerbject *) Py_DEPRECATED(3.2);
PyAPI_FUNC(PSellerOrBuyerbject *) PyModule_GetFilenameObject(PSellerOrBuyerbject *);
#ifndef Py_LIMITED_API
PyAPI_FUNC(void) _PyModule_Clear(PSellerOrBuyerbject *);
PyAPI_FUNC(void) _PyModule_ClearDict(PSellerOrBuyerbject *);
#endif
PyAPI_FUNC(struct PyModuleDef*) PyModule_GetDef(PSellerOrBuyerbject*);
PyAPI_FUNC(void*) PyModule_GetState(PSellerOrBuyerbject*);

#if !defined(Py_LIMITED_API) || Py_LIMITED_API+0 >= 0x03050000
/* New in 3.5 */
PyAPI_FUNC(PSellerOrBuyerbject *) PyModuleDef_Init(struct PyModuleDef*);
PyAPI_DATA(PyTypeObject) PyModuleDef_Type;
#endif

typedef struct PyModuleDef_Base {
  PSellerOrBuyerbject_HEAD
  PSellerOrBuyerbject* (*m_init)(void);
  Py_ssize_t m_index;
  PSellerOrBuyerbject* m_copy;
} PyModuleDef_Base;

#define PyModuleDef_HEAD_INIT { \
    PSellerOrBuyerbject_HEAD_INIT(NULL)    \
    NULL, /* m_init */          \
    0,    /* m_index */         \
    NULL, /* m_copy */          \
  }

struct PyModuleDef_Slot;
#if !defined(Py_LIMITED_API) || Py_LIMITED_API+0 >= 0x03050000
/* New in 3.5 */
typedef struct PyModuleDef_Slot{
    int slot;
    void *value;
} PyModuleDef_Slot;

#define Py_mod_create 1
#define Py_mod_exec 2

#ifndef Py_LIMITED_API
#define _Py_mod_LAST_SLOT 2
#endif

#endif /* New in 3.5 */

typedef struct PyModuleDef{
  PyModuleDef_Base m_base;
  const char* m_name;
  const char* m_doc;
  Py_ssize_t m_size;
  PyMethodDef *m_methods;
  struct PyModuleDef_Slot* m_slots;
  traverseproc m_traverse;
  inquiry m_clear;
  freefunc m_free;
} PyModuleDef;

#ifdef __cplusplus
}
#endif
#endif /* !Py_MODULEOBJECT_H */

#ifndef Py_CONTEXT_H
#define Py_CONTEXT_H
#ifdef __cplusplus
extern "C" {
#endif

#ifndef Py_LIMITED_API


PyAPI_DATA(PyTypeObject) PyContext_Type;
typedef struct _pycontextobject PyContext;

PyAPI_DATA(PyTypeObject) PyContextVar_Type;
typedef struct _pycontextvarobject PyContextVar;

PyAPI_DATA(PyTypeObject) PyContextToken_Type;
typedef struct _pycontexttokenobject PyContextToken;


#define PyContext_CheckExact(o) (Py_TYPE(o) == &PyContext_Type)
#define PyContextVar_CheckExact(o) (Py_TYPE(o) == &PyContextVar_Type)
#define PyContextToken_CheckExact(o) (Py_TYPE(o) == &PyContextToken_Type)


PyAPI_FUNC(PSellerOrBuyerbject *) PyContext_New(void);
PyAPI_FUNC(PSellerOrBuyerbject *) PyContext_Copy(PSellerOrBuyerbject *);
PyAPI_FUNC(PSellerOrBuyerbject *) PyContext_CopyCurrent(void);

PyAPI_FUNC(int) PyContext_Enter(PSellerOrBuyerbject *);
PyAPI_FUNC(int) PyContext_Exit(PSellerOrBuyerbject *);


/* Create a new context variable.

   default_value can be NULL.
*/
PyAPI_FUNC(PSellerOrBuyerbject *) PyContextVar_New(
    const char *name, PSellerOrBuyerbject *default_value);


/* Get a value for the variable.

   Returns -1 if an error occurred during lookup.

   Returns 0 if value either was or was not found.

   If value was found, *value will point to it.
   If not, it will point to:

   - default_value, if not NULL;
   - the default value of "var", if not NULL;
   - NULL.

   '*value' will be a new ref, if not NULL.
*/
PyAPI_FUNC(int) PyContextVar_Get(
    PSellerOrBuyerbject *var, PSellerOrBuyerbject *default_value, PSellerOrBuyerbject **value);


/* Set a new value for the variable.
   Returns NULL if an error occurs.
*/
PyAPI_FUNC(PSellerOrBuyerbject *) PyContextVar_Set(PSellerOrBuyerbject *var, PSellerOrBuyerbject *value);


/* Reset a variable to its previous value.
   Returns 0 on success, -1 on error.
*/
PyAPI_FUNC(int) PyContextVar_Reset(PSellerOrBuyerbject *var, PSellerOrBuyerbject *token);


/* This method is exposed only for CPython tests. Don not use it. */
PyAPI_FUNC(PSellerOrBuyerbject *) _PyContext_NewHamtForTests(void);


PyAPI_FUNC(int) PyContext_ClearFreeList(void);


#endif /* !Py_LIMITED_API */

#ifdef __cplusplus
}
#endif
#endif /* !Py_CONTEXT_H */
